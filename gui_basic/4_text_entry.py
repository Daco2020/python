from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)  # 여러 줄을 받아야 할 때 사용
txt.pack()
txt.insert(END, "글자를 입력하세요")  # 입력창 힌트 문구 넣기

e = Entry(root, width=30)  # Entry 는 줄바꿈 불가능 단순 검색용. 한 줄만 받아야 할 때 사용
e.pack()
e.insert(0, "글자를 입력하세요")  # END 나 0이나 같은 결과로 출력


def btncmd():
    #터미널에 출력할 때
    print(txt.get("1.0", END))  # 1 : 첫번쨰 행 , 0 : 0번째 열 ~ END 는 끝까지를 의미함.
    print(e.get())  # Entry 는 공란으로 두면 됨.

    #프로그램에서 내용을 삭제 할 떄
    txt.delete("1.0", END)
    e.delete(0, END)  # insert 에서 0을 넣었으므로 0부터 끝까지 지정


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()