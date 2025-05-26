import math
from tkinter import *
#------------------------------ CONSTANTS ------------------------------#
YELLOW = "#FFF1D5"
GREEN = "#90C67C"
work_min = 1
short_break_min = 2
long_break_min = 5
reps = 0
timer = None

#------------------------------ TIMER RESET ------------------------------#

def reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
#------------------------------ TIMER MECANHISM ------------------------------#

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_min * 60)
        title_label.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(short_break_min * 60)
        title_label.config(text="Short Break")
    else:
        count_down(work_min * 60)
        title_label.config(text="Work")
        check_marks = "✔" * (math.floor(reps/2))
        check_mark_label.config(text=check_marks)  

#------------------------------ COUNTDOWN MECHANISM ------------------------------#
def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        

#------------------------------ UI SETUP ------------------------------#

window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100,pady = 50, bg= YELLOW)

canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text= "00:00", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 35, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start",font=("arial", 10, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",font=("arial", 10, "bold"))
reset_button.grid(column=2, row=2)

check_mark_label = Label(fg=GREEN, bg=YELLOW,font=("Courier", 10, "bold"))
check_mark_label.grid(column=1, row=3)

start_button.config(text="Start",highlightthickness=0,command=start_timer)
reset_button.config(text="Reset",highlightthickness=0,command=reset)
window.mainloop()