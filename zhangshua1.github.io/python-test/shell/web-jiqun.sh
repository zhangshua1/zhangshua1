#！/bin/bash
#
sed -i.bak 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
systemctl stop firewalld
systemctl disable firewalld
ad=`id www &>/dev/null`
if [ $? -ne 0 ];then
    echo "用户已存在"
else
    useradd www -u 1002
fi

cd /etc/yum.repos.d

touch nginx.repo    

echo "[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/\$releasever/\$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key" > /etc/yum.repos.d/nginx.repo

yum makecache
yum list | grep nginx

if [ $? -gt 0 ];then
    echo "yum源设置失败！"
else
    yum install -y nginx
fi
systemctl start nginx
systemctl enable nginx

cd /etc/nginx/conf.d
touch blog.conf
echo "server{
        listen  8081;
        server_name  blog.shuai.com;
        client_max_body_size 50m;
        location /{
         root /html/blog;
         index index.php index.html;
        }

        location ~ \.php$ {
         root /html/blog;
         fastcgi_index index.php;
         fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
         fastcgi_pass  127.0.0.1:9000;
         include fastcgi_params;
       }
}" > /etc/nginx/conf.d/blog.conf

mkdir -p /html/blog/
sed -i.bak 's/user  nginx;/user  www;/' /etc/nginx/nginx.conf
systemctl restart nginx


