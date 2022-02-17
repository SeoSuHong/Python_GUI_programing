from tkinter import *

root = Tk()
root.title("GUI") # 제목
root.geometry("640x480") # 가로 * 세로

# scrollbar와 같이 사용하는 위젯은 한 frame에 넣고 같이 관리
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # fill="y" : 스크롤을 y축으로 늘림

# yscrollcommand=scrollbar.set으로 listbox와 scrollbar를 연결
# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

# scrollbar에도 yview로 listbox와 연결
scrollbar.config(command=listbox.yview)

root.mainloop()
