# HentaiSaver
一个用于下载nhentai及nyahentai的小工具
首发于xuexia15.org

本程序使用python编程
使用aria2c实现多并发下载
支持nyahentai等使用相同模板的网站


更新记录：

2021.3.211.4.2版本更新：
修复闪退bug（其实是我设计时的逻辑有点问题导致的）
添加系列 批量下载支持
任务会被暂时放到任务列表里（不会直接进行下载）
可以直接粘贴网址进行解析


2021.2.20
发布1.4 beta
添加按作者、作品、tag、团体批量下载功能


2021.2.18
发布第一版 代号1.3 alpha



使用说明：

1.从源码创建可使用的程序
2.直接下载已编译的完整程序包 https://github.com/o5-null/HentaiSaver/releases/tag/begining或https://wwa.lanzous.com/b00ob6xid 
密码:g910





注意！

本程序依赖于python扩展库 requests

请自行安装

使用源码步骤：

1.下载所有文件至本地
2.在源码同路径下创建site.ini文件
3.在文件中写入网址 https://zha.nyabus.com/ https://zhb.nyabus.com/ 或到https://trello.com/c/HzN241dq/ 获取



使用说明：
填写本子ID
举个例子
本子网址是https://zha.nyabus.com/g/348173/
那个348173就是ID
下载时填写该数字即可
按回车开始下载
下载完成后本子将保存到软件根目录

批量下载功能使用   
团体：
举例 https://zha.nyabus.com/group/nigami-whip-milk/
我们只需要nigami-whip-milk这一部分
前面加上gr表示是团体
即grnigami-whip-milk
回车进行解析

作者：
举例 https://zha.nyabus.com/artist/michiking/
只需要michiking这一部分
前面加上ar表示是作者
即armichiking
回车进行解析

角色：
举例 https://zha.nyabus.com/character/teitoku/
只需要teitoku这一部分
加上ch表示是作者

tag：
举例 https://zha.nyabus.com/tag/big-breasts/
只需要big-breasts这一部分
加上ta表示是作者

注意！！
在标示（即ch、ar等）后加上ja表示下载所有作品
默认仅下载中文翻译
