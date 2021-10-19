import os
from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco Memopad")
root.geometry("640x480")


tomato = Menu(root)

# 열기 저장 대상 파일 
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 트루, 없으면 폴스
        with open(filename, "r", encoding="utf8") as file: # r 읽기, as 는 변수명 지정
            txt.delete("1.0", END) # 텍스트 전체 범위 삭제
            txt.insert(END, file.read()) # file 변수에서 읽을 것을 삽입한다


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 범위 내용을 가져와서 저장

menu_file=Menu(tomato, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
tomato.add_cascade(label="파일", menu=menu_file)

# 빈껍데기 메뉴 항목들
tomato.add_cascade(label="편집") 
tomato.add_cascade(label="서식")
tomato.add_cascade(label="보기")
tomato.add_cascade(label="도움말")
# 원래는 빈껍데기 메뉴가 생성되어야 하는데 맥에서는 하위 옵션이 없으면 메뉴 항목이 생성되지 않음.

# 스크롤 바, 여기서는 프레임이 따로 없기 때문에 그냥 바로 루트에 집어넣는다
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True) # 전체 공간을 꽉 채우게 하기

scrollbar.config(command=txt.yview)

root.config(menu=tomato)
root.mainloop()