# docker安装

常规安装方式：

`**export REGISTRY_MIRROR=https://registry.cn-hangzhou.aliyuncs.com`**

**`yum install -y yum-utils device-mapper-persistent-data lvm2`**

**`yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo`**

**`yum install -y docker-ce`**

**`systemctl enable docker.service`**
**`systemctl start docker.service`**
**`docker version**`

# docker常用命令

**镜像相关**

1、拉取镜像：docker pull

2、查看镜像：docker images

3、删除镜像：docker rmi

常用参数：-f:强制删除运行中的容器

4、（1）创建镜像：docker build

常用参数：-t name/container:tag 指定镜像命名空间为name仓库为container,tag为版本号

（2）对源镜像更改后重新建立新镜像

docker commit

常用参数：-m:本次提交信息；-a/--author="":作者

**容器相关**

1、运行容器：docker run

常用参数：

1.--name:为容器指定名称

2.--it:启动一个交互型容器，此参数为我们和容器提供了一个交互shell

3.-d:创建后台型容器

4.-restart=always:容器退出后自动重启

5.-restart=on-failure:\x:容器退出时如果返回值是非0，就会尝试重启x次

6.-p x:y :主机端口：容器端口

7.-P：随机分配一个49000到49900的端口

8.-v：创建数据卷:宿主机路径:容器路径

9.-h : 指定容器的hostname

10.-n :指定dns

11.-e ：设置环境变量

12.-m :设置容器使用内存最大值

13.--net: 指定容器的网络连接类型，支持 bridge/host/none/container

14. --expose=x: 开放端口x

2、查看正在运行的容器：docker ps

常用参数：

1.-a:查看所有容器

2.-l:只列出最近创建的

3.-n=x:只列出最后创建的x个

4.-q:只列出容器ID

3、停止容器：docker stop \docker kill

4、删除容器：docker rm

常用参数：-f:强制删除运行中的容器

docker rm `docker ps -aq`：删除所有容器

5、查看容器日志：docker logs

6、查看容器进程：docker top

7、查看容器信息：docker inspect

8、进入容器：

（1）进入交互式容器：docker attch

（2）进入后台型容器：docker exec

常用参数：-it 容器ID /bin/bash

**Dockerfile:**

FROM------------------基础镜像，当前新镜像是基于哪个镜像的

MAINTAINER---------镜像维护者的姓名或邮箱地址

RUN---------------------容器构建时需要运行的命令

EXPOSE---------------当前容器对外暴露出的端口

WORKDIR-------------工作目录，容器创建后登陆的默认路径

ENV---------------------设置环境变量

ADD--------------------将宿主机目录下的文件拷贝进镜像且自动处理url和解压tar包

COPY------------------类似ADD，拷贝文件到目录镜像中

VOLUME-------------容器数据卷，用于数据保存和持久化工作

CMD------------------1、指定一个容器启动时要运行的命令
                              2、Dockerfile中可以有多个CMD指令，但只有最后一个生效，CMD命令会被docker run之后的参数替换

ENTRYPOINT------1、指定一个容器启动时要运行的指令

​                               2、ENTRYPOINT和CMD一样，都是在指定容器启动程序及参数

ONBUILD------------当构建一个被继承的Dockerfile时运行命令，父镜像在被子继承后，父镜像的onbuild被触发