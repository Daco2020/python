from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2")
btn3 = Button(root, text="버튼3")
btn4 = Button(root, text="버튼4")
# btn1.pack()
# btn2.pack()
# btn1.pack(side="left")
# btn2.pack(side="right")
# 일반 적인 팩은 쌓이는 느낌이라면 그리드는 지정된 장소에 위치하는 느낌임

btn1.grid(row=0, column=0, padx=50, pady=50) # padx, y : 패딩 값 / 동일 크기를 지정하려면 width, height 로 지정
btn2.grid(row=1, column=1)# 숫자와 상관없이 몇 번째 숫자이냐에 따라 위치 그리드가 생성됨(반드시 1,0/2,0 이 아님)
btn3.grid(row=2, column=2, columnspan=2) # span : 현재 위치로부터 그리드를 더함 // 근데 적용이 안되네..
btn4.grid(row=5, column=5, rowspan=5, sticky=N+W+S+E) 



root.mainloop()