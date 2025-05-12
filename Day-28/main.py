from tkinter import *
#------------------------------ CONSTANTS ------------------------------#
YELLOW = "#FFF1D5"
GREEN = "#90C67C"


#------------------------------ TIMER RESET ------------------------------#



#------------------------------ TIMER MECANHISM ------------------------------#

#------------------------------ COUNTDOWN MECHANISM ------------------------------#




#------------------------------ UI SETUP ------------------------------#

window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100,pady = 50, bg= YELLOW)

canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100,130,text= "00:00", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 35, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start",font=("arial", 10, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",font=("arial", 10, "bold"))
reset_button.grid(column=2, row=2)

check_mark_label = Label(text="✔",fg=GREEN, bg=YELLOW,font=("Courier", 10, "bold"))
check_mark_label.grid(column=1, row=3)

window.mainloop()