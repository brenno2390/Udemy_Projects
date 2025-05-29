import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.geometry("450x380")
window.config(padx=20, pady=20)

canva = tk.Canvas(width=200, height=200,highlightthickness=0)
canva.grid(row=0, column=0)
logo_image = tk.PhotoImage(file="logo.png")
logo_label = canva.create_image(100,100,image=logo_image)
canva.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = tk.Entry(width=35)
website_entry.grid(row = 1, column = 1, columnspan=2,sticky="w")
website_entry.focus()

username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2,column=0)
username_entry = tk.Entry(width=35)
username_entry.grid(row = 2, column = 1, columnspan=2, sticky="w")
username_entry.insert(0, "brennoconzatti13@gmail.com")

password_label = tk.Label(text="Password:")
password_label.grid(row=3,column=0)
password_entry = tk.Entry(width=28)
password_entry.grid(row=3, column=1, sticky="w")

generation_button = tk.Button(text="Generate Password")
generation_button.grid(row=3, column=2, sticky="w")

add_button = tk.Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")



window.mainloop()


