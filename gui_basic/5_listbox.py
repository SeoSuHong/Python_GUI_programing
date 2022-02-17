from tkinter import *

root = Tk()
root.title("GUI") # 제목
root.geometry("640x480") # 가로 * 세로

# selectmode : 모드 선택 (extended : 중복 선택 가능, single : 하나만 선택 가능 ...)
# height : 지정된 숫자만큼만 list 창이 보임 (0 입력 시 list 전부 보임)
listbox = Listbox(root, selectmode="extended", height=0)

listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2 ,"바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤에 항목을 삭제

    # 갯수 확인
    print("리스트에는", listbox.size(), "개가 있습니다.")

    # 항목 확인 (시작 idx, 끝 idx)
    print("1번째부터 3번째까지의 항목 :", listbox.get(0, 2))

    # 선택된 항목 확인 ( idx 위치로 반환 (0, 1, 2))
    print("선택된 항목 :", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
