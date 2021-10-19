import time
import tkinter.ttk as ttk
from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")
# 진행상황 바

#----
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# # 100 : 100%
# # indeterminate : 결정되지 않음(좌우로 움직이기만 함)
# # determinate : 왼쪽부터 오른쪽으로 차오름
# progressbar.start(10)  # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()  # 작동중지

# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()
#----

p_var2 = DoubleVar()  # 실수(소수점)까지 표현하는 것
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
# variabel : 이번에는 값을 저장하는 것이 아닌 가져오게 됨
progressbar2.pack()


def btncmd2():
    for i in range(101):  # 1 ~ 100
        time.sleep(0.1)

        p_var2.set(i)
        progressbar2.update()  # for 문 동작 때마다 업데이트하여 반영, 이걸 안쓰면 완료되고 업데이트 됨
        print(p_var2.get())
        if i >= 50:
            print("곧 설치가 끝납니다")


btn = Button(root, text="클릭", command=btncmd2)
btn.pack()

root.mainloop()