# DNS（Domain Name System） 服务

## DNS服务作用：
DNS是Domain Name System即域名服务，用于域名解析。常将域名解析为ip地址，称为正向解析；少量会将ip地址解析为域名，称为反向解析；

## DNS安装软件：
* bind     
提供主要程序及相关文件
* bind-chroot  
为bind提供一个伪装的根目录以增强安全性（将“/var/named/chroot/文件夹作为BIND的根目录”）不安装以/var/named为根目录
* bind-utils  
提供nslookup及dig等测试工具（默认桌面版已经安装）

## DNS服务：
服务进程名称：named
启动服务：/etc/init.d/named start 或 service named start

## DNS配置文件：
* /etc/hosts 
本地dns解析
* /etc/resolve.conf
解析DNS的服务器
* /etc/nsswitch.conf
更改hosts和dns优先级。更改 hosts   file   dns    先hosts后dns 
* /etc/named.conf
来自于/usr/share/doc/bind-9.8.2/sample/etc/named.conf  主配置文件
* /etc/named/etc/named.ca
包含了13台根域名服务器的地址
* /etc/named.rfc1912.zones
来自于/usr/share/doc/bind-9.8.2/sample/etc/named.rfc1912.zones 次要配置文件

## 域名服务器种类：
* 缓存域名服务器
* 注域名服务器
* 从域名服务器

## 服务端口号即协议：
 53 端口   tcp/udp

## 测试命令：
### windows里查看dns缓存
* ipconfig /displaydns  查看
* ipconfig /flushdns  刷新
### linux
* nscd
* yum install nscd
* service nscd restart
```
nscd -g
nscd -i
dnstop 查看dns流量查询的情况的软件
host
nslookup
dig
named-checkconf
```

## DNS解析过程：
www.baidu.com    
1.客户机先查询本地dns缓存   
2.查找本地配置文件/etc/hosts   
3.向本地dns服务器发送域名解析的请求，即/etc/rsolv.conf中指定的dns服务器   
4.本地dns查询缓存，如果有直接返回给客户机；如果没有再查询本地dns区域数据库文件里是否有记录，如果有返回给客户机；如果没有查询到就向跟域“.”查询   
5.根域告诉本地dns服务器找的com服务器   
6.本地dns服务器向.com的服务器查询,com服务器告诉本地dns baidu这个域的dns服务器ip   
7.本地dns服务器找到baidu.com域的dns服务器，查询到www这台主机的ip   
8.同时放到自己的缓存里   
9.告诉客户机www.baidu.com的域名对应的ip   
10.客户机将ip放到缓存里   

### 常见一级域名缩写：
>.com   ---->commercial     公司以及盈利性组织     
.net   ---->network   
.org   ---->organization   非盈利组织    
.edu   ---->education     以教育为主的组织   
.cn    --->china    属于中国一级域名   
.kr    ---->korea       
.tw    --->taiwan    台湾   
.hk    ---->hongkong  香港   
.mil   ---->military   

### DNS服务搭建：
* 第一步：配置yum源，安装以下软件包：
```
yum install bind bind-chroot bind-utils
```
* 第二步：
刷新named服务，/etc/named.conf配置文件会复制到/var/name/chroot/etc/下，
会产生一些key文件/var/name/chroot/etc  配置文件
