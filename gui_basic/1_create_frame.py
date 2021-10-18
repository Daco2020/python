from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")
#root.geometry("640x480+300+300") "가로 x 세로 + x좌표 + y좌표" 가로 세로 사이에는 소문자 'x' 만 사용가능

root.resizable(False, False)
# False 로 두면 마우스로 창 크기 변경 불가

root.mainloop()
