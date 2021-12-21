import requests
import csv

headers = {
    "cookie": "buvid3=C42372E3-5296-436C-9A48-AD0B1174AAD1143080infoc; rpdid=|(umYu~lkY~|0J'uY|RllumkR; blackside_state=1; LIVE_BUVID=AUTO6816140032823539; buvid_fp=C42372E3-5296-436C-9A48-AD0B1174AAD1143080infoc; PVID=1; _uuid=B7D419F7-8117-A6DE-BB60-D67A5E75BB0687737infoc; CURRENT_QUALITY=112; video_page_version=v_old_home; bp_t_offset_3060464=603016054063221000; CURRENT_BLACKGAP=0; i-wanna-go-back=-1; b_ut=5; bp_video_offset_3060464=605978636599981600; CURRENT_FNVAL=2000; innersign=1; b_lsid=D6D32BAA_17DD533E447; fingerprint=4360f18db3171f455bdca2e16bc8980e; buvid_fp_plain=C42372E3-5296-436C-9A48-AD0B1174AAD1143080infoc; SESSDATA=ee9ac6fc%2C1655512692%2Ca6bb0%2Ac1; bili_jct=2fa4fd9f0e3917a230366a3bf6370690; DedeUserID=3060464; DedeUserID__ckMd5=799f4900486a903b; sid=6qlfcrjr"
}

page = None

while page is None: 
    try: 
        page = int(input('请输入想要读取评论的页数: '))

    except ValueError:
        print('输入有误，请重新输入QAQ')
        continue



i = 1
f = open('myComment1.csv','w',newline='', encoding = 'utf-8-sig') # Open the file
writer = csv.writer(f)
writer.writerows([['Comment','User_name','Time','Video']])  #Write title of csv file
while i <= page:
    req = requests.get(url = 'https://member.bilibili.com/x/web/replies?order=ctime&filter=-1&is_hidden=0&type=1&comment_display=0&bvid=&pn=' + str(i) + '&ps=10', headers = headers)
    #Create request of every url
    resp = req.json()['data'] #Find list data in req
    for x in resp:
        dic = []
        dic.append(str(x.get('message')))
        dic.append(str(x.get('replier')))
        dic.append(str(x.get('ctime')))
        dic.append(str(x.get('title')))
        writer.writerows([dic])  #Find elements and write into csv file
            
    print('Page ' + str(i) + ' download success!')
    i += 1

f.close()
print('All success!')
