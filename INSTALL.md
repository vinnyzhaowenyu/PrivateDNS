# 安装指南

## CentOS7 系统安装
#### BIND9 安装
```
cp conf/aliyun.repo  /etc/yum.repos.d/
yum clean all && yum makecache
yum install bind bind-chroot bind-devel -y
```

#### Python3 安装
```
yum install  openssl openssl-devel libffi-devel gcc make sqlite sqlite-devel -y 
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar xf Python-3.7.0.tgz 
cd Python-3.7.0/ 
./configure --prefix=/usr/local/PrivateDNS/Python370
make
make install
```

#### Django2 安装
```
wget https://www.djangoproject.com/m/releases/2.1/Django-2.1.tar.gz
tar xf Django-2.1.tar.gz 
cd Django-2.1/
/usr/local/PrivateDNS/Python370/bin/python3 setup.py install
/usr/local/PrivateDNS/Python370/bin/pip3 install --upgrade pip
/usr/local/PrivateDNS/Python370/bin/pip3 install djangorestframework
```
## 初始化项目
```
django-admin startproject privateDNS
cd privateDNS/
python3.5 manage.py  startapp web
python3.5 manage.py  startapp api
```
后续的不需要在初始化了
```
cp -r /root/PrivateDNS/PrivateDNS  /usr/local/PrivateDNS/
```

## 运行
```
/usr/local/PrivateDNS/Python370/bin/python3  /usr/local/PrivateDNS/PrivateDNS/manage.py runserver 0.0.0.0:5055
```
