import time
import keyboard 
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S") # 현재시간 출력
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # 현재시간을 파일명에 덧붙임

keyboard.add_hotkey("crtl+s", screenshot) # 실행

keyboard.wait("esc") # esc 누를 때까지 수행