
import os
import time
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image


root = Tk()
root.title("๐ฝ๋ก๋๋ฅ_v1")


# ํ์ผ ์ถ๊ฐ
def add_file():
    files = filedialog.askopenfilenames(title="์ด๋ฏธ์ง ํ์ผ์ ์ ํํ์ธ์", \
        filetypes=(("๋ชจ๋  ํ์ผ", "*.*"),("PNG ํ์ผ", "*.png"),("JPG ํ์ผ", "*.jpg")), \
        initialdir="../Desktop") # ์ต์ด์ C:/ ๊ฒฝ๋ก๋ฅผ ๋ณด์ฌ์ค

    # ์ฌ์ฉ์๊ฐ ์ ํํ ํ์ผ ๋ชฉ๋ก
    for file in files:
        list_file.insert(END, file) # ์ด๋๊น์ง, ๋ฌด์์


# ์ ํ ์ญ์ 
def del_file(): 
    for index in reversed(list_file.curselection()): # reversed ๋ ์๋ณธ์ ์ ์งํ๋ ๋ค์ง์ ๊ฐ์ ์๋กญ๊ฒ ๋ณ์๋ก ํ ๋นํ๋ ๊ฒ์!
        list_file.delete(index)

# ์ ์ฒด ์ญ์ 
def delAll_file():
    list_file.delete(0,END) # list_file ์ด ์ํธ๋ฆฌ๋ผ๋ฉด (1, END) ํ์คํธ๋ผ๋ฉด (0, END)
    
# ์ ์ฅ ๊ฒฝ๋ก (ํด๋)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '' : # ์ฌ์ฉ์๊ฐ ์ทจ์๋ฅผ ๋๋ฅผ ๋ '' ๋ ๋น ๋ฌธ์์ด์ ์๋ฏธํจ
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected) # ์ธ์ํธ ํ  ๋ ์ด๋ ์์น์ ๋์ง๋ ๊ธฐ์ฌํด์ผํจ
    

# ์ด๋ฏธ์ง ํตํฉ
def merge_image():

    try:
        # ๊ฐ๋ก๋์ด
        img_width = cmb_width.get()
        if img_width == "780(๊ถ์ฅ)":
            img_width = 780 # -1 ์ผ ๋๋ ์๋ณธ ํฌ๊ธฐ ์ ์ง
        else:
            img_width = 1440
        
        # ๊ฐ๊ฒฉ
        img_space = cmb_space.get()
        if img_space == "์ข๊ฒ":
            img_space = 30
        elif img_space == "๋ณดํต":
            img_space = 60
        elif img_space == "๋๊ฒ":
            img_space = 90
        else:
            img_space = 0

        # ํฌ๋งท
        img_format = cmb_format.get().lower() # png, jpg ๊ฐ์ ์๋ฌธ์๋ก ๋ณ๊ฒฝ

        images = [Image.open(x) for x in list_file.get(0, END)] # ์ด๋ฏธ์ง ๋ถ๋ฌ์ค๊ธฐ
        # ์ด๋ฏธ์ง ์ฌ์ด์ฆ ๋ฆฌ์คํธ์ ๋ฃ์ด์ ์ฒ๋ฆฌ
        image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]

        # ๊ณ์ฐ์
        # 100 * 60 ์ด๋ฏธ์ง > ๊ฐ๋ก๋ฅผ 80์ผ๋ก ์ค์ด๋ฉด ๋์ด๋ ๋ณ๊ฒฝ๋์ด์ผ ํจ
        # ์๋ณธ(๊ฐ๋ก) : ์๋ณธ(์ธ๋ก) = ๋ณ๊ฒฝ(๊ฐ๋ก) : ๋ณ๊ฒฝ(์ธ๋ก)
        # ์๋ณธ(๊ฐ๋ก)*๋ณ๊ฒฝ(์ธ๋ก) = ์๋ณธ(์ธ๋ก)*๋ณ๊ฒฝ(๊ฐ๋ก)

        
        widths, heights = zip(*(image_sizes))
        # size -> size[0] : width, size[1] : height
        # x_widths = [x.size[0] for x in images]
        # heights = [x.size[1] for x in images]


        # ์ต๋ ๋์ด, ์ ์ฒด ๋์ด ๊ตฌํ๊ธฐ
        max_width, total_height = max(widths), sum(heights)
        # ์ค์ผ์น๋ถ ์ค๋น
        if img_space > 0:
            total_height += (img_space * (len(images)-1))

        result_img = Image.new("RGB",(max_width, total_height),(255,255,255)) # ๋ฐฐ๊ฒฝ ํฐ์
        y_offset = 0 # y ์์น ์ ๋ณด
        x_offset = 0
        # for img in images:
        #     result_img.paste(img, (0,y_offset))
        #     y_offset += img.size[1] # height ๊ฐ ๋งํผ ๋ํด์ค
        for idx, img in enumerate(images):
            # width ๊ฐ ์๋ณธ์ด ์๋ ๊ฒฝ์ฐ์๋ ๋ฆฌ์ฌ์ด์ฆ ํ์
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (x_offset, y_offset))
            y_offset += (img.size[1] + img_space) # height ๊ฐ + ์ฌ์ฉ์๊ฐ ์ง์ ํ ๊ฐ๊ฒฉ

            progress = (idx + 1) / len(images) * 100 # ์ค์  ํผ์ผํธ ์ ๋ณด๋ฅผ ๊ณ์ฐํจ , 1์ ๋ํ๋ ์ด์ ๋ ์ธ๋ฑ์ค๊ฐ 0๋ถํฐ ์์ํ๋ฏ๋ก 1๋ถํฐ ์์ํ  ์ ์๋๋ก ํ๊ธฐ ์ํจ(0 ์ ๋๋ ์ง์ง ์์ผ๋ฏ๋ก)
            p_var.set(progress)
            progress_bar.update()



        # ํฌ๋งท ์ต์ ์ฒ๋ฆฌ
        curr_time = time.strftime("_%y%m%d_%H%M%S")
        file_name = "MergeImage"+curr_time+"."+img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path) # save ์ ์ฅ () ์์ ์ ์ฅ๊ฒฝ๋ก
        msgbox.showinfo("์๋ฆผ", "์ด๋ฏธ์ง ํฉ์น๊ธฐ ์๋ฃ!")
    except Exception as err:
        msgbox.showerror("์๋ฌ", err)

