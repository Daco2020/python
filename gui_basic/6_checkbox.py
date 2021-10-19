from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")

chkvar = IntVar()  # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# variable : 변수를 저 곳에다가 저장한다 (불러오는거 아님!)
# chkbox.select()  # 자동 선택 처리
# chkbox.deselect()  # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())  # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()