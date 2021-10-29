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

for i in range(5):
    for j in range(5):
        if j >= i:
            print(rjust('*', end=' '))
    print()