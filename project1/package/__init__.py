# 이 파일은 해당 디렉토리가 패지키임을 알려주는 역할을 합니다.
# 해당 파일이 있어야 패키지로 인식됨
# import로 패키지를 가져오면 __init__.py 파일이 실행되므로 이 파일에서 from . import 모듈 형식으로 현재 패키지에서 모듈을 가져오게 만들어야 합니다. 참고로 .(점)은 현재 패키지라는 뜻입니다.
# from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
# from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴
# from .add_and_multiply import add_and_multiply as add


# __init__ 에 임포트를 미리 해두면 dir() 에 추가되어 패키지만 불러와도 하위 모듈의 함수와 변수를 불러올 수 있음!
# 확인은 dir()로 가능함!




# import module2
# print(dir())
b=2
a=3
print(a*b)
if __name__ == "__main__":
    print(1+2)


