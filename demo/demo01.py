# # 类型转换
# # 转换成整形
# # str --> int
# a = '123'
# print (type(a))
# # 酱字符串转换为整数
# b = int(a)
# print(type(b))
#
# # float ---> int
# a = 1.23
# print(type(a))
# # 如果我们将float转换为整数，南无会返回小数点前面的数值
# b = int(a)
# print(b)
# print(type(b))
#
# # 布尔类型转换成字符串
# a = True
# print(a)
# b = str(a)
# print(type(a))
# print(b)
# print(type(b))
# 列表 （只要列表中有数据那么强制类型转换为bool的时候，就返回true）
# 如果类表中什么数据都没有的情况下那么返回的是false
# a = ["章鱼", "路子", "张明"]
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))
#
# # 元组
# a = ('利益', '账期', '战役')
#
# #字典
# a = {'name':'章鱼','age':'13'}
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))
#
#
# a = "123"
# b = 456
# print(a+str(b))

# 多个变量赋值需要用逗号
# a,b,c = 1,2,3
# for k in a,b,c:
#     print(k)
# # 输入input
# name = input('请输入你的名字：')
# print('我的名字是：%s' % name)

# 在控制台输入一个年龄如果您的年龄大于18随了，那么打印可以去网吧了

# age = input('请输入您的年龄')
# # 字符串和整数无法比较
# if int(age)>18:
#     print("可以去网吧")
# if ---else 用法
# if判断条件：
#      判断条件为true的时候执行代码
# else：
#        判断条件为false的时候执行代码

# 在控制台上输入一个年龄 如果您的年龄大于18了 那么输出欢迎光临红浪漫男宾一位
# 否则输出 回家洗洗睡觉
# age = int(input('请输入你的年龄：'))
# if age>18:
#     print('欢迎光临红浪漫男宾一位')
# else:
#     print('回家睡睡吧')

# a = int(input('请输入你的成绩：'))
# if a >= 90:
#     print("成绩为优秀")
# elif a >= 80:
#     print("良好")
# elif a>= 70:
#     print("中等")
# else:
#     print('不及格')

# 循环字符串：
# range(5)
# range(1,6)
# range(1,10,3)
# 循环一个列表
# 一个一个的输出 叫做循环也叫做遍历

# s2 = "china"
# print(s2.startswith('h'))
# print(s2.endswith('n'))
# 切割
# s5 = "1#2#4#5#6"
# k = s5.split("#")
# for i in k:
#     print(i)

# append  追加 在列表的最后追加一个对象/数据
# foot_list = ['我想','吃']
# foot_list.append('苹果')
# print(foot_list)
# # insert 插入 index的值就是你想插入的值下标
# char_list = [1,2,3]
# char_list.insert(2,'b')
# print(char_list)

# extend
# num_list = [10,20,30]
# num1_list = [40,50,60]
# 指定下表添加于元素
# num_list[2]=100

# # num_list.append(num1_list)
# print(num_list)
# # del 变量[指定删除的下标]
# del num1_list[2]
# num_list.pop(-2)
# print(num_list)
# print(num1_list)

# foot_list = ['米饭','大米','稀饭']
# foot = input("你要吃啥")
# if foot in foot_list:
#     print("在")
# else:
#     print("不在")
#
# foot_list = ['米饭','大米','稀饭']
# foot = input("你要吃啥")
# if foot not in foot_list:
#     print("不在")
# else:
#     print("在")

# 当元组只有一个元素的时候，那么他就是整形数据
# 定义只有一个元素的元组，需要在唯一的元素后写一个逗号
# person = {'name':'章鱼','age':'13'}
# # (1)遍历字典的key
# # 字典.keys()方法 获取的字典中所有的key值 key是一个变量的名字 我们可以随便起
# for key in person.keys():
#     print(key)
# # (2)遍历字典的value
# for key in person.values():
#     print(key)
#
# # (3)遍历字典的key和value的值
# for key,varlue in person.items():
#     print(key,varlue)
# # (4)遍历字典的项/元素
# for item in person.items():
#     print(item)

# def f1():
#     print('欢迎光临')
#     print('两位南滨')
#
#
# if __name__ == '__main__':
#     f1()
# # 返回值的关键字是return 存在函数中
# def buy_apple():
#     return '18元'
# #使用一个变量来接收函数的返回值
# foot = buy_apple()
# print(foot)

# import json
#
# demo ={'name':'小明','age':16}
#
# demo1 = open('demo01.txt','w')
# a = json.dumps(demo)
# demo1.write(a)

# import requests
# url = "https://book.dangdang.com/"
# # 请求头信息
# headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# }
# demo = requests.get(url)
# a = demo.text
#
# print(a)
import urllib.parse
import urllib.request
url = 'https://www.baidu.com/s?wd=url'

data = {
    'wd':'周杰伦'
}
new_data = urllib.parse.urlencode(data)
# 请求资源路径
url = url + new_data
# 请求对象的定制为了解决反爬的一种手段
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
}
# 我们需要以来urllib.parse
# name = urllib.parse.quote('周杰伦')
# url = url +name
# 请求对象的定制
request = urllib.request.Request(url=url ,headers=headers)


# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

# urlencode 应用场景：多个参数的时候