from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")  # y 가 높이를 의미함, 내부 세로를 다 채운다는 뜻

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
# set 이 없으면 스크롤을 내려도 다시 올라옴. 꼭 넣어줘야함
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()