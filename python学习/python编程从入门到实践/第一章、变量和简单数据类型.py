#### 1.1 字符串
# 引号可以是单引号，也可以是双引号
## 1.1.1 使用方法修改字符串的大小写
# name = "ada lovelace"
# print(name.title())  # .的意思是让Python对变量name执行方法title指定的操作，title()以首字母大写的方式显示每个单词
# print(name.upper())  # 将字符串改为全部大写
# print(name.lower())  # 将字符串改为全部小写

## 1.1.2 合并字符串
# 使用"+"
# first_name = 'ada'
# last_name =  'lovelace'
# full_name = first_name+" "+last_name
# print(full_name.title())
# message = "Hello, " + full_name.title()+'!'
# print(message)

## 1.1.3 使用制表符或者换行符来添加空白
# \t：制表符；\n:换行符
# print('python')
# print('languages:\n\tPython\n\tJava\n\tR')

## 1.1.4 删除空白
# favorite_language = ' python '
# print(favorite_language.strip())  # 删除字符串两端空白
# print(favorite_language.rstrip())  # 删除字符串右端空白
# print(favorite_language.lstrip())  # 删除字符串左端空白

#### 1.2 数字
## 1.2.1 整数
## 1.2.2 浮点数
## 1.2.3 使用函数str()b避免类型错误
age = 23
message = "Happy "+ str(age) +"rd Birthday!"
print(message)


