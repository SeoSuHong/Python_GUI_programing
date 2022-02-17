from tkinter import *

root = Tk()
root.title("GUI") # 제목
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5) # 여러 줄 입력 가능
txt.pack()
txt.insert(END, "글자를 입력하세요.") # 기본값

e = Entry(root, width=30) # 한 줄 입력 ex)아이디, 닉네임
e.pack()
e.insert(0, "한 줄만 입력하세요.") # 기본값

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1(라인).0(인덱스)부터 END까지 가져오기(처음부터 끝까지)
    print(e.get())

    # 내용 삭제
    txt.delete(1.0, END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
