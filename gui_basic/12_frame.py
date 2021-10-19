from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")

Label(root, text="메뉴 선택해").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 햄버거 프레임
frame_burger = Frame(root, relief="solid", bd=1)
# relief : 테두리 모양 , bd : 외곽 프레임 크기
frame_burger.pack(side="left", fill="both", expand=True)
# side : 위치 ,fill : 공간 채우기를 의미 , expand : 외부 공간을 꽉채우기

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="오징어버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="제로콜라").pack()

root.mainloop()