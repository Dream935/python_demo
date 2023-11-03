# #
# str1 = "name"
# str2 = "ithema"
# str3 = "mingzi"
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#         print(f"字符串{str3}的长度是{count}")
# my_len(str1)
# my_len(str2)
# my_len(str3)
#
# def name():
#     print("你好我叫什么名字")
#     return
# name()
# # ·····················函数，，练习案例：自动查核酸·······················
# def name():
#     print("欢迎来到黑马程序员！\n请出示您的健康码以及72小时核酸证明！")
#     return
# name()
# def add(x,y):
#     result = x+y
#     print(f"{x}+{y}的计算值是:{result}")
# add(5,6)
#
# def name(x):
#     if x <= 37.5:
#         print(f"欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！\n"
#               f"体温测量中，您的体温是：{x}度，体温正常请进！")
#     else:
#         print(f"欢迎来到黑马程序员！请出示您 的健康码以及72小时核酸证明，并配合测量体温！\n"
#               f"体温测量中，您的体温是：{x}度，需要隔离！")
# name(float(input("你的体温是多少:")))
#
# def name(a,b):
#     resource = a+b
#     return resource
#     print("nihao")
# random = name(5,6)
# print(random)
# # ·······························案例·······································
# money = 500000
# name =str(input("请输入姓名："))
#
# def demo( ):
#     print("·················查询余额··························")
#     print(f"{name}，你好，您的余额剩余：{money}元")
# def demo1(num):
#     global money
#     money += num
#     print("·················存款··························")
#     print(f"{name}，你好，您的存款余额：{num}元成功,\n{name},您的账户剩余金额{money}")
#     return num
# def demo2(nam):
#     global money
#     money -= nam
#     print("·················取款··························")
#     print(f"{name}，你好，您的取款金额：{nam}元,取款成功，\n{name},您的账户剩余金额{money}")
#     return nam
# def main():
#     print("·················主菜单··························")
#     print(f"{name}，你好，欢迎来到黑马银行ATM，请选择操作：")
#     print(f"查询余额\t[输入1]")
#     print(f"存款\t\t[输入2]")
#     print(f"取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("请输入你您的选择：")
#
# while True:
#     key_input = main()
#     if key_input == '1':
#         demo( )
#         continue
#     elif key_input == '2':
#         demo1(int(input("请输入你的存款金额:")))
#         continue
#     elif key_input == '3':
#         demo2(int(input("请输入你的取款金额：")))
#         continue
#     else :
#         print("程序退出了")
#         break
#
# # ············列表 list 使用··················
#
# mylist = ["itcake","itheima","python"]
# index = mylist[0]
# print(f"{index}")
# # 查找元素的下标
# index = mylist.index("itheima")
# print(f"{index}")
# # # 修改特定下标                                           index查找元素下标
# mylist[0] = "智慧团建"
# print(f"修改的下标：{mylist}")
#
# # 在指定的下标插入索引的值                                  insert(1,"你是谁")指定下标插入元素
# index = mylist.insert(1,"你是谁")
# print(f"列表的插入：{mylist}")
#
# # 在列表后插入一个元素                                          append填加一个
# mylist.append("黑马程序员")
# print(f"列表在追加元素后，结果是：{mylist}")
# # 在列表尾部追加一批新元素                                      extend 添加一批
# mylist1 = [1,2,3]
# mylist.extend(mylist1)
# print(f"列表在追加一个新的元素，结果是：{mylist}")
# # 删除指定的下标元素 删除下标2 itheima
# del mylist[2]
# print(f"列表删除元素后结果：{mylist}")
# # 删除下标1 你是谁                                                        .pop取出删除
# mylist.pop(1)
# print(f"列表删除元素后结果：{mylist}")
# element = mylist.pop(1)
# print(f"通过pop方法区属元素{mylist}，取出的元素是{element}")
# #
# mylist = ["itcake","itheima","python","itheima"]
# # 通过remove移除元素 从前往后，要是重复移除在调用一次remmove                  remmove 移除元素
# mylist.remove("python")
# print(f"通过remove移除元素{mylist}")
# # 清空列表的内容                                                        clear清楚
# mylist.clear()
# print(f"清空列表{mylist}")
#
# mylist = ["itcake","itheima","python","itheima"]
# # # 统计的元素有几份 itheima 有几分                                        count统计
# count = mylist.count("itheima")
# print(f"itheima有{count}份")
# #
# # 统计列表中有几个元素                                                len列表里有多少个元素
# count = len(mylist)
# print(f"列表元素的总数{count}份")
# mylist = [21,25,21,23,22,20]
# print(f"{mylist}")
# mylist.append(31)
# print(f"追加一个数字{mylist}，到列表的尾部")
# demo = [29,33,30]
# mylist.extend(demo)
# print(f"追加一个新的列表{mylist}，到列表的尾部")
# demo1 = mylist.pop(0)
# print(f"取出第一个元素（应是{demo1}）")
# demo2 = mylist.pop(-1)
# print(f"取出最后一个元素（应是{demo2}）")
# demo3=mylist.index(31)
# print(f"查找元素{demo3}，在列表中的下标位置

