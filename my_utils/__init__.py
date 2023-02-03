
import requests #导入请求模块
from lxml import etree #数据预处理
from urllib import request #下载方法

#1.确定网址
#互联网上的标准资源的地址
url = 'https://v.huya.com/g/all?set_id=3'
headers = {
   'User-Agent': 'zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
result = requests.get(url=url,headers=headers)
with open("虎牙.text","w",encoding="utf-8") as f:
   f.write(result.text)
html =etree.parse("虎牙.text",etree.HTMLParser())
r = html.xpath('//ul[@class="vhy-video-list clearfix "]/li/@data-vid')
for k in r:
   m =print(k)


# result = requests.get(url=url, headers=headers).text
#
#
# #3.筛选数据  result (re xpath bs4 pyquery json)
# res = etree.HTML(result)
#
# data = res.xpath('//img[@class="pic"]')
# print(data)
#
# # # #data ==== list 列表
# #循环 重复事情
# for i in data:
#   NewName = i.xpath('./@alt')[0]
#   NewUrl = i.xpath('./@data-original')[0]
#   # print(NewName,NewUrl)
#
#   # 4.保存本地
#   request.urlretrieve(NewUrl,r'C:\Users\EDZ\Desktop\美女\\'+NewName+'.jpg')
#   print('下载完成!')




