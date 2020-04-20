import requests
from lxml import etree
import xlwt

#获取html页面
url = 'https://www.bilibili.com/ranking/rookie/0/0/3'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.text


#解析页面，提取目标信息
data = []
tree = etree.HTML(html)
lis = tree.xpath('//ul/li[@class="rank-item"]//div[@class="info"]')
for li in lis:
    info = []
    #提取视频名
    name = li.xpath('./a/text()')[0]
    info.append(name)
    #提取链接
    link = li.xpath('./a/@href')[0]
    info.append(link)
    #提取播放量
    play_num = li.xpath('./div[1]/span[1]/text()')[0]
    info.append(play_num)
    #提取弹幕数
    discuss = li.xpath('./div[1]/span[2]/text()')[0]
    info.append(discuss)
    #提取up主
    up = li.xpath('.//a[@target="_blank"]/span/text()')[0]
    info.append(up)
    #汇总到data列表中
    data.append(info)

#保存数据
wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('sheet1')
#写表头
col_name = ('视频名','视频链接','播放量','弹幕量','up主')
for i in range(5):
    ws.write(0,i,col_name[i])
for r in range(len(data)):
    case = data[r]
    for c in range(5):
        ws.write(r+1,c,case[c])
wb.save('新人排行.xls')




