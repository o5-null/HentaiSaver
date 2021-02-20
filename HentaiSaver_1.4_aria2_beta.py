import os
import re
import time

import requests


#初始化变量
localna = os.getcwd()
global hostnull
if os.path.exists(localna+'\\site.ini'):
    with open(localna+'\\site.ini','r',encoding='GBK') as f:
        hostnull = f.read()
elif not os.path.exists(localna+'\\site.ini'):
    hostnull = 'https://zha.nyabus.com/'
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
    return ('\n'+title+'下载已完成,按任意键开始新任务')

def save(url,url_dir):
    os.chdir(url_dir)
    os.system(ar+url)
    os.chdir(localna)


#
#
#ID提取
def hentai_ar_all(id,type,language='ch',host1=hostnull):
    global a_list
    print(id+'作品提取中。。。')
    if language == 'ch':
        a_date = requests.get(host1+type+'/'+id+'/chinese',headers=headers).content.decode()
    elif language == 'ja':
        a_date = requests.get(host1+type+'/'+id,headers=headers).content.decode()
    a_list = re.findall('<a href="/g/(.*?)/" c',a_date)
    #提取页数
    a_num = re.findall('</span> <span class="count">(.*?)</span>',a_date)
    num = 0
    a_page = 1
    a_num = a_num[0][1:-1]
    print('作品ID提取完毕，共有'+str(a_num)+'本')
    while 1==1:
        num = 25+num
        a_page = 1+a_page
        if num >= int(a_num):
            break
    print('作品共有'+str(a_page)+'页')
    for a in range(2,a_page):
        a_shenxia = a_page-a
        print('第'+str(a)+'页提取中，还有'+str(a_shenxia)+'页')
        if language == 'ch':
            a_date = requests.get(host1+type+'/'+id+'/chinese'+'/page/'+str(a),headers=headers).content.decode()
        elif language == 'ja':
            a_date = requests.get(host1+type+'/'+id+'/page/'+str(a),headers=headers).content.decode()
        a_list_nu = re.findall('<a href="/g/(.*?)/" c',a_date)
        print('第'+str(a)+'页提取完毕，还有'+str(a_shenxia)+'页')
        #追加列表
        a_list = a_list+a_list_nu
    print("提取完毕，共有"+str(len(a_list))+'页')
    os.system('cls')
    for a in a_list:
        input(hentaisaver(a))
    return (a_list)

def id_get(a):
    if a[0:2] == 'ar':
        if a[2:4] == 'ja':
            list = hentai_ar_all(a[4:],'artist','ja',hostnull)
        a = a[2:]
        list = hentai_ar_all(a,'artist','ch',hostnull)
    elif a[0:2] == 'gr':
        if a[2:4] == 'ja':
            list = hentai_ar_all(a[4:],'group','ja',hostnull)
        a = a[2:]
        list = hentai_ar_all(a,'group','ch',hostnull)
    elif a[0:2] == 'ch':
        if a[2:4] == 'ja':
            list = hentai_ar_all(a[4:],'character','ja',hostnull)
        a = a[2:]
        list = hentai_ar_all(a,'character','ch',hostnull)
    elif a[0:2] == 'ta':
        if a[2:4] == 'ja':
            list = hentai_ar_all(a[4:],'tag','ja',hostnull)
        a = a[2:]
        list = hentai_ar_all(a,'tag','ch',hostnull)
    return list
        


os.system('title HentaiSaver 1.4 BETA')
os.system('color 02')
while 1==1:
    os.system('color 02')
    print('MADE IN xuexia\nmaker 千反田爱瑠\n用于在线本子网站本子下载\n支持nhentai,nyahentai等使用相同模板的网站\n下载使用aria2c实现多并发下载\n可读取文本文件中的ID实现批量下载\npower by python\n1.4公开测试版\n最新版本请至xuexia15.cc获取\n')
    a = input('请输入所需要解析的文件、画师、团体、tag、本子ID：')
    id_get(a)
    try:
        if not os.path.isfile(a) and a < 0 and a > 999999:
            os.system('color 04')
            input('输入不正确，请重试')
            os.system('cls')
            continue
    except TypeError as e:
        os.system('color 04')
        input('输入不正确，请重试')
        os.system('cls')
        continue
    if os.path.isfile(a):
        with open(a,'r',encoding='GBK') as f:
            list = f.readlines()
        for idlist in list:
            hentaisaver(str(idlist).replace("\n",""))
    else:
        input(hentaisaver(a))
    os.system('cls')