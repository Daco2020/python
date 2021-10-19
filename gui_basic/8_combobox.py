import tkinter.ttk as ttk
from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)]  # 1 ~ 31 까지의 숫자가 "일" 이 붙어서 넣어줌
combobox = ttk.Combobox(root, height=5, values=values)  # height : 목록 개수를 의미함
combobox.set("카드 결제일")  # 최초 목록 제목 설정
combobox.pack()

combobox2 = ttk.Combobox(root, height=10, values=values, state="readonly")
# 읽기 전용으로 사용자가 다른 것을 입력할 수 없도록 함.(엉뚱한 값 방지)
combobox2.current(0)  # 0번째 인덱스 값 선택
combobox2.pack()


def btncmd():
    print(combobox.get())  # 선택된 값 표시
    print(combobox2.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()