# PrivateDNS系统规划设计

PrivateDNS预计打造一套开源的、便于管理的、基于RESTFul API的、支持多种DNS软件的系统。它能够通过Web、API、Client等方式进行管理DNS。

该系统设计分多层：

- 应用客户端层：最上层与用户交互的界面。默认提供Web界面。

- API层：将底层的实现统一封装成标准的API向外提供服务支持。默认支持REST标准。

- DNS层：实际提供功能的基础。默认使用Bind9。

## 应用客户端层
前期计划基于Python3+Django2提供Web端UI设计。

## API层
有Django2提供标准的REST API接口

## DNS层
使用BIND9提供DNS功能。


