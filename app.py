from tkinter import *
import sqlite3

conn = sqlite3.connect(".\words.db")
c = conn.cursor()

win = Tk()

win.title("單字測驗系統")
win.geometry("800x500")
win.configure(bg="#444444")


def word_in():
    x = en_eng.get()
    y = en_chi.get()
    if x != "" and y != "":
        vaules = [x,y]
        c.execute("INSERT INTO word_list VALUES (?,?)",vaules)
        conn.commit()
    else :
        print("Can't be null")

def generate():
    global rows
    c.execute("SELECT * FROM word_list ORDER BY random() LIMIT 1")
    rows = c.fetchall()
    word_lb.config(text=rows[0][1])
    result_lb.config(text="-")
    
def send():
    ans = en_ans.get()
    if ans == rows[0][0] :
        result_lb.config(text="correct!")
    else: 
        result_lb.config(text="nah.Try again!")       

def del_word():
    word_name = del_word.get()
    c.execute("DELETE FROM word_list WHERE english = (?)",word_name)
    conn.commit()

def show_all():
    c.execute("SELECT * FROM word_list")
    rows = c.fetchall()
    all_word_lb.config(text=rows)
def close_all():
    all_word_lb.config(text="")
             
header_lb = Label(text='WORD TEST',bg="#444444",fg="#9400D3")
header_lb.config(font="Unispace 32")
header_lb.pack()

#輸入
word_in_eng = Label(text='Enter english:',bg="#444444",fg="#9400D3")
word_in_eng.config(font="Unispace 24")
word_in_eng.pack()

en_eng = Entry()
en_eng.pack()

word_in_eng = Label(text='Enter chinese:',bg="#444444",fg="#9400D3")
word_in_eng.config(font="Unispace 24")
word_in_eng.pack()

en_chi = Entry()
en_chi.pack()

btn_save = Button(text="SAVE",command=word_in)
btn_save.config(font="Unispace 20")
btn_save.pack()

btn_generate = Button(text="generate",command=generate)
btn_generate.config(font="Unispace 20")
btn_generate.pack()

#輸出
word_lb = Label(text="-",bg="#444444",fg="white")
word_lb.config(font="Unispace 16")
word_lb.pack()

en_ans = Entry()
en_ans.pack()

btn_ans = Button(text="Send answer",command=send) 
btn_ans.config(font="Unispace 20")
btn_ans.pack()

result_lb = Label(text="-",bg="#444444",fg="white")
result_lb.config(font="Unispace 16")
result_lb.pack()

#刪除單字
del_word = Entry()
del_word.pack()

btn_del = Button(text="delete",command=del_word)
btn_del.pack()

#檢視所有單字
btn_show_all = Button(text="Show all words",command=show_all)
btn_show_all.pack()

btn_close_all = Button(text="Closes",command=close_all)
btn_close_all.pack()

all_word_lb = Label(text="",bg="#444444",fg="gray")
all_word_lb.config(font="Unispace 12")
all_word_lb.pack()

win.mainloop()
