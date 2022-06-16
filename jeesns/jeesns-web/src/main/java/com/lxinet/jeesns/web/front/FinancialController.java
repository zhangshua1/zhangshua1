package com.lxinet.jeesns.web.front;

import com.lxinet.jeesns.core.annotation.Before;
import com.lxinet.jeesns.core.annotation.UsePage;
import com.lxinet.jeesns.core.controller.BaseController;
import com.lxinet.jeesns.core.dto.ResultModel;
import com.lxinet.jeesns.core.model.Page;
import com.lxinet.jeesns.core.utils.PageUtil;
import com.lxinet.jeesns.interceptor.UserLoginInterceptor;
import com.lxinet.jeesns.model.member.Financial;
import com.lxinet.jeesns.model.member.Member;
import com.lxinet.jeesns.model.member.ScoreDetail;
import com.lxinet.jeesns.service.member.IFinancialService;
import com.lxinet.jeesns.service.member.IScoreDetailService;
import com.lxinet.jeesns.utils.MemberUtil;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import javax.annotation.Resource;
import java.util.List;

/**
 * Created by zchuanzhao on 2018/11/28.
 */
@Controller("frontFinancialController")
@RequestMapping("/member/financial/")
@Before(UserLoginInterceptor.class)
public class FinancialController extends BaseController {
    private static final String INDEX_FTL_PATH = "/member/financial/";
    @Resource
    private IFinancialService financialService;

    @UsePage
    @GetMapping("list")
    public String list(Model model){
        Member loginMember = MemberUtil.getLoginMember(request);
        List<Financial> list = financialService.list(loginMember.getId());
        ResultModel resultModel = new ResultModel(0, PageUtil.getPage());
        resultModel.setData(list);
        model.addAttribute("model", resultModel);
        return INDEX_FTL_PATH + "list";
    }
}
