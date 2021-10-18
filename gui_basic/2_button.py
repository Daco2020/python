from tkinter import *
from random import *

root = Tk()
root.title("Daco GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()  # pack을 호출해야만 실제 버틴이 생성됨

btn2 = Button(root, padx=5, pady=10, text="버튼2 길어져라 얍얍!")
btn2.pack()  # padx, pady -> 버튼 내 공간을 의미함, 텍스트가 길어지면 그만큼 넓어짐

btn3 = Button(root, width=5, height=3, text="버튼3 길어져랴 얍얍!")
btn3.pack()  # width, height -> 버튼의 실제 크기를 지정, 단 텍스트 길이와 무관함

btn4 = Button(root, fg="yellow", bg="yellow", text="버튼4 색상 바꾸기")
btn4.pack()  # 맥에서는 bg 적용이 안됨.. 그 외에 버튼 모양새를 바꾸는 relief 옵션도 적용이 안된다고 함..ㅜㅜ

photo = PhotoImage(file="source/emoji.png")
btn5 = Button(root, image=photo, width=300, height=300, text="버튼5")
btn5.pack()  # 이미지 버튼을 만드는 방법, 기본은 이미지 크기이나 따로 크기 지정도 가능.
# 단 이미지는 잘림, 그리고 텍스트는 노출되지 않음


def btncmd():
    text = ["나는 엄청나", "나는 굉장해", "나는 훌륭해", "나는 놀라워"]
    shuffle(text)
    print(text[1])


btn6 = Button(root, text="오늘의 나는", command=btncmd)
btn6.pack()  # 실제 동작하는 버튼의 구조는 이렇게 됨. 커맨드로 함수를 불러로고 함수 내용이 실행됨

root.mainloop()
