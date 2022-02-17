import keyboard
from PIL import ImageGrab
import time

def screenshot():
    # 2022년 2월 12일 12시 16분 20초 -> _20220212_121620
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # ex) image_20220212_121620.png

keyboard.add_hotkey("f9", screenshot) # 사용자가 F9 키를 누르면 스크린샷 저장

keyboard.wait("esc") # 사용자가 esc 키를 누를 때까지 프로그램 수행
