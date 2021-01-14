import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent 
import re
import pandas as pd




def getHTMLText(url):
    ua = UserAgent()        # 实例化，需要联网但是网站不太稳定-可能耗时会长一些
    headers = {
        'User-Agent': ua.random    # 伪装
    }
    
    try:
        r = requests.get(url, headers=headers,timeout=300)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
 
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    singleUniv = []  #存放单个酒店的信息
    try:
        adress = soup.find(id='detail_pageHeader')  #酒店名称
        adress = adress.find('span')
   
        singleUniv.append(adress.string)
    except:
        singleUniv.append(" ")
    try:
        info = soup.find(id="js_hotelInfo_descAll")
        str1 = re.search('<p>(.*?)<br/></p>',str(info))
        singleUniv.append(str1.group(1))
    except:
        singleUniv.append(" ")

    other = soup.find_all(class_="inform-list bordertop facility clrfix")  
    for i in other:
        i = i.find_all('span')
        lis_service = []
        for lis in i:
            lis.find('span')
            
            try:
                result = re.search('</i>(.*?)</span>',str(lis))  
                if result.group(1) not in lis_service: 
                    lis_service.append(result.group(1))
            except:
                lis_service.append(" ")
        list2=[str(i) for i in lis_service] #使用列表推导式把列表中的单个元素全部转化为str类型
        list3=','.join(list2) #把列表中的元素放在空串中，元素间用逗号隔开
        singleUniv.append(list3)

    ulist.append(singleUniv)
def printUnivList(ulist,num):
   
    headers = ["名称","简介","网络设施","停车场","房间设施","酒店服务","酒店设施"]
    df = pd.DataFrame(ulist)
    df.to_csv('goWhere酒店.csv',encoding='utf-8-sig',index=False,header= headers)
    for i in range(num):
        u = ulist[i]
        print(u)
        
def main():
    df = pd.read_csv('去哪儿网酒店.csv')
    adress_list = df['网址'].values.tolist()
    uinfo = []
    for url in adress_list[0:50]:
        html = getHTMLText(url)
        fillUnivList(uinfo,html)
    printUnivList(uinfo,50)  
main()

