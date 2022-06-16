package com.lxinet.jeesns.service.system.impl;

import com.lxinet.jeesns.core.exception.ParamException;
import com.lxinet.jeesns.core.service.impl.BaseServiceImpl;
import com.lxinet.jeesns.dao.system.IConfigDao;
import com.lxinet.jeesns.model.system.Config;
import com.lxinet.jeesns.service.system.IConfigService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by zchuanzhao on 16/9/27.
 */
@Service("configService")
public class ConfigServiceImpl extends BaseServiceImpl<Config> implements IConfigService {
    @Resource
    private IConfigDao configDao;


    @Override
    public List<Config> allList() {
        return super.listAll();
    }

    @Override
    public Map<String, String> getConfigToMap() {
        List<Config> allList = this.allList();
        Map<String,String> map = new HashMap<>();
        for (Config config : allList) {
            map.put(config.getJkey(),config.getJvalue());
        }
        return map;
    }

    @Override
    public String getValue(String key) {
        Config config = configDao.selectByKey(key);
        if (config != null){
            return config.getJvalue();
        }
        return null;
    }

    @Override
    public boolean update(Map<String, String> params, HttpServletRequest request) {
        for(Map.Entry entry : params.entrySet()){
            if(((String)entry.getValue()).length() > 2000){
                throw new ParamException("只能输入2000个字符");
            }else {
                configDao.update((String)entry.getKey(),(String)entry.getValue());
                request.getServletContext().setAttribute(((String)entry.getKey()).toUpperCase(),entry.getValue());
            }
        }
        return true;
    }


}
