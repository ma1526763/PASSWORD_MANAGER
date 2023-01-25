from tkinter import *
import random
from tkinter import messagebox
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# def automatic_password_to_clipboard(password):
#     clip = Tk()
#     clip.withdraw()
#     clip.clipboard_clear()
#     clip.clipboard_append(password)
#     clip.destroy()

# ADDING DATA TO FILE
def add_data_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website.strip() and email.strip() and password.strip():
        ok = messagebox.askokcancel(title="Confirm", message=f"Website:    {website}\n"
                                                             f"Password:  {password}")
        if ok:
            with open("data.text", "a") as file:
                file.write(f"{website.title()}\t|\t{email}\t|\t{password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo("Fail: ", message="Please fill all the fields")

# RANDOM PASSWORD GENERATOR
def generate_random_password():
    if password_entry.get():
        password_entry.delete(0, END)
    random_password = [random.choice(letters) for _ in range(8)] + [random.choice(numbers) for _ in range(4)] + [
        random.choice(symbols) for _ in range(2)]
    random_password = "".join(list(set(random_password)))
    password_entry.insert(0, random_password)
    # automatic_password_to_clipboard(random_password)
    pyperclip.copy(random_password)

# APP GUI
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=50)
canvas = Canvas(width=200, height=189)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=img)
canvas.grid(row=0, column=1, padx=30)

# Website
website_label = Label(text="Website", font=("Arial", 10, "normal"), pady=3)
website_label.grid(row=1, column=0)
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

# Email
email_label = Label(text="Email/Username:", font=("Arial", 10, "normal"), pady=3)
email_label.grid(row=2, column=0)
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "mega.film199@gmail.com")

# Password
password_label = Label(text="Password:", font=("Arial", 10, "normal"), pady=3)
password_label.grid(row=3, column=0)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1, sticky="EW")
password_button = Button(text="Generate Password", command=generate_random_password)
password_button.grid(row=3, column=2, sticky="EW")

# Add Button
add_button = Button(text="Add", width=44, pady=2, command=add_data_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
