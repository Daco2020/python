from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")


def create_new_file():
    print("뀨웅?")


tomato = Menu(root)

# File 메뉴
menu_file = Menu(tomato, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()  # 구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save ALL", state="disable")  # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)  # 프로그램 종료
tomato.add_cascade(label="File", menu=menu_file)
# menu_file 을 add_cascade 를 통해 레이블 File 로 묵어 준다.

# Edit 메뉴 (빈 값)
tomato.add_cascade(label="Edit")  # 메뉴 항목 이름

# Language 메뉴 추가 (radio 버튼으로 택1), 프로그램 컨셉 변경처럼 응용가능
menu_lang = Menu(tomato, tearoff=0)
menu_lang.add_radiobutton(label="a")
menu_lang.add_radiobutton(label="b")
menu_lang.add_radiobutton(label="c")
tomato.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 (check 버튼으로 다중 택)
menu_view = Menu(tomato, tearoff=0)
menu_view.add_checkbutton(label="a")
menu_view.add_checkbutton(label="b")
menu_view.add_checkbutton(label="c")
tomato.add_cascade(label="View", menu=menu_view)
# 맥에서 View 메뉴를 만들면 전체 스크린 기능이 자동 추가됨

root.config(menu=tomato)
root.mainloop()