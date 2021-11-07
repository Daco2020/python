#import로 모듈 가져오기

#해당 모듈을 가져올 때, 요소를 사용하려면 모듈명.요소명 으로 적어야함. (as는 이름을 지정해주는 것)
import math as m
print(m.pi)


#해당 모듈에서 원하는 요소(변수, 함수, 클래스 등)만 가져 올 때. (as는 이름을 지정해주는 것)
from math import pi as p
print(p)


#해당 모듈에서 요소를 여러개 가져 올 때. (as는 이름을 지정해주는 것)
from math import pi as p, sqrt as s
print(p)
print(s(2))


#해당 모듈에서 요소를 모두 가져 올 때
from math import *
print(pi)
print(sqrt(2))


#import로 패키지 가져오기
# import 패키지.모듈 
# import 패키지.모듈1, 패키지.모듈2 -> 여러개 가져오기

# 일반적인 패키지.모듈 가져오는 방법
import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
print(response.status)

# 불러온 패키지.모듈을 as로 이름 줄여주기 
import urllib.request as r
response = r.urlopen('http://www.google.co.kr')
print(response.status)

# from import로 패키지의 모듈에서 일부만 가져오기

# from 패키지.모듈 import 변수
# from 패키지.모듈 import 함수
# from 패키지.모듈 import 클래스
# from 패키지.모듈 import 변수, 함수, 클래스

# urllib 패키지의 request 모듈에서 urlopen urlopen 함수, Request 클래스를 가져옴
from urllib.request import Request as r, urlopen as u 
req = r('http://www.google.co.kr')       # Request 클래스를 사용하여 req 생성
response = u(req)                        # urlopen 함수 사용
print(response.status)

