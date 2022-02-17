from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("Photo Overlap Program")
root.resizable(False, False)

# 파일 추가 함수
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir=r"C:/Users/Seo Su Hong/Desktop/IT/Python/GUI programing") # 최초의 사용자가 지정한 경로를 보여줌

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

# 선택 삭제 함수
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 함수 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합
def marge_image():
    # print(cmb_width.get(), cmb_space.get(), cmb_format.get())
    
    try:
        # 가로넓이
        img_width = cmb_width.get()

        if img_width == "원본유지":
            img_width = -1
        else:
            img_width = int(img_width)
        
        # 간격
        img_space = cmb_space.get()

        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else: # 없음
            img_space = 0
        
        # 포맷
        img_format = cmb_format.get().lower() # JPG, PNG, BMP 값을 받아와서 소문자로 변경

        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈 리스트에 넣어서 하나씩 관리
        image_sizes = [] # [(width1, height1), (width2, height2), ...]
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images] # width 값 변경
        else:
            # 원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        # 계산식
        # 100 * 60 이미지가 있다. -> width를 80으로 줄인다면 height는?
        # (원본 width : 원본 height) = (변경 width : 변경 height)
        # x   : y  = x' : y'(?)   -->   xy'     =   x'y     -->   y' =  x'y / x
        # 100 : 60 = 80 :  ?      -->   100 * ? = 60 * 80   -->   ?  = 4800 / 100

        # 코드에 대입했을 때는?
        # x = width = size[0]
        # y = height = size[1]
        # x' = img_width # 이 값으로 변경해야 함
        # y' = x'y / x = img_width * size[1] / size[0]

        widths, heights = zip(*(image_sizes))

        # 최대 넓이, 전체 높이 구해옴
        max_width, total_height = max(widths), sum(heights)
        
        # 스케치북 준비

        if img_space > 0: # 이미지 간격 옵션
            total_height += (img_space * (len(images) - 1))
        
        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # 배경 흰색
        y_offset = 0 # y 위치
        
        for idx, img in enumerate(images):
            # width가 원본유지가 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space) # height값 + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100 # 실제 퍼센트 정보를 계산
            p_var.set(progress)
            progressbar.update()
        # 포맷 옵션 처리
        file_name = "First Photo Overlap." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err:
        msgbox.showerror("오류", err)

# 시작 함수
def start():
    # 각 옵션들 값을 확인
    # print(cmb_width.get(), cmb_space.get(), cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 선택하세요.")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요.")
        return

    # 이미지 통합 작업
    marge_image()

# 프레임 작업 #########################################################

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

# 파일 추가 버튼
btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(fill="y", side="right")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # ipady : 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 1-1. 가로 넓이 레이블
lbl_width = Label(option_frame, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 1-2. 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_width, width=8)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 2-1. 간격 옵션 레이블
lbl_space = Label(option_frame, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 2-2. 간격 옵션 콤포
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(option_frame, state="readonly", values=opt_space, width=8)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 3-1. 파일 포맷 레이블
lbl_format = Label(option_frame, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 3-2. 파일 포맷 콤포
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state="readonly", values=opt_format, width=8)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Pogress Bar
progressbar_frame = LabelFrame(root, text="진행상황")
progressbar_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progressbar = ttk.Progressbar(progressbar_frame, maximum=100, variable=p_var)
progressbar.pack(fill="x", padx=5, pady=5)

# 실행 프레임 (시작 버튼, 닫기 버튼)
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

# 닫기 버튼
btn_close = Button(run_frame, text="닫기", padx=5, pady=5, width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

# 시작 버튼
btn_start = Button(run_frame, text="시작", padx=5, pady=5, width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.mainloop()
