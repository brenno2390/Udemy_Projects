import tkinter

# Create the main window
window = tkinter.Tk()
window.title("My Tkinter App GUI")
window.geometry("400x200")

my_label = tkinter.Label(window, text="Hello World!")
my_label.pack()

my_label["text"] = "Hello Tkinter!" #1° way to change the text
my_label.config(text="Hello Tkinterrr") #2° way to change the text

def button_click():
    my_label["text"] = "Button clicked!"
    new_text = input.get()
    my_label["text"] = new_text

button = tkinter.Button(text ="Click me", command=button_click)
button.pack()

#entry

input = tkinter.Entry(width=10)
input.pack()
print(input.get()) 
# Run the application
window.mainloop()
