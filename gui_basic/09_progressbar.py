import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI") # 제목
root.geometry("640x480") # 가로 * 세로

# ttk.Progressbar : 다운로드 진행 상황을 보여줌

# mode="indeterminate" : 언제 끝날지 모르는 다운로드 시에 사용
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 정수와 소수 모두 표시
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101): # 0 ~ 100
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progressbar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()
root.mainloop()
