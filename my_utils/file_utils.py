import requests
from lxml import etree #数据预处理
for i in range(1,100):
   url = "https://movie.douban.com/top250?start={i}"
# url = "https://movie.douban.com/top250?start=25&filter="
   headers = {
   'User-Agent': 'zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
   result = requests.get(url=url,headers=headers)
   with open("豆瓣.text","a",encoding="utf-8") as f:
      f.write(result.text)
   html =etree.parse("豆瓣.text",etree.HTMLParser())
   r = html.xpath('//div[@class="hd"]/a/span[1]/text()')

   for k in r:
      print(f"电影网站：{k}")
   for k in r:
      with open("nihao.text","a",encoding="utf-8") as f:
         f.write(str(k))
         f.write("\n")
