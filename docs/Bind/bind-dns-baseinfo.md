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

### DNS配置文件：
/etc/hosts            本地dns解析
/etc/resolve.conf     解析DNS的服务器
/etc/nsswitch.conf    更改hosts和dns优先级。更改 hosts   file   dns    先hosts后dns 
/etc/named.conf       来自于/usr/share/doc/bind-9.8.2/sample/etc/named.conf  主配置文件
/etc/named/etc/named.ca   包含了13台根域名服务器的地址
/etc/named.rfc1912.zones  来自于/usr/share/doc/bind-9.8.2/sample/etc/named.rfc1912.zones 次要配置文件

### 域名服务器种类：
* 缓存域名服务器
*  注域名服务器
*  从域名服务器

### 服务端口号即协议：
 53 端口   tcp/udp

### 测试命令：
##### windows里查看dns缓存
* ipconfig /displaydns  查看
* ipconfig /flushdns  刷新
##### linux
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

### DNS解析过程：
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








 

 ===
ds缓存域名服务器
	1.安装好软件
	2.修改/etc/named.conf    
	3.刷新服务
	4.确保服务器能上网
===

```
options {
	listen-on port 53 { 10.0.2.189; };
//	listen-on-v6 port 53 { ::1; };
	directory 	"/var/named";
	dump-file 	"/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";
	allow-query     { any; };
#forwarders  {8.8.8.8;};   转发到指定的dns服务器
	recursion yes;
#	dnssec-enable yes;
#	dnssec-validation yes;
#	dnssec-lookaside auto;
	/* Path to ISC DLV key */
#	bindkeys-file "/etc/named.iscdlv.key";
#	managed-keys-directory "/var/named/dynamic";
};
logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};
zone "." IN {
	type hint;
	file "named.ca";
};
include "/etc/named.rfc1912.zones";
#include "/etc/named.root.key";

3.添加域名
[root@localhost named]# vim /etc/named.rfc1912.zones
zone "feng.com" IN {
        type master;
        file "feng.com.zone";
};
zone "2.0.10.in-addr.arpa" IN {
        type master;
        file "10.0.2.arpa";
};
```
====

 4.新建区域数据库文件
[root@localhost named]# cd /var/named/
[root@localhost named]# ls
chroot  dynamic   named.empty      named.loopback
data    named.ca  named.localhost  slaves
[root@localhost named]# cp named.localhost feng.com.zone -p
[root@localhost named]# cp named.localhost 10.0.2.arpa -p
===
主、从服务器之间复制区域数据库文件的时候的一些设置
                                        0       ; serial
当从域名服务器到主域名服务器来复制区域数据库文件的时候，看serial值是否比它的serial值大，如果大，就复制，如果相等就不复制
                                        1D      ; refresh
                                        1H      ; retry
                                        1W      ; expire
                                        3H )    ; minimum
===
SOA
A
NS
MX  ---》mail exchange  告诉邮件服务器的ip 创建邮件交换记录，5表示优先级，越小优先级越高   数据范围自己定义
CNAME
*
===
负载均衡
泛域名解析
===
[root@localhost named]# cat feng.com.zone 
$TTL 1D
@	IN SOA	@ root.feng.com. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
	NS	@
	A	10.0.2.100
www      A  10.0.2.253
ftp     A   10.0.2.253
lulu  A 10.0.2.25
@  MX  6   mail2.feng.com.
mail2   A  10.0.2.12
@  MX  5   mail.feng.com.
mail   A  10.0.2.11
luu   CNAME  lulu
$GENERATE 10-50  station$ A 10.0.2.$
*  A   10.0.2.253
video  A 10.0.2.253
video  A 10.0.2.250
video  A 10.0.2.230

[root@localhost named]# 
===
[root@localhost named]# cat 10.0.2.arpa 
$TTL 1D
@	IN SOA	@ root.feng.com. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
	NS	@
	A	10.0.2.100
253   PTR  www.feng.com.
25   PTR lulu.feng.com.
12  PTR mail2.feng.com.
11  PTR mail.feng.com.
253  PTR ftp.feng.com.
253  PTR video.feng.com.
$GENERATE 10-50  $ PTR station$.feng.com.
[root@localhost named]# 
===
[root@localhost etc]#  -t /var/named/chroot/
[root@localhost named]# named-checkzone feng.com feng.com.zone 
======
在/etc/named.conf
  forwarders {10.0.2.250;10.0.32.3;};
先查本机，再查转发器服务器，然后再查根域
===
条件转发器，符合dear.com的域名查询的时候，就去10.0.0.151查询
zone "dear.com" IN {
	type forward;
	forwarders {10.0.0.151;};
};
===
nslookup
	set  type=mx
	set  type=ns
	set  type=a
	set  type=PTR	
