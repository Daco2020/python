from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")
# 체크 박스는 여러개 선택이지만 라디오 버튼은 한 개만 택하는 것을 의미함(= 옵션버튼)
# 라디오버튼의 원리는 저장하는 변수값이 한 곳에 저장되느냐 이다. 즉 저장되는 변수 위치가 다르다면 옵션선택에 대한 영향을 받지 않음

Label(root, text="메뉴를 선택하세요").pack()  # 코드를 한 줄로도 작성 가능

burger_var = IntVar()  # 여기에 int 형으로 값을 저장한다.
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()  # 코드를 한 줄로도 작성 가능

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="제로콜라", value="제로콜라", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())  # 선택한 옵션의 값(value)을 출력
    print(drink_var.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()