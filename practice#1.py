from random import *

def add(a,b):
    return a+b

a = 3
b = 4
c = add(a,b)
print(c)
#a, b are parameter(매개변수)
print(add(1,2))
#1, 2 are arguments(인수)


def wdd(a, b):
    result = a+b
    return result
d = wdd(a,b)
print(d)
#일반적인 함수(입력값과 결과값이 모두 있는 함수) > 결괏값을 받을 변수 = 함수이름(입력인수1, 입력인수2, ...)


def say():
    return 'Hi'
print(say())
#입력값이 없는 함수 > 결괏값을 받을 변수 = 함수이름()


def zdd(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))
print(zdd(1,2))
e = zdd(3,4)
print(e)
#결괏값이 없는 함수 > 함수이름(입력인수1, 입력인수2, ...), 변수에 결과값이 저장이 안됨 none으로 출력


def say():
    print('bye')
print(say())
say()
#입력값도 결괏값도 없는 함수 > 함수이름()


team_five = ["원소연", "황주영", "제갈창민", "이유진", "김은찬", "구유진"]




def output():
    shuffle(*args)
    num = 1
    for i in args:
        result = print("{0}번 순서는 {1} 입니다." .format(num ,i))
        num += 1
    return result

result = output(team_five)
print(result)