#/bin/bash
source /etc/rc.d/init.d/functions


# 退出以及退出码
function EXITNUM(){
echo '##'
echo "#退出码： $1"
echo "#      $2"   
echo '##'
exit $1
}

# 访问控制
if [ ${USER} != 'root' ];then
  echo "You'r Cannot run the Script!"
  EXITNUM '10' 'User access control'
fi

# 可更改变量区域
TEMPLATEIMG=/vhost/images
TEMPLATEXML=/etc/libvirt/qemu
SUCCESS=`echo -e "\033[32mSUCCESS\033[0m"`
INVALID=`echo -e "\033[31mINVALID\033[0m"`


# 标志位以及变量区域
HIP=null
HNUM=0
HCPU=2
HMEM=4
STATCODE=0



# 返回区域
function result(){
        if [[ $1 == 'true'  ]];then
                echo "[${SUCCESS}]  $2"
  else
                echo "[${INVALID}]  $2"
        fi
}

function envCheck(){
        if [[ `systemctl status libvirtd | grep Active |awk '{print $3}'` == '(running)'  ]];then
                 result  'true' 'KVM environment check'
                echo '+---------------------------+'
                for hosts in `virsh list --all | awk '{print $2}' | egrep -v '^$|Name'`
                do
                  echo "| ▸  ${hosts}"
                done
                 return 101
  else
           result  'false'  'KVM environment check'
                 return 10
        fi
}

# 克隆功能函数区域
function getUserEnter(){
        hNAME="clone-`date +'%Y-%m-%d'`-100250"
        read -e -p 'Enter host name: ' HNAME
        ${HNAME}=${HNAME:=${hNAME}} &> /dev/null
        [[ ${HNAME} =~ ^[a-zA-Z] ]] || EXITNUM  20   'Get Host name Invalid!'
        for name in `virsh list --all | awk '{print $2}' | egrep -v '^$|Name'| xargs`
        do
        [[ ${HNAME} == ${name}  ]] &&  EXITNUM  20   "Host name ${HNAME}  ready exits."
        done
        read -e -p 'Enter host address: ' HIP
        hIP=192.168.100.250
        ${HIP}=${HIP:=${hIP}} &> /dev/null
        [[ ${HIP} =~ ^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$  ]] || EXITNUM  30   'Get Host address Invalid!' 
  `ping -c 1 -i 1 ${HIP}` > /dev/null
  [[ $? -eq 0 ]] &&  EXITNUM  30   "Get Host address ${HIP} Invalid!"
}

function cpHostTemp(){
  # Copy Images
        qemu-img create -f qcow2 -b ${TEMPLATEIMG}/template  ${TEMPLATEIMG}/${HNAME}  &> /dev/null
        [[ -e ${TEMPLATEIMG}/${HNAME}  ]] && result  'true'  'Host Images copy success.' || result  'false'  'Host Images copy invalid.'
        cp ${TEMPLATEXML}/template.xml ${TEMPLATEXML}/${HNAME}.xml
        [[ -e ${TEMPLATEXML}/${HNAME}.xml  ]] && result  'true'  'Host XML copy success.' || result  'false'  'Host XML copy invalid.'
        sed -i "s#<name>temp</name>#<name>${HNAME}</name>#g" ${TEMPLATEXML}/${HNAME}.xml
        sed -i "s#<source file='${TEMPLATEIMG}/temp'/>#<source file='${TEMPLATEIMG}/${HNAME}'/>#g" ${TEMPLATEXML}/${HNAME}.xml
        result  'true'  'Host configure file Success.'
}

function hostDefine(){
        # Define host
        $(virsh define ${TEMPLATEXML}/${HNAME}.xml)
        $(virsh start ${HNAME})
        [[ `virsh list --all | grep rancher-10020 | awk '{print $3}'` == 'running' ]] && result  'true'  'Host define Success.' || result  'false'  'Host define invalid.'
        echo "${HIP}  ${HNAME}" >> /etc/hosts
        echo ''
}

function cloneHost(){
  envCheck 
        getUserEnter
  result 'true' 'Get Host messsage'
  cpHostTemp
        result 'true' 'CP Host images and XML'
        hostDefine
}

# 删除函数区域
function  deleteHost(){
        echo '+---------------------------+'
  for hosts in `virsh list --all | awk '{print $2}' | egrep -v '^$|Name'`
  do
      echo "| ▸  ${hosts}"
  done
  read -e -p 'Enter need delete hosts: ' DELHOST
        #[[   ]]
         virsh undefine ${DELHOST} &> /dev/null
        `rm -rf /etc/libvirt/qemu/${DELHOST}.xml`
        `rm -rf /vhost/images/${DELHOST}`
        `sed -i '#${HNAME}#d' /etc/hosts`
}

# 展示虚机信息
function showHost(){
  echo '+---------------------------+'
  for hosts in `virsh list --all | awk '{print $2}' | egrep -v '^$|Name'`
  do
    echo "| ▸  ${hosts}"
  done
        read -e -p 'Enter show  hosts name: ' SHOWHOST
  echo "虚拟机内存："
        echo "虚拟机CPU： "


}


# 主函数区域
function main(){
   clear
         echo ' _        _______  _______  _       '
         echo '( \      (  ____ \(  ___  )( (    /|'
         echo '| (      | (    \/| (   ) ||  \  ( |'
         echo '| |      | (__    | |   | ||   \ | |'
         echo '| |      |  __)   | |   | || (\ \) |'
         echo '| |      | (      | |   | || | \   |'
         echo '| (____/\| (____/\| (___) || )  \  |'
         echo '(_______/(_______/(_______)|/    )_)'
        echo
        # 身份环境检查
        result 'true' 'Authentication.'
        # 选择操作
        while true
        do
                echo '+---------------------------+'
                echo '    1.  Clone host'
                echo '    2.  Change IpAddress'
                echo '    3.  Change Flovar'
                echo '    4.  Delete host'
                echo '    5.  Show  And test VirtHost'
                read -e -p 'Choise operating: ' CHOISE
                case ${CHOISE} in
                "1")
                cloneHost
                ;;
                "2")
                echo "待完善"
                ;;
                "3")
                echo "待完善"
                ;;
                "4")
                deleteHost
                ;;
                "5")
                showHost
                ;;
                *)
                exit 0
                ;;
                esac
        done
}

main