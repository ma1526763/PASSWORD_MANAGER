from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

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
def confirm(title, message):
    return True if messagebox.askokcancel(title=title, message=message) else False
def clear_screen():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
def write_data_to_file(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    clear_screen()
def search_website_info():
    website_name = website_entry.get().title()
    if website_name:
        try:
            with open("data.json") as file:
                file_data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="File Not Found", message=f"\"data.json\" file does not exist")
        except json.decoder.JSONDecodeError:
            messagebox.showinfo(title="Empty File", message=f"\"data.json\" is empty!")
        else:
            try:
                website_data = file_data[website_name]
            except KeyError:
                messagebox.showinfo(title="Website not Found", message=f"No data found for \"{website_name}\"")
            else:
                message = ""
                for data in website_data:
                    message += f"Email:\t\t{data['email']}\nPassword:\t{data['password']}\n\n"
                messagebox.showinfo(title=f"{website_name}", message=message)
                pyperclip.copy(website_data[-1]["password"])
    else:
        messagebox.showinfo(title="Empty", message=f"Please enter website name")


# ADDING DATA TO FILE
def save_data_to_file():
    website = website_entry.get().title().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    if not website or not email or not password:
        messagebox.showinfo("Fail: ", message="Please fill all the fields")
    elif len(password) < 8:
        messagebox.showinfo(title="Short Password", message="Password length must be 8 characters minimum")
    else:
        new_data = {website: [{"email": email, "password": password}]}
        try:
            with open("data.json", "r+") as file:
                data_dict = json.load(file)
                try:
                    website_data = data_dict[website]
                except KeyError:
                    if confirm(title=f"Confirm data for {website}", message=f"Email:\t   {email}\nPassword:  {password}"):
                        data_dict[website] = [{"email": email, "password": password}]
                        # Move the file pointer to the beginning of the file
                        file.seek(0)
                        json.dump(data_dict, file, indent=4)
                        clear_screen()
                else:
                    already_email = False
                    for data in website_data:
                        if data['email'] == email:
                            already_email = True
                            messagebox.showinfo(title=f"Already exists",
                                                message=f"Website with this email already exists.Change website or email")
                    if not already_email:
                        if confirm(title=f"Confirm data for {website}", message=f"Email:\t   {email}\nPassword:  {password}"):
                            data_dict[website].append({"email": email, "password": password})
                            file.seek(0)
                            json.dump(data_dict, file, indent=4)
                            clear_screen()

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            if confirm(title=f"Confirm data for {website}", message=f"email:    {email}\nPassword:  {password}"):
                write_data_to_file(new_data)

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
window.config(padx=80, pady=50, bg="light blue")
canvas = Canvas(width=200, height=189, bg="light blue", highlightbackground="light blue")
img = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=img)
canvas.grid(row=0, column=1, padx=30)

# Website
website_label = Label(text="Website", font=("Arial", 10, "normal"), pady=3, bg="light blue")
website_label.grid(row=1, column=0)
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
search_website_button = Button(text="Search", command=search_website_info)
search_website_button.grid(row=1, column=2, sticky="EW")

# Email
email_label = Label(text="Email/Username:", font=("Arial", 10, "normal"), pady=3, background="light blue")
email_label.grid(row=2, column=0)
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "mega.film199@gmail.com")

# Password
password_label = Label(text="Password:", font=("Arial", 10, "normal"), pady=3, background="light blue")
password_label.grid(row=3, column=0)
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")
password_button = Button(text="Generate Password", command=generate_random_password)
password_button.grid(row=3, column=2, sticky="EW")

# Add Button
add_button = Button(text="Add", command=save_data_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
