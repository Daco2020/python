from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=3)
# selectmode : 선택 방법(단일, 중복 등)
# height : 리스트를 몇 개까지 노출할지 보여줌. 0이라면 전체 다보여줌
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")  # END를 사용하면 마지막에 차례로 들어가게 된다!
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤에 것 삭제, 0이라면 맨 처음 리스트

    # 갯수 확인
    # print("리스트는", listbox.size(), "개가 있어요")  # size() 는 리스트 갯수를 알려줌

    # 항목 확인
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))  # get 은 리스트를 불러옴
    print("선택된 항목 : ", listbox.curselection())
    # curselection 는 인덱스 값(위치)을 반환해줌


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()