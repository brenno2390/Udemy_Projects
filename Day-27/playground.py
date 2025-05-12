from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Entries
entry = Entry(width=10)
entry.insert(END, string="0")
entry.place(x=100,y=0)

save = 0

label_miles = Label(text="miles") 
label_miles.place(x=150, y=0)
#Labels
label = Label(text=f"is equal to {save} kilometers") 
label.place(x=100, y=30)

#Buttons
def action():
    global save
    save = int(entry.get())
    save = save * 1.60934
    save = round(save, 2)
    print(save)
    label.config(text=f"is equal to {save} kilometers")
    label.place(x=100, y=30)

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.place(x=150, y=80)


window.mainloop()
