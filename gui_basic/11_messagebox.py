from distutils.log import error
import tkinter.messagebox as msgbox
from tkinter import *
from urllib import response

root = Tk()
root.title("GUI") # 제목
root.geometry("640x480") # 가로 * 세로

# 기차 예매 시스템이라고 가정

# 정보 표시
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

# 경고 표시
def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

# 오류 표시
def err():
    msgbox.showerror("오류", "결제 오류가 발생했습니다.")

# 확인 / 취소 표시 (확인 : 1, True), (취소 : 그 외, else)
def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아 동반 좌석입니다. 예매하시겠습니까?")

# 다시 시도 / 취소 표시 (다시 시도 : 1, True), (취소 : 그 외, else)
def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

# 예 / 아니요 표시 (예 : 1, True), (아니요 : 0, False)
def yesno():
    msgbox.askyesno("예 / 아니오", "결제를 하시겠습니까?")

# 예 / 아니오 / 취소 표시 (예 : 1, True), (아니요 : 0, False), (취소 : 그 외, else)
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료 하시겠습니까?")
    print("응답 :", response) # True, False, None -> 예 1, 아니오 0, 그 외
    
    if response == 1: # 예
        print("예")
    elif response == 0: # 아니요
        print("아니요")
    else: # 취소
        print("취소")
    

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=err, text="오류").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()
