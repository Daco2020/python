import tkinter.messagebox as msgbox  # as 는 이름을 바꿔주는 것임
from tkinter import *
# brew install python-tk@3.9 -> 맥에서는 이걸 설치해야 실행됨.

root = Tk()
root.title("Daco GUI")
root.geometry("640x480")
# 메세지박스는 팝업을 의미함


def info():
    msgbox.showinfo("알림", "당신은 훌륭합니다.")  # 첫 번째는 알림 타이틀 두 번째는 알림 메시지를 의미함


def warn():
    msgbox.showwarning("경고", "당신은 너무 훌륭합니다.")


def error():
    msgbox.showerror("에러", "당신의 훌륭함이 한계를 넘어 작동하지 않습니다.")


def cancel():
    msgbox.askokcancel("확인 / 취소", "당신의 훌륭함을 멈추시겠습니까?")


def cancel2():
    msgbox.askretrycancel("재시도 / 취소", "당신의 훌륭함을 유지하시겠습니까?")


def cancel3():
    msgbox.askyesno("예 / 아니요", "당신의 훌륭함을 유지하시겠습니까?")


def cancel4():
    response = msgbox.askyesnocancel(title=None, message="당신의 훌륭함을 유지하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니요 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답", response)  #True, False, None -> 예 : 1, 아니요 : 0, 그 외
    if response == 1:
        print("예")
    elif response == 0:
        print("아니요")
    else:
        print("취소")
    # 응답별로 다른 동작을 수행할 수 있음


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=cancel, text="취소").pack()
Button(root, command=cancel2, text="재시도").pack()
Button(root, command=cancel3, text="예/아니요").pack()
Button(root, command=cancel4, text="예/아니요/취소").pack()

root.mainloop()