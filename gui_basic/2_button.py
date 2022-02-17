from tkinter import *

root = Tk()
root.title("First GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

# padx= : 글자 양 옆 여백 공간 수치, pady= : 글자 위 아래 여백 공간 수치
# (글자가 커지면 버튼 크기도 커짐)
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# width= : 버튼 너비 수치, height= : 버튼 높이 수치
# (글자가 커져도 글자가 안 보이지 버튼 크기는 그대로)
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

# fg= : 글자 색상 (foreground), bg= : 배경 색상 (background)
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

# 이미지를 통한 버튼
photo = PhotoImage(file="gui_basic/image.png")
btn6 = Button(root, image=photo)
btn6.pack()

# command 속성을 통한 버튼 동작
def btncmd():
    print("버튼이 클릭되었습니다.")

btn7 = Button(root, text="동작 버튼", command=btncmd)
btn7.pack()

root.mainloop()