# 列表和元组下标都是按0开始

# 定义元组
# t1 =(1,"hello",True)
# t2 =()
# t3 = tuple()
# print(f"t1的类型是{type(t1)}")
# # 元组的嵌套
# t5 = ((1,2,3),(4,5,6))
# print(f"t5的类型{type(t5)}")
# # 下标索引取除内容
# num = t5[1][2]
#
# print(f"{num}")
# t6 = ("船只教育","黑马程序员","python")
# index = t6.index("python")
# print(f"python下标{index}")
# t7 = ("船只教育","黑马程序员","python","黑马程序员")
# num =t7.count("黑马程序员")
# print(f"统计黑马程序员字符串有几个{num}")
# # 元组的遍历
# index= 0
# while (index<len(t7)):
#     print(f"{t7[index]}")
#     index +=1
# demo = ("周杰伦",11,["football","music"])
# num =demo.index(11)
# print(f"年龄下标:{num}")
# num1= demo[0]
# print(f"学生的姓名:{num1}")
# 删除学生爱好中的football
# demo = ("周杰伦",11,["football","music"])
# del demo[2][0]
# print(f"{demo}")
# # 添加爱好:从顶到爱好list内
# demo[2].append("coding")
# print(f"{demo}")



# ···················字符串查找··················
# demo = "itheima and itcast"
# value = demo[2]
# value2 = demo [-16]
# print (f"从字符串{demo}取消表2的元素，值是：{value}，取小标为-16的元素，值是{value2}")
# demo1 = demo.index("and")
# print (f"在demo里查找字符串{demo1}")
#
# # .replace字符串替换
# demo2=demo.replace("it","程序")
# print(f"将字符串{demo}更换成：{demo2}")
#
# # .split字符串分割
# demo3 = demo.split(" ")
# print(f"字符串{demo}分割成{demo3}")
#
# # .strip取出前后空格
# name1 = "12itheima and itcast21"
# demo4=name1.strip( )
# print(f"字符串{name1}去除空格{demo4}")
#
# # .strip("")去除想要的字符
# name = "12itheima and itcast21"
# demo5=name.strip("12")
# print(f"字符串{name}去除字符12：{demo5}")
#
# # len( )统计字符串长度
# demo6=len(demo)
# print(f"字符串{demo}长度一共是{demo6}")
#
# # count()字符串出现的次数
# demo7 = demo.count("it")
# print(f"字符串{demo}，it出现的次数{demo7}")
#
# # ··············作业·················
# demo = "itheima itcast boxuegu"
# name=demo.count("it")
# name1=demo.replace(" ","|")
# name2 = name1.split("|")
# print(f"字符串{demo}中有：{name}个it字符")
# print(f"字符串{demo}，被替换后，结果：{name1}")
# print(f"字符串{name1}，按照|分割后，得到：{name2}")
#
# # ···················切片····················
#
# # 对list进行切片，从1开始，4结束，(结束不包含本身)步长1
# demo = [0, 1, 2, 3, 4, 5, 6]
# name = demo[1:4]
# print(f"结果1：{name}")
#结果:123
# # 对tuple进行切片，从头开始，到最后结束，步长1可以省略
# name1 = demo[:]
# print(f"结果2：{name1}")
#
# # 对str进行切片，从头开始，到最后结束，步长 2
# demo1 = "012345678"
# name2 = demo1[::2]
# print(f"结果3：{name2}")
#
# # 对str进行切片，从头开始，到最后结束，步长-1
# name3 = demo[::-1]
# print(f"结果4：{name3}")
#
# # 对列表金相切片，从3开始，到1结束，步长-1
# demo = [0,1,2,3,4,5,6]
# name4 = demo[3:1:-1]
# print(f"结果5:{name4}")
#切片 demo[起始位置：结束位置：步长]
# 起始位置个结束位置可以省略