===
> server 10.0.0.151   临时修改dns服务器地址，不需要去修改/etc/resolv.conf文件
===
[root@localhost ~]# dig www.baidu.com @8.8.8.8
===
反向解释过程
 
===
从域名服务器
	1.安装软件
	2.修改配置
zone "feng.com" IN {
        type slave;
        file "slaves/feng.com.zone";
        masters {10.0.2.100;};
};
zone "2.0.10.in-addr.arpa" IN {
        type slave;
        file "slaves/10.0.2.arpa";
        masters {10.0.2.100;};
};
===

http://10.0.2.253/4ban-linux/system3
lftp 10.0.2.253/software
===
转发器
	forward first/only
	forwarders  {8.8.8.8;};
条件转发器
====
子域授权
view
TISG
===
dns 优先级最高的解析服务文件是/etc/hosts文件
dns domain name system  域名系统
dns的特点：分布式，层次式

redhat5 修改配置文件要进入到/var/named/chroot/中
redhat6 可以直接修改/etc/named.conf，然后会自动复制到/var/named/chroot中




更改hosts和dns优先级更改
/etc/nsswitch.conf
hosts   file   dns    先hosts后dns

反向域解析的文件文件
10.168.192.in-addr.arpa
反向解析192.168.10网段

named.conf
options 是全局配置
listen-on port 53  默认时any
directory “/var/named”;
dump-file "/var/named/data/cache_dump.db" 缓存文件
recursion yes; 是否进行互联网解析
statistics  统计
memstatistics  统计内存消耗时段
 
zone "." IN {
type hint ;
file “named.ca”  国际13台dns顶级服务器的地址在named.ca中
}
=============
最简单的dns服务器配置文件
options {
directory  "/var/named"
}

=====================
options {                                        全局配置
        listen-on port 53 { 127.0.0.1; };监听的端口，删除时监听所有的端口
        listen-on-v6 port 53 { ::1; };ipv6，的监听
        directory       "/var/named";住配置文件，这个必须有，而且必须是这个位置，不能修改
        dump-file       "/var/named/data/cache_dump.db";缓存文件存放的地方，默认没有。要是用rpch dumpdb同步内存
        statistics-file "/var/named/data/named_stats.txt";       统计dns
        memstatistics-file "/var/named/data/named_mem_stats.txt";统计dns服务消耗的内存及时间段
        allow-query     { localhost; };      可以删除
        recursion yes;  是否解析互联网dns，默认是yes

        dnssec-enable yes;可以删除
        dnssec-validation yes;可以删除
        dnssec-lookaside auto;可以删除

        /* Path to ISC DLV key */
        bindkeys-file "/etc/named.iscdlv.key";

        managed-keys-directory "/var/named/dynamic";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

zone "." IN {
        type hint;       
        file "named.ca";
};

include "/etc/named.rfc1912.zones";    把文件包含进来，
include "/etc/named.root.key";

~                  



------
/etc/resolved.conf
search  com.cn  在ping时会自动在ping的域名后面加上com.cn，如果错误将都无法ping通
nameserver   222.245.129.80   dns服务器，如8.8.8.8

/etc/named.conf
options 是全局配置
listen-on port 53  默认时any
directory “/var/named”;
dump-file "/var/named/data/cache_dump.db" 缓存文件
recursion yes; 是否进行互联网解析

statistics  统计

memstatistics  统计内存消耗时段


zone "." IN {
type hint ;
file “named.ca”  国际13台dns顶级服务器的地址在named.ca中
}
=============
最简单的dns服务器配置文件
options {
directory  "/var/named"
}

=====================
options {                                        全局配置
        listen-on port 53 { 127.0.0.1; };监听的端口，删除时监听所有的端口
        listen-on-v6 port 53 { ::1; };ipv6，的监听
        directory       "/var/named";住配置文件，这个必须有，而且必须是这个位置，不能修改
        dump-file       "/var/named/data/cache_dump.db";缓存文件存放的地方，默认没有。要是用rpch dumpdb同步内存
        statistics-file "/var/named/data/named_stats.txt";       统计dns
        memstatistics-file "/var/named/data/named_mem_stats.txt";统计dns服务消耗的内存及时间段
        allow-query     { localhost; };      可以删除
        recursion yes;  是否解析互联网dns，默认是yes

        dnssec-enable yes;可以删除
        dnssec-validation yes;可以删除
        dnssec-lookaside auto;可以删除

        /* Path to ISC DLV key */
        bindkeys-file "/etc/named.iscdlv.key";

        managed-keys-directory "/var/named/dynamic";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

zone "." IN {
        type hint;      
        file "named.ca";
};

include "/etc/named.rfc1912.zones";    把文件包含进来，
include "/etc/named.root.key";
