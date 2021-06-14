from tkinter import *
import pandas as pd
import os

print(os.getcwd())

dat = pd.read_excel("./전력용어사전.xls")
print(dat.columns)


def click():
    print("버튼이 클릭되었습니다")
    word = entry.get()
    output.delete(0.0, END)

    try:
        def_word1 = dat.loc[dat['용어'] == word, '용어설명'].values[0]
        def_word2 = dat.loc[dat['용어'] == word, '용어(영문)'].values[0]
        def_word3 = dat.loc[dat['용어'] == word, '비고'].values[0]
    except:
        def_word1 = "단어를 뜻을 찾을 수 없음."

    output.insert(END, def_word1)
    output2.insert(END, def_word2)
    output3.insert(END, def_word3)

window = Tk()
window.title("My Dictionary")

# 01 입력 상자 설명 레이블
label = Label(window, text="원하는 단어 입력 후, 제출 누르기\n")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="gray")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 버튼 추가
btn = Button(window, text="입력", width=5,command=click)
btn.grid(row=1, column=0, sticky=S)

# 04 설명 레이블 - 의미
label2 = Label(window, text="\n용어설명")
label2.grid(row=3, column=0, sticky=W)

output = Text(window, width=50, height=6, wrap=WORD, background="white")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 04 설명 레이블 - 영문
label3 = Label(window, text="용어(영문)")
label3.grid(row=5, column=0, sticky=W)

output2 = Text(window, width=50, height=6, wrap=WORD, background="white")
output2.grid(row=6, column=0, columnspan=2, sticky=W)

# 04 설명 레이블 - 비고
label4 = Label(window, text="비고")
label4.grid(row=7, column=0, sticky=W)

output3 = Text(window, width=50, height=6, wrap=WORD, background="white")
output3.grid(row=8, column=0, columnspan=2, sticky=W)

#메인 반복문 실행
window.mainloop()