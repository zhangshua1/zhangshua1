package com.lxinet.jeesns.service.group.impl;

import com.lxinet.jeesns.core.service.impl.BaseServiceImpl;
import com.lxinet.jeesns.core.utils.ValidUtill;
import com.lxinet.jeesns.core.enums.Messages;
import com.lxinet.jeesns.core.exception.OpeErrorException;
import com.lxinet.jeesns.core.utils.*;
import com.lxinet.jeesns.model.group.Group;
import com.lxinet.jeesns.model.member.Financial;
import com.lxinet.jeesns.model.member.Member;
import com.lxinet.jeesns.model.system.ScoreRule;
import com.lxinet.jeesns.service.group.IGroupService;
import com.lxinet.jeesns.dao.group.IGroupDao;
import com.lxinet.jeesns.service.group.IGroupFansService;
import com.lxinet.jeesns.service.member.IFinancialService;
import com.lxinet.jeesns.service.member.IMemberService;
import com.lxinet.jeesns.service.member.IScoreDetailService;
import com.lxinet.jeesns.service.system.IActionLogService;
import com.lxinet.jeesns.service.system.IConfigService;
import com.lxinet.jeesns.utils.ActionUtil;
import com.lxinet.jeesns.utils.ConfigUtil;
import com.lxinet.jeesns.utils.ScoreRuleConsts;
import com.lxinet.jeesns.service.system.IScoreRuleService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.annotation.Resource;
import java.util.Date;
import java.util.List;
import java.util.Map;

/**
 * Created by zchuanzhao on 2016/12/23.
 */
@Service("groupService")
@Transactional
public class GroupServiceImpl extends BaseServiceImpl<Group> implements IGroupService {
    @Resource
    private IGroupDao groupDao;
    @Resource
    private IGroupFansService groupFansService;
    @Resource
    private IMemberService memberService;
    @Resource
    private IConfigService configService;
    @Resource
    private IActionLogService actionLogService;
    @Resource
    private IScoreDetailService scoreDetailService;
    @Resource
    private IScoreRuleService scoreRuleService;
    @Resource
    private IFinancialService financialService;

    @Override
    public List<Group> list(int status, String key) {
        if (StringUtils.isNotBlank(key)){
            key = "%"+key.trim()+"%";
        }
        List<Group> list = groupDao.list(status,key);
        return list;
    }

    /**
     * ???????????????????????????
     * @param loginMember
     * @param groupId
     * @param type 0?????????1????????????
     * @return
     */
    @Override
    public boolean follow(Member loginMember, Integer groupId, int type) {
        Group group = this.findById(groupId);
        ValidUtill.checkIsNull(group,"???????????????");
        if(type == 0){
            if (group.getFollowPay() == 1){
                Date date = new Date();
                loginMember = memberService.findById(loginMember.getId());
                if (loginMember.getMoney().doubleValue() < group.getPayMoney().doubleValue()){
                    throw new OpeErrorException("?????????????????????????????????????????????????????????????????????"+group.getPayMoney()+"????????????????????????"+loginMember.getMoney()+"???");
                }
                //??????
                memberService.updateMoney(-group.getPayMoney(), loginMember.getId());
                //??????????????????
                Financial financial = new Financial();
                financial.setBalance(loginMember.getMoney() - group.getPayMoney());
                financial.setCreateTime(date);
                financial.setForeignId(group.getId());
                financial.setMemberId(loginMember.getId());
                financial.setMoney(group.getPayMoney());
                financial.setType(1);
                //1???????????????
                financial.setPaymentId(1);
                financial.setRemark("????????????" + group.getName());
                financial.setOperator(loginMember.getName());
                financialService.save(financial);
                double payMoney = group.getPayMoney();
                String feeStr = configService.getValue(ConfigUtil.GROUP_FOLLOW_PAY_FEE);
                double feePercent = 0d;
                try {
                    feePercent = Double.parseDouble(feeStr);
                }catch (Exception e){
                }
                double fee = payMoney * feePercent;
                payMoney -= fee;
                //??????
                Member findMember = memberService.findById(group.getCreator());
                findMember.setMoney(findMember.getMoney() + payMoney);
                memberService.updateMoney(payMoney, findMember.getId());
                //??????????????????
                Financial creFinancial = new Financial();
                creFinancial.setBalance(findMember.getMoney() + group.getPayMoney());
                creFinancial.setCreateTime(date);
                creFinancial.setForeignId(group.getId());
                creFinancial.setMemberId(findMember.getId());
                creFinancial.setMoney(group.getPayMoney());
                creFinancial.setType(0);
                //1???????????????
                creFinancial.setPaymentId(1);
                creFinancial.setRemark("???????????????" + group.getName());
                creFinancial.setOperator(loginMember.getName());
                financialService.save(creFinancial);
                if (fee != 0d){
                    //??????????????????
                    Financial creFeeFinancial = new Financial();
                    creFeeFinancial.setBalance(findMember.getMoney() + payMoney);
                    creFeeFinancial.setCreateTime(date);
                    creFeeFinancial.setForeignId(group.getId());
                    creFeeFinancial.setMemberId(findMember.getId());
                    creFeeFinancial.setMoney(fee);
                    creFeeFinancial.setType(1);
                    //1???????????????
                    creFeeFinancial.setPaymentId(1);
                    creFeeFinancial.setRemark("????????????????????????" + group.getName());
                    creFeeFinancial.setOperator(findMember.getName());
                    financialService.save(creFeeFinancial);
                }
            }

            return groupFansService.save(loginMember,groupId);
        }else {
            //???????????????????????????
            if(loginMember.getId().intValue() == group.getCreator().intValue()){
                throw new OpeErrorException("?????????????????????");
            }
            return groupFansService.delete(loginMember,groupId);
        }

    }

