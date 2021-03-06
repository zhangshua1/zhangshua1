package io.mycat.config.loader.zkprocess.zktoxml.listen;

import com.google.common.io.Files;
import io.mycat.MycatServer;
import io.mycat.config.loader.console.ZookeeperPath;
import io.mycat.config.loader.zkprocess.console.ParseParamEnum;
import io.mycat.config.loader.zkprocess.entity.Property;
import io.mycat.config.loader.zkprocess.entity.Rules;
import io.mycat.config.loader.zkprocess.entity.rule.function.Function;
import io.mycat.config.loader.zkprocess.entity.rule.tablerule.TableRule;
import io.mycat.config.loader.zkprocess.parse.ParseJsonServiceInf;
import io.mycat.config.loader.zkprocess.parse.ParseXmlServiceInf;
import io.mycat.config.loader.zkprocess.parse.XmlProcessBase;
import io.mycat.config.loader.zkprocess.parse.entryparse.rule.json.FunctionJsonParse;
import io.mycat.config.loader.zkprocess.parse.entryparse.rule.json.TableRuleJsonParse;
import io.mycat.config.loader.zkprocess.parse.entryparse.rule.xml.RuleParseXmlImpl;
import io.mycat.config.loader.zkprocess.zookeeper.DataInf;
import io.mycat.config.loader.zkprocess.zookeeper.DiretoryInf;
import io.mycat.config.loader.zkprocess.zookeeper.process.ZkDataImpl;
import io.mycat.config.model.SchemaConfig;
import io.mycat.config.model.SystemConfig;
import io.mycat.config.model.TableConfig;
import io.mycat.config.model.rule.RuleConfig;
import io.mycat.manager.response.ReloadConfig;
import io.mycat.route.function.AbstractPartitionAlgorithm;
import io.mycat.route.function.ReloadFunction;
import io.mycat.util.ZKUtils;
import org.apache.curator.framework.CuratorFramework;
import org.apache.curator.framework.recipes.cache.ChildData;
import org.apache.curator.framework.recipes.cache.PathChildrenCacheEvent;
import org.apache.curator.framework.recipes.cache.PathChildrenCacheListener;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.xml.bind.JAXBException;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import static com.google.common.base.Preconditions.checkNotNull;

/**
 * Created by magicdoom on 2016/10/27.
 */
public class RuleFunctionCacheListener implements PathChildrenCacheListener {
    private static final Logger LOGGER = LoggerFactory.getLogger(RuleFunctionCacheListener.class);
    @Override public void childEvent(CuratorFramework client, PathChildrenCacheEvent event) throws Exception {
        ChildData data = event.getData();
        switch (event.getType()) {

            case CHILD_ADDED:
                addOrUpdate();
                break;
            case CHILD_UPDATED:
                addOrUpdate();
                break;
            default:
                break;
        }
    }

    public RuleFunctionCacheListener() {
        XmlProcessBase xmlProcessBase = new XmlProcessBase();

        parseRulesXMl = new RuleParseXmlImpl(xmlProcessBase) ;
        try {
            xmlProcessBase.initJaxbClass();
        } catch (JAXBException e) {
            LOGGER.error("error",e);
        }
    }

    private void addOrUpdate()
  {
      Rules Rules = null;
      try {
          Rules = this.zktoRulesBean();
      } catch (Exception e) {
          LOGGER.error("error",e);
      }

      LOGGER.info("RuleszkToxmlLoader notiflyProcess zk to object  zk Rules Object  :" + Rules);

      // ???mapfile????????????????????? ???
      writeMapFileAddFunction(Rules.getFunction());

      LOGGER.info("RuleszkToxmlLoader notiflyProcess write mapFile is success ");

      // ???????????????????????????
      String path = RuleszkToxmlLoader.class.getClassLoader().getResource(ZookeeperPath.ZK_LOCAL_WRITE_PATH.getKey())
              .getPath();
      path = new File(path).getPath() + File.separator;
      path = path + WRITEPATH;

      LOGGER.info("RuleszkToxmlLoader notiflyProcess zk to object writePath :" + path);

      this.parseRulesXMl.parseToXmlWrite(Rules, path, "rule");

      LOGGER.info("RuleszkToxmlLoader notiflyProcess zk to object zk Rules      write :" + path + " is success");

      if (MycatServer.getInstance().getProcessors() != null)
          ReloadConfig.reload();

  }


