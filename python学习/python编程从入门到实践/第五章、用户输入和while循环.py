#### 5.1 函数input的工作原理
## input接受一个参数，即要向用户显示的提示和说明，让用户知道该如何做
# message = input('Tell me somthing, and I will repeat it back to you: ')
# print(message)

## 如果提示超过一行，可能需要将提示储存在一个变量中
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print("\nHello, "+ name + '!')

## 使用int来获取数值输入
# age = input('How old are you ?')
# age = int(age)
# print(age >= 18)

## 求模运算符
## % 是一个很有用的工具，将两个数相除并返回余数。
## 判断一个数是偶数还是奇数。
# number = input('Enter a number, and I will tell you if it is even or odd: ')
# number = int(number)
# if number % 2 == 0:
#     print('\nThe number '+ str(number) + ' is even.')
# else:
#     print('\nThe number '+ str(number) + ' is odd.')

#### 5.2 While 循环
## for循环是针对集合中的每个元素的一个代码块，而While循环不断地运行，直到指定的条件满足为止。
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

## 让用户自己选择何时退出
# prompt = "Tell me something , and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

## 使用标志
## 在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态，这个变量被称为标志。
# prompt = "Tell me something , and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

## 使用break退出循环
# prompt = "Tell me something , and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         break
#     else:
#         print(message)

## 在循环中使用continue
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue  # 如果结果为0，就执行continue语句，让python忽略余下的代码，并返回循环的开头；否则，执行循环中余下的代码。
#     print(current_number)

#### 5.3 While 循环处理列表和字典
## for循环是一种遍历列表的方式，但是不应该修改列表。而要在遍历列表的同时对其修改，可使用while循环。
## 5.3.1 在列表间移动元素

# 首先创建一个待验证的用户列表
# 和一个用于储存已验证用户的列表
# unconfirmed_users = ['alice', 'brain', 'candace']
# confirmed_users = []
#
# # 验证每个用户，直到没有未验证用户为止，将每个经过验证的列表都已到已验证的列表之中
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print('Verifying user: ' + current_user.title())
#     confirmed_users.append(current_user)
# # 显示所有已验证的用户
# print('The following users have been confirmed:')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

## 5.3.2 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets: # 删除所有这些元素，可执行一个while循环
    pets.remove('cat')
print(pets)