# ์์
def start():
    # ๊ฐ ์ต์ ๊ฐ์ ํ์ธ
    
    # ํ์ผ์ด ์๋์ง ํ์ธ
    if list_file.size() == 0: 
        msgbox.showwarning("๊ฒฝ๊ณ ", "์ด๋ฏธ์ง ํ์ผ์ด ๋ฃ์ด์ฃผ์ธ์!")
        return # ํจ์๋ฅผ ๋น ์ ธ๋์ด

    # ์ ์ฅ๊ฒฝ๋ก ํ์ธ
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("๊ฒฝ๊ณ ", "์ ์ฅ ๊ฒฝ๋ก๋ฅผ ์ ํํ์ธ์!")

    merge_image()

# ํ์ผ ํ๋ ์ (ํ์ผ ์ถ๊ฐ, ์ ํ ์ญ์  + ์ ์ฒด ์ญ์ )
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # x๋ ํ ์ ๋ปํจ

btn_add_file = Button(file_frame, padx=5, pady=5, width=12,text="ํ์ผ์ถ๊ฐ", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12,text="์ ํ์ญ์ ", command=del_file)
btn_del_file.pack(side="right")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12,text="์ ์ฒด์ญ์ ", command=delAll_file)
btn_del_file.pack(side="right")



# ๋ฆฌ์คํธ ํ๋ ์
list_frame = LabelFrame(root, text="ํ์ผ๋ชฉ๋ก")
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# ์ ์ฅ ๊ฒฝ๋ก ํ๋ ์
path_frame = LabelFrame(root, text="์ ์ฅ๊ฒฝ๋ก")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # x ๋ ํ์ ๋ปํจ // ipady : ์ํธ๋ฆฌ ์์ญ ํฌ๊ธฐ

btn_dest_path = Button(path_frame, text="์ฐพ์๋ณด๊ธฐ", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# ์ต์ ํ๋ ์
frame_option = LabelFrame(root, text="์ต์")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. ๊ฐ๋ก ๋์ด
# ๊ฐ๋ก ๋์ด ๋ ์ด๋ธ
lbl_width = Label(frame_option, text="๊ฐ๋ก๋์ด", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# ๊ฐ๋ก ๋์ด ์ฝค๋ณด
opt_width = ["780(๊ถ์ฅ)", "1440(๊ณ ํ์ง)"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)


# 2. ๊ฐ๊ฒฉ ์ต์
# ๊ฐ๋ก ๋์ด ๋ ์ด๋ธ
lbl_space = Label(frame_option, text="์ํ๊ฐ๊ฒฉ", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# ๊ฐ๋ก ๋์ด ์ฝค๋ณด
opt_space = ["์์", "์ข๊ฒ", "๋ณดํต", "๋๊ฒ"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. ํ์ผ ํฌ๋งท
# ๊ฐ๋ก ๋์ด ๋ ์ด๋ธ
lbl_format = Label(frame_option, text="ํฌ๋งท", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# ๊ฐ๋ก ๋์ด ์ฝค๋ณด
opt_format = ["PNG", "JPG"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


# ์งํ ์ํฉ ํ๋ก๊ทธ๋ ์ค ๋ฐ
frame_progress = LabelFrame(root, text="์งํ์ํฉ")
frame_progress.pack(fill="x", padx=5, pady=5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# ์คํ ํ๋ ์

frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="๋ซ๊ธฐ", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="์์", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5) # ๊ฐ์ ์ฌ์ด๋์ธ ๊ฒฝ์ฐ ๋์ค์ ์๋๊ฒ ์์ฐจ์ ์ผ๋ก ๋ถ๊ฒ ๋จ.


root.resizable(False, False)
root.mainloop() 