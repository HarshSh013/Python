import tkinter
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    passwordentry.delete(0, END)
    password = "".join(password_list)
    passwordentry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website=webentry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry=webentry.get()
    email_entry = emailentry.get()
    password_entry = passwordentry.get()
    newdata={
        website_entry: {
            "email":email_entry,
            "password":password_entry,
        }
    }
    if len(website_entry)==0 or len(email_entry)==0 or len(password_entry)==0:
        messagebox.showerror(title="Try Again",message="Fields are empty!!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry,
                                       message=f"These are your details:\nEmail:{email_entry}\npassword:{password_entry}")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    data=json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(newdata, data_file, indent=4)
            else:
                data.update(newdata)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                webentry.delete(0,END)
                passwordentry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Mangar")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website = Label(text="Website:")
website.grid(column=0, row=1)


webentry = Entry(width=21)
webentry.grid(column=1,row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

emailentry = Entry(width=35)
emailentry.grid(column=1,row=2,columnspan=2)
emailentry.insert(0,"harshsh013@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)

passwordentry = Entry(width=21)
passwordentry.grid(column=1,row=3)

button = Button(text="Generate Password",command=generate_password)
button.grid(column=2,row=3)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

subbutton = Button(text="ADD",width=36, command=save)
subbutton.grid(column=1,row=4,columnspan=2)














window.mainloop()