    @Override
    public boolean changeStatus(int id) {
       return groupDao.changeStatus(id) == 1;
    }

    @Override
    public List<Group> listByCustom(int status, int num, String sort) {
        return groupDao.listByCustom(status,num,sort);
    }

    @Override
    public Group findById(int id) {
        return groupDao.findById(id);
    }

    @Override
    @Transactional
    public boolean save(Member loginMember, Group group) {
        loginMember = memberService.findById(loginMember.getId());
        Map<String,String> config = configService.getConfigToMap();
        group.setCreator(loginMember.getId());
        if(loginMember.getIsAdmin() > 0){
            group.setStatus(1);
        }else {
            if("0".equals(config.get(ConfigUtil.GROUP_APPLY))){
                throw new OpeErrorException("???????????????????????????");
            }
            ScoreRule scoreRule = scoreRuleService.findById(ScoreRuleConsts.APPLY_GROUP);
            if (scoreRule != null && loginMember.getScore() < Math.abs(scoreRule.getScore())){
                throw new OpeErrorException("??????????????????????????????????????????????????????????????????" + Math.abs(scoreRule.getScore()) + "???????????????????????????" + loginMember.getScore());
            }
            if("0".equals(config.get(ConfigUtil.GROUP_APPLY_REVIEW))){
                group.setStatus(0);
            }else {
                group.setStatus(1);
            }
        }
        //????????????
        if(StringUtils.isEmpty(group.getLogo())){
            group.setLogo(Const.DEFAULT_IMG_URL);
        }
        //???????????????
        String managerIds = String.valueOf(loginMember.getId());
        group.setManagers(managerIds);
        group.setCanPost(1);
        group.setTopicReview(0);
        if (group.getFollowPay() == 0){
            group.setPayMoney(0d);
        }
        boolean result = groupDao.save(group) == 1;
        if(result){
            //???????????????????????????
            groupFansService.save(loginMember,group.getId());
            //???????????????????????????
            scoreDetailService.scoreBonus(loginMember.getId(), ScoreRuleConsts.APPLY_GROUP, group.getId());
        }
        return result;
    }

    @Override
    public boolean update(Member loginMember, Group group) {
        Group findGroup = this.findById(group.getId());
        ValidUtill.checkIsNull(findGroup, "???????????????");
        if(loginMember.getId().intValue() != findGroup.getCreator().intValue()){
            throw new OpeErrorException("????????????");
        }

        //???????????????
        String managerNames = group.getManagers();
        String managerIds = "";
        String[] names = managerNames.split(",");
        if(names.length > 10){
            throw new OpeErrorException("?????????????????????10???");
        }
        for (String name : names){
            Member member = memberService.findByName(name.trim());
            if(member != null){
                managerIds += member.getId() + ",";
            }
        }
        if(managerIds.length() > 0){
            managerIds = managerIds.substring(0,managerIds.length()-1);
        }
        if(StringUtils.isNotEmpty(group.getLogo())){
            findGroup.setLogo(group.getLogo());
        }
        findGroup.setManagers(managerIds);
        findGroup.setName(group.getName());
        findGroup.setTags(group.getTags());
        findGroup.setCanPost(group.getCanPost());
        findGroup.setTopicReview(group.getTopicReview());
        findGroup.setIntroduce(group.getIntroduce());
        findGroup.setTypeId(group.getTypeId());
        findGroup.setPayMoney(group.getPayMoney());
        return groupDao.update(findGroup) == 1;
    }

    @Override
    public boolean delete(Member loginMember, int id) {
        Group findGroup = this.findById(id);
        ValidUtill.checkIsNull(findGroup, "???????????????");
        boolean result = groupDao.delete(id) == 1;
        if(result){
            actionLogService.save(loginMember.getCurrLoginIp(),loginMember.getId(), ActionUtil.DELETE_GROUP,"ID???"+findGroup.getId()+"????????????"+findGroup.getName());
        }
        return result;
    }


}
