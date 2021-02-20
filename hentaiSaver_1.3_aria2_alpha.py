import os
import re
import time

import requests
#初始化变量
"""
MADE IN xuexia
maker 千反田爱瑠
用于在线本子网站本子下载
支持nhentai,nyahentai等使用相同模板的网站
下载使用aria2c实现多并发下载
可读取文本文件中的ID实现批量下载
power by python

1.3内部测试版
"""


localna = os.getcwd()
if os.path.exists(localna+'\\downdir.ini'):
    with open(localna+'\\downdir.ini','r',encoding='GBK') as f:
        localna = f.read()
elif not os.path.exists(localna+'\\downdir.ini'):
    localna = os.getcwd()

if os.path.exists(localna+'\\site.ini'):
    with open(localna+'\\site.ini','r',encoding='GBK') as f:
        hostnull = f.read()
elif not os.path.exists(localna+'\\site.ini'):
    hostnull = 'https://zha.nyabus.com'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'}
ar = localna+'\\aria2-1.35.0-win-64bit-build1\\aria2c.exe -i '

def hentaisaver(id,a=localna,host1=hostnull,dir=os.pardir):
    global local
    local = a
    titledate = id
    print(titledate+'正在解析')
    htmlba = requests.get(host1+'g/'+titledate+'/list2/',headers=headers).content.decode()
    titlehtml = requests.get(host1+'g/'+titledate,headers=headers).content.decode()
    print(titledate+'解析完成')
    #获取基本数据
    global title
    titleset = ">(.*?) &raquo;"
    title = re.findall(titleset,titlehtml)
    title = str(title[0])
    titlehtml = 0
    #提取标题
    os.makedirs(title,exist_ok=True)
    print(title+'正在下载中——')
    images = re.findall('data-src=\"(.*?)\"' ,htmlba)
    if not os.path.exists(localna+'\\'+id+'.aria'):
        with open(localna+'\\'+id+'.aria','w',encoding='GBK') as f:
            for a in images:
                f.write(a+'\n')
    save(localna+'\\'+id+'.aria',localna+'\\'+title)
    os.rename(localna+'\\'+id+'.aria',localna+'\\'+id+'.log')
    return(title+'下载已完成')

def save(url,url_dir):
    os.chdir(url_dir)
    os.system(ar+url)
    os.chdir(localna)



#lists = [236355,311611,322105,342866,342842,343596,339157,343287,254563,298908,342650,342169,252606,344463,344526,344527,344723,344818,344681]

while 1==1:
    a = input('请输入所需要解析的文件或ID：')
    if os.path.isfile(a):
        with open(a,'r',encoding='GBK') as f:
            list = f.readlines()
        for idlist in list:
            hentaisaver(str(idlist).replace("\n",""))
    else:
        print(hentaisaver(a))
