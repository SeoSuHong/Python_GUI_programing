from tkinter import *

root = Tk()
root.title("First GUI")
root.geometry("640x480")

# 레이블 생성
label1 = Label(root, text="안녕하세요")
label1.pack()

# 이미지로 레이블 생성
photo = PhotoImage(file="gui_basic/image.png")
label2 = Label(root, image=photo)
label2.pack()

# 버튼 눌러 레이블, 이미지 바꾸기
def change():
    label1.config(text="또 만나요")

    # 함수 내에서 이미지 바꿀 시 Garbage Collection 때문에 이미지를 전역변수(global)로 바꾸기
    # Garbage Collection : 불필요한 메모리(photo2) 공간 해제
    global photo2
    photo2 = PhotoImage(file="gui_basic/image2.png")
    label2.config(image=photo2)

btn = Button(root, text="버튼", command=change)
btn.pack()

root.mainloop()
