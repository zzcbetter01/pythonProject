#### 6.1 定义函数
# def greet_user(username):
#     """显示简单的问候语"""  # 三引号表示文档字符串的注释，描述函数是做什么的。
#     print('Hello, ' + username.title() + '!')
#
# greet_user('zheng zhi chao')

#### 6.2 传递实参
##  6.2.1  位置实参
## 位置实参的顺序很重要，一定要注意。
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is "+pet_name.title() +'.')
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

##  6.2.2  关键字实参
## 关键字实参是传递给函数的名称-值对。
# describe_pet(animal_type='hamster', pet_name='harry')

##  6.2.3  默认值
## 编写函数时，可给每个形参指定默认值，在调用函数中给形参提供实参，将使用指定的实参，否则使用默认的参数。
# def describe_pet(pet_name, animal_type='dog' ):
#     """显示宠物的信息"""
#     print('\nI have a ' + animal_type + '.')
#     print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
# describe_pet(pet_name='willie')
# describe_pet('haba')
# describe_pet(animal_type='hamster', pet_name='harry')

#### 6.3 返回值
##  6.3.1 返回简单值
# def get_formatted_name(first_name, last_name):
#     """返回整洁的名字"""
#     full_name = first_name + '' + last_name
#     return full_name.title()
# musician = get_formatted_name('zheng', 'zhi chao')
# print(musician)

##  6.3.2 让实参变为可选的
# def get_formatted_name(first_name, last_name, middle_name=''):  # 给middle_name 指定一个空字符串
#     """返回整洁的名字"""
#     if middle_name:
#         full_name = first_name + " " + middle_name + " " + last_name
#     else:
#         full_name = full_name = first_name + ' ' + last_name
#     return full_name.title()
#
# name1 = get_formatted_name('zheng', 'chao', 'zhi')
# name2 = get_formatted_name('zheng','chao')
# print(name1)
# print(name2)

##  6.3.3 返回字典
# def build_person(first_name, last_name):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first' : first_name, 'last': last_name}
#     return person
# musician = build_person('zheng', 'zhi chao')
# print(musician)

#### 6.4 传递列表

# def greet_users(names):
#     """向列表中的每个用户都发出简单的问候"""
#     for name in names:
#         msg = "Hello, " + name.title() + '!'
#         print(msg)
# usernames = ['han lv', 'ty', 'margot']
# greet_users(usernames)

## 6.4.1 在函数中修改列表
# def print_models(unprinted_designs, completed_models):
#     """模拟打印每个设计，直到没有未打印的为止，打印每个设计后，都将其一道列表completed_models中"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         # 根据设计制作打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print('\nThe following models have been printed:')
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models =[]
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#### 6.5 传递任意数量的实参
def make_pizzas(*toppings):  # 形参*toppings中的星号让python创建一个toppings的空元组，并将收到的值装到这个元组中
    """概述要制作的披萨"""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print("-" + topping)
make_pizzas('paaap')
make_pizzas('rrew', 'hhhhssf', 'sdfjjd')

## 6.5.1 传递任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们直到的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'ainstein', location = 'china', field = 'physics' )
print(user_profile)

#### 6.6 导入函数
##  导入特定函数
from module_name import function_name

## 使用as 给函数指定别名
from module_name import function_name as fn

## 使用as 给模块指定别名
import module_name as mn

## 导入模块中的所有函数
from module_name import *




















