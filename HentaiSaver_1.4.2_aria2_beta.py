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
    hostnull = 'https://zhb.nyabus.com/'
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
    time.sleep(1)
    return a_list

def id_get(a):
    if a[0:2] == 'ar':
        if a[2:4] == 'ja':
            list = hentai_ar_all(a[4:],'artist','ja',hostnull)
            return list
        a = a[2:]
        list = hentai_ar_all(a,'artist','ch',hostnull)
        return list
    
    elif a[0:2] == 'gr':
        if a[2:4] == 'ja':
            list = hentai_ar_all(a[4:],'group','ja',hostnull)
            return list
        a = a[2:]
        list = hentai_ar_all(a,'group','ch',hostnull)
        return list
    
    elif a[0:2] == 'ch':
        if a[2:4] == 'ja':
            list = hentai_ar_all(a[4:],'character','ja',hostnull)
            return list
        a = a[2:]
        list = hentai_ar_all(a,'character','ch',hostnull)
        return list
    
    elif a[0:2] == 'ta':
        if a[2:4] == 'ja':
            list = hentai_ar_all(a[4:],'tag','ja',hostnull)
            return list
        a = a[2:]
        list = hentai_ar_all(a,'tag','ch',hostnull)
        return list
    
    elif a[0:2] == 'pa':
        if a[2:4] == 'ja':
            list = hentai_ar_all(a[4:],'parody','ja',hostnull)
            return list
        a = a[2:]
        list = hentai_ar_all(a,'parody','ch',hostnull)
        return list
    return 0
    
def clean(a):
    if "http" in a:
        if "/g/" in a:
            a = re.findall('/g/(.*?)/',a)
            a = a[0]

        elif "/group/" in a:
            a = re.findall('/group/(.*?)/',a)
            a = "grja"+a[0]
        elif "/group/" in a and "/chinese" in a :
            a = re.findall('/group/(.*?)/chinese',a)
            a = "gr"+a[0]

        elif "/artist/" in a:
            a = re.findall('/artist/(.*?)/',a)
            a = "arja"+a[0]
        elif "/artist/" in a and "/chinese" in a :
            a = re.findall('/artist/(.*?)/chinese',a)
            a = "ar"+a[0]

        elif "/character/" in a:
            a = re.findall('/character/(.*?)/',a)
            a = "chja"+a[0]
        elif "/character/" in a and "/chinese" in a :
            a = re.findall('/character/(.*?)/chinese',a)
            a = "ch"+a[0]

        elif "/tag/" in a:
            a = re.findall('/tag/(.*?)/',a)
            a = "taja"+a[0]
        elif "/tag/" in a and "/chinese" in a :
            a = re.findall('/tag/(.*?)/chinese',a)
            a = "ta"+a[0]
        
        elif "/parody/" in a:
            a = re.findall('/parody/(.*?)/',a)
            a = "paja"+a[0]
        elif "/parody/" in a and "/chinese" in a :
            a = re.findall('/parody/(.*?)/chinese',a)
            a = "pa"+a[0]
    return a


os.system('title HentaiSaver 1.4.2 BETA')
os.system('color 02')
work_list = []
while 1==1:
    try:
        os.system('cls')
        os.system('color 02')
        print('MADE IN xuexia\nmaker 千反田爱瑠\n用于在线本子网站本子下载\n支持nhentai,nyahentai等使用相同模板的网站\n下载使用aria2c实现多并发下载\n可读取文本文件中的ID实现批量下载\npower by python\n1.4.2修复版\n最新版本请至xuexia15.org获取\n')
        print("目前列表中有"+str(len(work_list))+"个任务\n")
        a = input('请输入所需要解析的文件、画师、团体、tag、本子ID[输入y开始下载列表任务]：')
        #文本读取
        if os.path.isfile(a):
            with open(a,'r',encoding='GBK') as f:
                read_list = f.readlines()
            for a in read_list:
                a = str(a)
                a = clean(a)
                #批量提取
                list = id_get(a)
                if not list == 0:
                    print("已添加"+str(len(list))+"个任务")
                    work_list = work_list + list
                    continue
                
                #id
                if not os.path.isfile(a) and int(a) > 0 and int(a) < 999999:
                    work_list.append(a)
                    print("目前列表中有"+str(len(work_list))+"个任务")
                    continue
        a = clean(a)
        
        if a == "y" and len(work_list) > 0:
            os.system("cls")
            print("列表任务开始解析。。。")
            for work in work_list:
                os.system("cls")
                time.sleep(1)
                hentaisaver(work)
                work_list.remove(work)
                print("目前列表中有"+str(len(work_list))+"个任务")
            os.system("cls")
            input("所有任务下载完成，按任意键继续")
            continue
        
        #批量提取
        list = id_get(a)
        if not list == 0:
            print("已添加"+str(len(list))+"个任务")
            work_list = work_list + list
            continue
        
        try: 
            if not os.path.isfile(a) and int(a) < 0 and int(a) > 999999:
                os.system('color 04')
                input('输入不正确，请重试')
                os.system('cls')
                continue
        except TypeError as e:
            os.system('color 04')
            input('输入不正确，请重试')
            os.system('cls')
            continue
        
        #id
        if not os.path.isfile(a) and int(a) > 0 and int(a) < 999999:
            work_list.append(a)
            print("任务加入成功")
            time.sleep(1)
            continue
        os.system('cls')
    except:
        continue