# # 对元组进行切片，从头开始，到尾结束，步长-2负数从后开始
# demo = (0,1,2,3,4,5,6)
# name5 = demo[::-2]
# print(f"结果5:{name5}")

# ·············作业················
# demo = "万过薪月，员序程马黑来，nohtyP学"
# name = demo.split(",")
# name1 = demo.replace("，"," ")
# name2=name1.strip("万过薪月 来 nohtyP 学")
# name4=name2[::-1]
# print(f"{name4}")


# 集合
# name = {"创智教育","黑马程序员","itheima","传智教育","黑马程序员"}
# name.add("传智教育")
# print(f"{name}")
# name.remove("传智教育")
# print(f"{name}")
# # 随即取出
# demo = name.pop()
# print(f"{demo}")
# name.clear()
# print(f"{name}")
# # 取两个数的差集
# set1 = {1,2,3}
# set2 = {1,5,6}
# 在集合1的基础上寻找集合2不同点
# set3 = set1.difference(set2)
# print(f"{set3}")
# print(f"{set1}")
#####在集合1内删除和集合2相同的元素
# set1.difference_update(set2)
# print(set1)
# print(set2)
#####集合合并
# set3 = set1.union(set2)
# print(f"{set3}")
# # 集合的遍历
# name = {"创智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员"}
# for demo in name:
#     print(f"{demo}")

#作业
# my_list = ['黑马程序员', '传智教育', '黑马程序员', '传智播客',
#            'itheima', 'itcast', 'itheima', 'itcast', 'best']
# my_set = set()
# for demo in my_list:
#     my_set.add(demo)
# print(f"{my_list}")
# print(f"{my_set}")

# 字典
# 字典没有下标索引
#            key   Value  通过key寻找value
# my_dict = {"王力宏":100,"张宇":79,"张建":99}
# dict1 = {}        #空字典
# dict2 = dict()     #空字典
# demo = my_dict["王力宏"]
# print(f"王力宏成绩是{demo}")

# 字典的嵌套
# my_dict ={
#     "王力宏":{"语文":77,"数学":66,"英语":33},
#     "林俊杰":{"语文":88,"数学":86,"英语":55},
#     "周杰伦":{"语文":99,"数学":96,"英语":66}
# }
# # print(f"{my_dict}")
# # 寻找周杰伦数学成绩
# demo = my_dict["周杰伦"]["数学"]
# print(f"{demo}")
#
# # 新增字典
# my_dict["张宇"]={"数学":55,"语文":99,"英语":90}
# print(f"{my_dict}")
#
# # 更新元素
# my_dict["张宇"]["数学"]=40
# print(f"{my_dict}")
#
# #删除元素
# my_dict.pop("周杰伦")
# print(f"{my_dict}")
#
# #清空元素
# # my_dict.clear()
# # print(f"{my_dict}")
#
# #获取全部key
# keys = my_dict.keys()
# print(f"{keys}")
#
# #遍历字典
# # 方法一
# # for key in keys:
# #     print(f"{key}")
# #     print(f"{my_dict[key]}")
# # 方法二
# for key in my_dict:
#     print(f"{key}")
#     print(f"{my_dict[key]}")

# 字典作业
# my_dict = {"王力宏":{"部门":"科技部","工资":3000,"级别":1},
#            "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
#            "林俊杰":{"部门":"市场部","工资":7000,"级别":4},
#            "张学友":{"部门":"科技部","工资":4000,"级别":1},
#            "刘德华":{"部门":"市场部","工资":6000,"级别":2}}
# print(f"{my_dict}")
# for name in my_dict:
#     if (my_dict[name]["级别"]==1):
#         demo = my_dict[name]
#         demo["级别"]=2
#         demo["工资"]+=1000
#         my_dict[name]=demo
# print(f"{my_dict}")

# open函数的使用
# 打开文件
# f = open("测试.txt","r",encoding="utf-8")
# print(type(f))

# read()方法
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取全部内容：{f.read()}")

# 读取文件 - readlines()
# lines = f.readlines() #读取文件的全部行，封装到列表中
# print(f"{lines}")

# lines1 = f.readline()
# print(f"读取第一行{lines1}")
# lines2 = f.readline()
# print(f"读取第二行{lines2}")

# for循环读取文件行
# for k in f:
#     print(f"{k}")
# # 把文件关闭
# f.close()

# with open 语法
#
# f = open("测试.txt","r",encoding="utf-8")
# 跟下面语句用法是一样的
# with open("测试.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(f"每一行数据是：{line}")

