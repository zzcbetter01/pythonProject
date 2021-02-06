#### 4.1 使用字典
##  字典是一系列键值对，每个键都和一个值相关联，可以使用键来访问相关联的值
alien_0 = {'color': "green", 'points': 5}
# new_points = alien_0['points']  # 访问字典中的值
# print('You just earned ' + str(new_points)+" points!")

## 添加键值对
#  ['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

## 创建空字典，方便添加键值对
# alien_0 = {}

## 修改字典的值
# alien_1 = {'color': "green"}
# print("The alien is " + alien_1['color'] + ".")
#
# alien_1['color'] = 'yellow'
# print("The alien is " + alien_1['color'] + ".")

## 例子
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print('Original x_position: ' + str(alien_0['x_position']))
#
# if alien_0["speed"] == 'slow':
#     x_increment = 1
# elif alien_0["speed"] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position']+x_increment
# print('New x_position: ' + str(alien_0['x_position']))

## 删除键值对
# del alien_0['speed']  # 删除之后永久消失
# print(alien_0)

#### 4.2 遍历字典
### 4.2.1 遍历所有的键值对
user_0 = {
    'username': 'zheng zhi chao',
    'first': 'zheng',
    'last': 'zhi chao',
    'family': 'zheng'
}
# for key, value in user_0.items():
#     print("\n Key: " + key)
#     print('Value: ' + value)

### 4.2.2 遍历字典中的所有的键
## 不使用字典中的值时，使用方法keys
# for key in user_0.keys():  # 等价于for key in user_0() 默认遍历所有的键
#     print(key.title())
## 按顺序遍历字典中的所有键
# for key1 in sorted(user_0.keys()):
#     print(key1.title() + ", Thank you for taking the poll.")

### 4.2.2 遍历字典中的所有的值
# print("The following languages have been mentioned:")
# for language in user_0.values():
#     print(language.title())
#
# ##  使用集合set删除重复项
# for language in set(user_0.values()):
#     print(language.title())

#### 4.3 嵌套
## 有时候需要将一系列字典储存在列表中，或将列表作为值储存在字典中，这就是嵌套。
# alien_0 = {'color': "green", 'points': 5}
# alien_1 = {'color': "yellow", 'points': 15}
# alien_2 = {'color': "red", 'points': 20}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

## 4.3.2 在列表中储存字典

## 创建一个具有相同特征的30个外星人
# aliens =[]
# for alien_number in range(0, 30):
#     new_alien = {'color': "green", 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# # for alien in aliens[0:5]:  # 显示前五个外星人
# #      print(alien)
#
# ## 如果前5个外星人是不同的，修改一下
# for alien in aliens[0:5]:
#     if alien['color'] == 'green':
#         alien['color'] = 'red'
#         alien['points'] = 10
#         alien['speed'] = 'medium'
# for alien in aliens[0:5]:  # 显示前五个外星人
#     print(alien)

## 4.3.2 在字典中储存列表
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
print('You ordered a ' + pizza['crust'] + '-crust pizza' + ' with the following toppings:')
for topping in pizza['toppings']:
    print('\t'+topping)

## 4.3.2 在字典中储存字典
users = {
    'number1': {
        'first': 'zheng',
        'last': 'zhi chao',
        'location': '睢县'
    },
    'number2': {
        'first': 'zhang',
        'last': 'xue',
        'location': '日照'
    },
}
for username, user_info in users.items():
    print("\n Username: " + username)
    full_name = user_info['first']+" " +user_info['last']
    location = user_info['location']
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())