    private static final String WRITEPATH = "rule.xml";

    /**
     * Rules???xml???????????????
     * @???????????? parseRulesXMl
     */
    private ParseXmlServiceInf<Rules> parseRulesXMl;;

    /**
     * ??????????????????
     * @???????????? parseJsonService
     */
    private ParseJsonServiceInf<List<TableRule>> parseJsonTableRuleService = new TableRuleJsonParse();

    /**
     * ????????????????????????
     * @???????????? parseJsonFunctionService
     */
    private ParseJsonServiceInf<List<Function>> parseJsonFunctionService = new FunctionJsonParse();


    private Rules zktoRulesBean() throws Exception {
        Rules Rules = new Rules();

        // tablerule??????
     String value=  new String( ZKUtils.getConnection().getData().forPath(ZKUtils.getZKBasePath()+"rules/tableRule"),"UTF-8") ;
        DataInf RulesZkData = new ZkDataImpl("tableRule",value);
        List<TableRule> tableRuleData = parseJsonTableRuleService.parseJsonToBean(RulesZkData.getDataValue());
        Rules.setTableRule(tableRuleData);



        // ??????function??????
        String fucValue=  new String( ZKUtils.getConnection().getData().forPath(ZKUtils.getZKBasePath()+"rules/function"),"UTF-8") ;
        DataInf functionZkData =new ZkDataImpl("function",fucValue) ;
        List<Function> functionList = parseJsonFunctionService.parseJsonToBean(functionZkData.getDataValue());
        Rules.setFunction(functionList);



        return Rules;
    }


    /**
     *  ?????????????????????????????????
     * ????????????
     * @param functionList
     * @???????????? 2016???9???18???
     */
    private void writeMapFileAddFunction(List<Function> functionList) {

        List<Property> tempData = new ArrayList<>();

        List<Property> writeData = new ArrayList<>();

        for (Function function : functionList) {
            List<Property> proList = function.getProperty();
            if (null != proList && !proList.isEmpty()) {
                // ??????????????????
                for (Property property : proList) {
                    // ?????????mapfile?????????????????????????????????????????????json???
                    if (ParseParamEnum.ZK_PATH_RULE_MAPFILE_NAME.getKey().equals(property.getName())) {
                        tempData.add(property);
                    }
                }

                // ??????mapfile???????????????????????????????????????
                if (!tempData.isEmpty()) {
                    for (Property property : tempData) {
                        for (Property prozkdownload : proList) {
                            // ??????mapfile???????????????????????????
                            if (property.getValue().equals(prozkdownload.getName())) {
                                writeData.add(prozkdownload);
                            }
                        }
                    }
                }

                // ??????????????????????????????????????????
                if (!writeData.isEmpty()) {
                    for (Property writeMsg : writeData) {
                        this.writeMapFile(writeMsg.getName(), writeMsg.getValue());
                    }
                }

                // ???????????????????????????
                proList.removeAll(writeData);

                // ????????????????????????????????????
                tempData.clear();
                writeData.clear();
            }
        }

    }

    /**
     * ?????? mapFile???????????????
     * ????????????
     * @param name ????????????
     * @return
     * @???????????? 2016???9???18???
     */
    private void writeMapFile(String name, String value) {

        // ????????????
        String path = RuleszkToxmlLoader.class.getClassLoader().getResource(ZookeeperPath.ZK_LOCAL_WRITE_PATH.getKey())
                .getPath();

        checkNotNull(path, "write Map file curr Path :" + path + " is null! must is not null");
        path = new File(path).getPath() + File.separator;
        path += name;

        // ??????????????????
        try {
            Files.write(value.getBytes(), new File(path));
        } catch (IOException e1) {
            e1.printStackTrace();
        }

    }

}
