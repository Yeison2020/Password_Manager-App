from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_site_entry.get()
    email = email_entry.get()
    password = pass_Word_entry.get()
    new_data = {website: {
        "email": email,
         "password": password

    }}


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_site_entry.delete(0, END)
            pass_Word_entry.delete(0, END)
            email_entry.delete(0, END)
    # ---------------------------- Searchning inside of the file------------------------------- #
def search_password():
    website = web_site_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message= "Data Not found ")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(f"Website", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title = "No File found ", message= "Please you have not saved data under this website")











# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)
    pass_Word_entry.insert(0, password)
    pyperclip.copy(password)
    


# ---------------------------- UI SETUP ------------------------------- #

# Step 1
window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)
# window.minsize(300,200)

# Step 2

canvas = Canvas(width=200, height=200, bg="white")
image_product = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_product)
canvas.grid(row=0, column=1)

# Step 3


web_site_label = Label(text="Website:", font=("Arial", 8, "normal"))
web_site_label.grid(column=0, row=1)

email_label = Label(text="Email/ Username:", font=("Arial", 8, "normal"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 8, "normal"))
password_label.grid(column=0, row=3)

# Step 4

web_site_entry = Entry(width=35)
# web_site_entry.insert(text=("Ye2019892@gmail.com"))
web_site_entry.focus()
web_site_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
# email_entry.insert(0)
email_entry.grid(column=1, row=2, columnspan=2)

pass_Word_entry = Entry(width=26)
pass_Word_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=36, command=save)

add_button.grid(column=1, row=4)


search_button = Button(text="Search", padx=32, command=search_password)
search_button.grid(column=2, row=1, columnspan=4, pady=8)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#
#
# # Password Generator Project
# def generate_password():
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#     password_letter = [choice(letters) for _ in range(randint(8, 10))]
#
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#
#     password_number = [choice(numbers) for _ in range(randint(2, 4))]
#
#     password_list = password_letter + password_symbols + password_number
#     shuffle(password_list)
#
#     password = "".join(password_list)

 


window.mainloop()
