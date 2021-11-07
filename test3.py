# FizzBuzz는 매우 간단한 프로그래밍 문제이며 규칙은 다음과 같습니다.

# 1에서 100까지 출력
# 3의 배수는 Fizz 출력 -> 오구
# 5의 배수는 Buzz 출력 -> 오오구
# 3과 5의 공배수는 FizzBuzz 출력 -> 오구오오구
# 즉, 1부터 100까지 숫자를 출력하면서 3의 배수는 숫자 대신 'Fizz', 5의 배수는 숫자 대신 'Buzz', 3과 5의 공배수는 숫자 대신 'FizzBuzz'를 출력하면 됩니다.

# for i in range(1,101):
#     if i % 3 and 5 == 0:
#         print("오구오오구")
#     elif i % 3 == 0:
#         print("오구")
#     elif i % 5 == 0:
#         print("오오구")
#     else:
#         print(i)


# a = [[[0 for i in range(3)] for j in range(4)] for k in range(2)]
# print(a)


# c = (1,2,3,4,5)
# print(c)
# d = list(c)
# print(c)
# print(d)
# c = d
# print(c)

# c = (1,2,3,4,5)
# d=len(c)-1
# print(c[d])
# del c[4]
# print(c)

# a = dict(키 = '값')
# print(a)


# a = [1,2,3,4,5]
# b = ['a','b','c','d','e']

# c = dict(zip(a,b))
# print(c)

# a = dict({'a':1,'b':2})
# print(a)

# print(bool(-1))

# import random
# import numpy as np

# list = [1, 1, 1, 2, 3, 4, 5, 5, 5]
# list2 = np.unique(list)
# print(list2)

# for i in range(1,5):
# 	if i == 3:
# 		break
# 	print(i, end=' ')

# for i in range(5):
#     for j in range(5):
#         if j >= i:
#             print('*', end=' ')
#     print()


# a = dict(키 = '값')
# print(a)

# a = [1,2,3,4,5]
# b = ['a','b','c','d','e']
# c = dict(zip(a,b))
# print(c)

# a = dict([('a',1),('b',2)])
# print(a)

# a = dict({'a':1, 'b':2})
# # print(a)

# c = a['a']
# print(c)


# # a = {'키':2}
# # print(a)

# a = [1,2,3,4,5]
# del a[2:3]
# print(a)

# a = []
# a[len(a):] = [1]
# a[len(a):] = [2,3]
# print(a)


# def find_smallest_integer_divisor(num): 
#     ## 아래 코드를 입력해주세요.

#     number = 2
#     while number >= num:
#         if num % number == 0:
#             print(number)
#         else :
#             number += 1
    

# print(find_smallest_integer_divisor(15))


# a = {'1':2} # 딕셔너리 생성
# a[2] = 3 # 딕셔너리 추가
# print(a)

# b = {1,2,3}
# set(a)
# print(type(a))
# print(a)
# set(b)
# print(type(b))
# print(b)
# b = list(b)
# print(b)

# set 은 {} 를 사용하나 타입은 set 임
# 딕셔너리와 차이는 키와 값이 없다


# a = set([1,2,3,4,(1,2)])
# print(a)
