
import os
import time
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image


root = Tk()
root.title("😽로디냥_v1")


# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("모든 파일", "*.*"),("PNG 파일", "*.png"),("JPG 파일", "*.jpg")), \
        initialdir="C:/") # 최초에 C:/ 경로를 보여줌

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file) # 어디까지, 무엇을


# 선택 삭제
def del_file(): 
    for index in reversed(list_file.curselection()): # reversed 는 원본은 유지하되 뒤집은 값을 새롭게 변수로 할당하는 것임!
        list_file.delete(index)

# 전체 삭제
def delAll_file():
    list_file.delete(0,END) # list_file 이 엔트리라면 (1, END) 텍스트라면 (0, END)
    
# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '' : # 사용자가 취소를 누를 때 '' 는 빈 문자열을 의미함
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected) # 인서트 할 때 어디 위치에 둘지도 기재해야함
    

# 이미지 통합
def merge_image():

    try:
        # 가로넓이
        img_width = cmb_width.get()
        if img_width == "780(권장)":
            img_width = 780 # -1 일 때는 원본 크기 유지
        else:
            img_width = 1440
        
        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower() # png, jpg 값을 소문자로 변경

        images = [Image.open(x) for x in list_file.get(0, END)] # 이미지 불러오기
        # 이미지 사이즈 리스트에 넣어서 처리
        image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]

        # 계산식
        # 100 * 60 이미지 > 가로를 80으로 줄이면 높이도 변경되어야 함
        # 원본(가로) : 원본(세로) = 변경(가로) : 변경(세로)
        # 원본(가로)*변경(세로) = 원본(세로)*변경(가로)

        
        widths, heights = zip(*(image_sizes))
        # size -> size[0] : width, size[1] : height
        # x_widths = [x.size[0] for x in images]
        # heights = [x.size[1] for x in images]


        # 최대 넓이, 전체 높이 구하기
        max_width, total_height = max(widths), sum(heights)
        # 스케치북 준비
        if img_space > 0:
            total_height += (img_space * (len(images)-1))

        result_img = Image.new("RGB",(max_width, total_height),(255,255,255)) # 배경 흰색
        y_offset = 0 # y 위치 정보
        x_offset = 0
        # for img in images:
        #     result_img.paste(img, (0,y_offset))
        #     y_offset += img.size[1] # height 값 만큼 더해줌
        for idx, img in enumerate(images):
            # width 가 원본이 아닐 경우에는 리사이즈 필요
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (x_offset, y_offset))
            y_offset += (img.size[1] + img_space) # height 값 + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100 # 실제 퍼센트 정보를 계산함 , 1을 더하는 이유는 인덱스가 0부터 시작하므로 1부터 시작할 수 있도록 하기 위함(0 은 나눠지지 않으므로)
            p_var.set(progress)
            progress_bar.update()



        # 포맷 옵션 처리
        curr_time = time.strftime("_%y%m%d_%H%M%S")
        file_name = "MergeImage"+curr_time+"."+img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path) # save 저장 () 안에 저장경로
        msgbox.showinfo("알림", "하나의 이미지로 변환되었습니다! ☝🏼")
    except Exception as err:
        msgbox.showerror("에러", err)

# 시작
def start():
    # 각 옵션 값을 확인
    
    # 파일이 있는지 확인
    if list_file.size() == 0: 
        msgbox.showwarning("경고", "이미지 파일이 넣어주세요!")
        return # 함수를 빠져나옴

    # 저장경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요!")

    merge_image()

# 파일 프레임 (파일 추가, 선택 삭제 + 전체 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # x는 행 을 뜻함

btn_add_file = Button(file_frame, padx=5, pady=5, width=12,text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12,text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12,text="전체삭제", command=delAll_file)
btn_del_file.pack(side="right")



# 리스트 프레임
list_frame = LabelFrame(root, text="파일목록")
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # x 는 행을 뜻함 // ipady : 엔트리 영역 크기

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["780(권장)", "1440(고화질)"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)


# 2. 간격 옵션
# 가로 넓이 레이블
lbl_space = Label(frame_option, text="상하간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷
# 가로 넓이 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_format = ["PNG", "JPG"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


# 진행 상황 프로그레스 바
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임

frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5) # 같은 사이드인 경우 나중에 있는게 순차적으로 붙게 됨.


root.resizable(False, False)
root.mainloop() 