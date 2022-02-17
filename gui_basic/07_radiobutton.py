from tkinter import *

root = Tk()
root.title("GUI") # 제목
root.geometry("640x480") # 가로 * 세로

Label(root, text="메뉴를 선택하세요.").pack()

# Radiobutton : 지정된 값 중 한 가지만 선택 가능
burger_var = IntVar() # 모든 햄버거 종류 값(value)을 burger_var에 Int형으로 저장
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요.").pack()

drink_var = StringVar() # 모든 음료수 종류 값(value)을 drink_var에 String형으로 저장
btn_drink1 = Radiobutton(root, text="콜라", value='콜라', variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value='사이다', variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value='환타', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()
