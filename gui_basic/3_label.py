from tkinter import *
from random import *

# 레이블은 버튼처럼 실제 동작이 아닌 텍스트나 이미지만 보여주는 것

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="source/emoji.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    text = ["나는 엄청나", "나는 굉장해", "나는 훌륭해", "나는 놀라워"]
    shuffle(text)
    label1.config(text=text[1])  # 변경할때는 .config(00=00) 으로 수정
    global photo2  # 전역 변수로 설정하지 않으면 photo2 값이 사라져 나타나지 않음! 꼭 기억할 것!
    photo2 = PhotoImage(file="source/emoji2.png")
    photo3 = [photo, photo2]
    shuffle(photo3)  # 문자열 뿐만 아니라 이미지도 리스트화 시켜서 셔플이 가능하다!!!
    label2.config(image=photo3[1])


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
