# >>> bool(1)
# True
# >>> bool(0)
# False
# >>> bool(1.5)
# True
# >>> bool('False') 
# True

# print(False and True) 
# print(False and False)
# print(True or True)     
# print(True or False)
# print(True and 'Python')
# print(True or 'Python')
# print('Python' and True)
# print('Python' and False)
# print('Python' or True)
# print(False and 'Python')
# print(False or 'Python')
# print(0 or False)
# print(0 and 'Python')

# camille = {
#     'health': 575.6,
#     'health_regen': 1.7,
#     'mana': 338.8,
#     'mana_regen': 1.63,
#     'melee': 125,
#     'attack_damage': 60,
#     'attack_speed': 0.625,
#     'armor': 26,
#     'magic_resistance': 32.1,
#     'movement_speed': 340
# }

# camille2 = [1,2,3]
# a = 3 * camille2

# print(a)

# print(bool(0.0))
# print(bool(0.1))

# x = int(input())

# if 10 < x < 21 :
#     print('11~20')
# elif 20 < x < 31 :
#     print('21~30')
# else :
#     print('아무것도 해당되지 않음')

# for tomato in range(1,5):
#     print('tomato')


# x = [49, -17, 25, 102, 8, 62, 21]

# for potato in x:
#     print(potato * 10, end=' ')

#                  # 초기식
# while i < 100:            # while 조건식
#      print('Hello, world!')    # 반복할 코드
#      i += 1           


# import random
# import numpy as np

# list = [1, 1, 1, 2, 3, 4, 5, 5, 5,]

# print(list)
# list2 = np.unique(list)
# print(list2)

# for i in list2:
    # print(i)

# i = 2
# j = 5

# while i <= 32 or j > 0:
#     print(i,j)
#     i *= 2
#     j -= 1

# i = 0
# while True:
#     if i % 10 != 3:
#         i += 1
#         continue
#     if i == 73:
#         break
#     print(i, end=' ')
#     i += 1



# for i in range(7):
#     for j in range(i+10):
#         print('*',end=' ')
#     print()


# for i in range(5):
#     for j in range(5):
#         if j < i :
#             print('',end=' ')
#         else :
#             print('*', end=' ')
#     print()


# for i in range(1,101):
#     if i % 15 == 0 :
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# for i in range(1, 101):
#     print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
#     # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리

# a = 2
# b = 11

# # 1안
# for i in range(1, 101):
#     if i % (a*b) == 0 :
#         print('FizzBuzz')
#     elif i % a == 0 :
#         print('Fizz')
#     elif i % b == 0 :
#         print('Buzz')
#     else:
#         print(i)

# # 2안
# for i in range(1, 101):
#     print('Fizz' * (i % a == 0) + 'Buzz' * (i % b == 0) or i)

# import turtle as t
# t.shape('turtle')
# t.forward(100)
# t.right(90)
# t.forward(200)
# t.left(45)
# t.backward(200)
# t.left(100)
# t.forward(80)

# for i in range(1,5):
#     t.forward(100)
#     t.backward(100)

# t.color('#00bcd4')
# t.begin_fill()
# t.begin_poly()

# for i in range(1,361):
#     t.forward(3)
#     t.left(1)

# t.end_fill()

# for i in range(10):
#     t.circle(100)  
#     t.right(20)


# t.exitonclick()