
"""
1.确定网址
2.搭建关系  发送请求 接受响应
3.筛选数据
4.保存本地

"""
#                折线图生成
# # 导包，导入Line功能构建折现对象
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# # 得到折线图对象
# line=Line()
# # 添加x轴数据
# line.add_xaxis(["中国","美国","日本"])
# # 添加y轴数据
# line.add_yaxis("GDP",[30,20,10])
# # 设置全局配置set_global_opts来设置
# line.set_global_opts(
#     # 设置标题 控制位置
#     title_opts=TitleOpts("GDP展示",pos_left="center",pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show = True),
# )
# # 生成图表
# line.render()
# 基础地图演示

# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
# # 主备地图对象
# map = Map()
# # 主备数据
# data=[
#       ("北京",99),
#       ("上海",100),
#       ("湖南",299),
#       ("台湾",199),
#       ("安徽",299),
#       ("广州",399),
#       ("湖北",599)
# ]
# # 添加数据
# map.add("地图",data,"china")
# # 设置全局变量
# map.set_global_opts(
#       visualmap_opts=VisualMapOpts(
#             is_show=True,
#             is_piecewise=True,
#             pieces=[
#                   {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
#                   {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
#                   {"min":100,"max":500,"label":"100-500","color":"#990033"}
#             ]
#       )
# )
# # 绘图
# map.render()


# import requests #导入请求模块
# from lxml import etree #数据预处理
# from urllib import request #下载方法
#
# #1.确定网址
# #互联网上的标准资源的地址
# url = 'https://v.huya.com/cat/51'
#
# #2.搭建关系 发送请求 接受响应
# #爬虫的原理：伪装成浏览器
# #字典 键名 键值 键值对 {key:value}
# #tab
# headers = {
#    'User-Agent': 'zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
# }
# #工具
# #请求目标网站
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
#
# import requests
# url = "https://www.baidu.com"
# # 请求头信息
# headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# }
# res = requests.get(url=url,headers=headers)
# # 获取相应结果
# print(res) #<Response [200]>
# print(res.status_code) #请求状态码 200
# print(res.text) #获取响应的内容
# print(res.url) #请求的url地址
# print(res.request.headers) #请求头信息
# print(res.headers) #响应头信息


