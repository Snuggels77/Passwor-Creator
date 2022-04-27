from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

img_file = r"logo.png"
pw_file = r"Data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) 


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Invlid Entry", message="Oops, there are fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Username: {username}\nPassword: {password}\nSave it?")
        
        if is_ok:
            with open(pw_file, 'a') as file:
                file.write(f"{website} | {username} | {password} \n")
                
                website_entry.delete(0, END)
                # username_entry.delete(0, END)
                password_entry.delete(0, END)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
# Canvas
img_photo = PhotoImage(file=img_file)
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img_photo)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus() # Corsor bei Start in dem Feld 

# Username
username_label = Label(text="Email/Username:") 
username_label.grid(column=0, row=2)

username_entry = Entry(width=36)
username_entry.insert(END, "angela@gmail.com") 
username_entry.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", width=13, command=password_generator)
password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=35, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
