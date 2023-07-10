import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for num in range(nr_letters)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for num in range(nr_symbols)]

    password_list = password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get().strip()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} found")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(
            title="OOPS", message="Please fill all fields.")
    else:
        try:
            file = open("data.json", "r")
        except FileNotFoundError:
            file = open("data.json", "w")
        else:
            existing_data = json.load(file)
            existing_data.update(data)
            file.close()
            with open("data.json", "w") as file:
                json.dump(existing_data, file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(
    file="C:/Users/anshm/Documents/Python Projects/Password Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = tkinter.Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = tkinter.Entry(width=35)
email_entry.insert(0, "<EMAIL>")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = tkinter.Button(
    text="Generate Password", width=14, command=generate_password)
password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
