from tkinter import *

root = Tk()
root.title("GUI") # 제목
root.geometry("640x480") # 가로 * 세로

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root) # 메뉴를 root에 넣는다.

# File 메뉴
menu_file = Menu(menu, tearoff=0) # menu_file을 만든다.
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator() # 구분선
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file) # Menu에 File을 넣고 File의 menu에 menu_file을 넣는다.

# Edit 메뉴
menu.add_cascade(label="Edit")

# Language 메뉴 (radiobutton을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")

menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 (checkbutton을 통해서 체크)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show Breadcrumbs")
menu_view.add_checkbutton(label="Render Whitespace")
menu_view.add_checkbutton(label="Render Control Characters")

menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)

root.mainloop()