#不定长 -位置不定长 *号
#不定长定义的形式参数会作为  元组  存在，接受不定长数量的参数传入
#
# def user_info(*args): #实参
#     print(f"args参数的类型是：{type(args)}内容是{args}")
# user_info(1,2,3,'小明','男孩') #形参
# 实参传入形参     一个*实参不受限制传  两个**只能通过字典像是传值 key = value
#不定长，关键不定长，**号  字典形式传输通过key = Value
# def user_info(**kwargs):
#     print(f"args参数的类型是：{type(kwargs)}内容是{kwargs}")
# user_info(name='小王')

# try有异常执行except
# try:
#     f = open("E:/abc.txt","r",encoding="utf-8")
# except:
#     print("出现异常，因为文件不存在，我将open的模式，改为w模式去打开")
#     f= open("E:/abc.txt","w",encoding="urf-8")

# 引用time这个库，要使用这个库需要后面加点来引用
# import time #导入time模块
# print("你好")
# time.sleep(10)  #通过.就可以使用模块内部的全部功能
# print("你好")
# 直接用from这个库里的sleep模块不用加点
# from time import sleep
# print("你好")
# sleep(10)
# print("你好")

# 使用as给特定的功能加上别名
# import time as t
# t.sleep(12)
# from time import sleep as s
# s(5)

# demo ="itheima itcast boxueegu"
# num = demo.count("it")
# print(f"统计字符串有多少个it字符{num}个it字符")
# num1 = demo.replace(" ","|")
# print(f"将字符串内的空格,求暗部替换成|{num1}")
# num2 = num1.split("|")
# print(f"并按照进行字符串分割得到列表{num2}")

# 联系案例

# str = "万过薪月,员序程马黑来,nohtyp学"
# demo=str[::-1]
# num = demo.replace(","," ")
# num2 = num[9:15]
# print(f"{num2}")

# 统计单词数目
# 方法一
# with open("word.txt","r",encoding="utf-8") as f:
#     m = f.read()
#     q = m.count("itheima")
#     print(f"{q}")


import json
# # 准备列表，列表内每一个元素都是字典，将其转入JSON
# data = [{"name":"张大仙","age":11},{"name":"张大锤","age":14},{"name":"小明","age":88}]
# json_str = json.dumps(data,ensure_ascii=False)
# print(type(json_str))
# print(json_str)
#  # 准备字典，将其转换成JSON
# d ={"name":"周杰伦","add":"台北"}
# json_str =json.dumps(d,ensure_ascii=False)
# print(type(json_str))
# print(json_str)
#
# # 将JSON字符串转换python数据类型[{k:v,k:v},{k:v,k:v}]
# s = [{"name": "张大仙", "age": 11}, {"name": "张大锤", "age": 14}, {"name": "小明", "age": 88}]
# m = json.loads(s)
# print(type(m))
# print(m)
# # 将JSON字符串转换为python数据类型{k:v,k:v}
# c = {"name":"周杰伦","add":"台北"}
# k =json.loads(c)
# print(type(k))
# print(k)

# 类的定义
# class Student:
#     name = None
#
#
#     def say(self):
#         print(f"大家好啊，我是{self.name}，欢迎大家多多关照")
#
# stu = Student()
# stu.name = "周杰伦"
# stu.say()
# 对象学习
# 设计一个类 （类比生活中，设计一个登记表）
# class Student:
#     name =None                      #记录学生姓名
#     gender = None                   #记录学生性别
#     nationality = None              #记录学生学籍
#     native_place = None             #记录学生籍贯
#     age = None                      #记录学生年龄
# # 2.创建一个对象
# stu_1 = Student()
# # 3 .对象属性进行赋值
# stu_1.name ="林俊杰"
# stu_1.gender = "男"
# stu_1.nationality = "中国"
# stu_1.native_place = "山东省"
# stu_1.age = 32
# # 4.获取对象中的赋值
# print(stu_1.name)
# print(stu_1.gender)
# print(stu_1.nationality)
# print(stu_1.native_place)
# print(stu_1.age)

 # 定义一个带有成员的方法
# class Student:
#     name =None
#     def say_hi(self):
#         print(f"大家好,我是{self.name},请大家多多关照")
# stu = Student()
# stu.name = "章鱼"
# stu.say_hi()
# print("----------- 100-999 之间水仙花数----------")
for i in range(100,1000):
    a = i%10
    b = i//10%10
    c = i//100
    if a*a*a+b*b*b+c*c*c == i:
        print(i)

# 输出一个三行四列的长方形
