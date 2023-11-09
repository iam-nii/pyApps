from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

gen_password_list = []

def generate_password():

    # letters
    for _ in range(1, nr_letters + 1):
        gen_password_list.append(random.choice(letters))
    # Symbols
    for _ in range(1, nr_symbols + 1):
        gen_password_list.append(random.choice(symbols))
    # Numbers
    for _ in range(1, nr_numbers + 1):
        gen_password_list.append(random.choice(numbers))

    # Shuffle the list to generate complex password
    random.shuffle(gen_password_list)

    # Create a password string
    gen_password = ""
    for char in gen_password_list:
        gen_password += char

    # Insert the password into the Entry
    initial_pass = password_txt.get()
    print(len(initial_pass))
    if len(initial_pass) > 0:
        password_txt.delete(0, 'end')
        gen_password_list.clear()
    password_txt.insert(0, gen_password)
    pyperclip.copy(gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    password = password_txt.get()
    username_email = user_or_email_txt.get()
    website = website_txt.get()

    data_dict = {
        website:
            {
                "email": username_email,
                "password": password
            }
    }

    if website == "":
        messagebox.showwarning(message="Please enter a website")
    elif password == "":
        messagebox.showwarning(message="Please enter a password")
    elif username_email == "":
        messagebox.showwarning(message="Please enter a a Username/Email")
    else:
        _ok = messagebox.askokcancel(title=website, message=f"These are the details you entered\n"
                                                            f"Email/Username: {username_email}\n"
                                                            f"Password: {password}\n"
                                                            f"Do you want to save these details?")
        if _ok:

            #-------------------------- File Work -------------------------#
            # We are trying to save data to a file.
            # if the file does not exist, create the file and dump the new data
            # if the file exists and contains data, update the data
            try:
                file = open("data.json", mode="r")
            except FileNotFoundError:
                file = open("data.json", mode="w")
                json.dump(data_dict, file, indent=4)
                file.close()
            else:
                # read old data
                new_data = json.load(file)
                file.close()
                # update old data
                new_data.update(data_dict)
                file = open("data.json", mode="w")
                # save the new data to the file
                json.dump(new_data, file, indent=4)
                file.close()
            finally:
                password_txt.delete(0, 'end')
                website_txt.delete(0, 'end')

#----------------------------- SEARCH FOR PASSWORD --------------------------#
def search_for_password():
    website_name = website_txt.get()

    try:
        with open("data.json", mode="r") as file:
            data_dict = json.load(file)

            # Try getting the indicated website
            try:
                web_info = data_dict[website_name]
            except KeyError as message:
                messagebox.showwarning(title="Website not found", message=f"You did not create a password for {message}")
            else:
                user_email = web_info["email"]
                user_password = web_info["password"]

                messagebox.showinfo(website_name, message=f"Email: {user_email}\nPassword: {user_password}\n"
                                                          f"\nPassword copied to clipboard 😁")
                #copy the password to the clipboard
                pyperclip.copy(user_password)
    except FileNotFoundError:
        messagebox.showwarning(title="File not found", message=f"Please try saving a password for {website_name}")




# ---------------------------- UI SETUP ------------------------------- #
# Creating the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, width=500, height=500)

# Creating the canvas
canvas = Canvas(width=200, height=200)
# Getting an image for the canvas
img_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_file)  # To get the center (x and y), we divide the size of the canvas into two
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

user_or_email = Label(text="Username/Email: ")
user_or_email.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# textboxs
website_txt = Entry()
website_txt.config(width=39)
website_txt.focus()
website_txt.grid(row=1, column=1, sticky="EW")

user_or_email_txt = Entry()
user_or_email_txt.config(width=39)
user_or_email_txt.insert(0, "adjeiboyejnr@gmail.com")
user_or_email_txt.grid(row=2, column=1, columnspan=2, sticky="EW")

password_txt = Entry()
password_txt.config(width=21)
password_txt.grid(row=3, column=1, sticky="EW")

# buttons
generate_btn = Button()
generate_btn.config(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2, sticky="EW")

add_btn = Button()
add_btn.config(text="Add", width=35, command=save_to_file)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

search_btn = Button()
search_btn.config(text="Search", command=search_for_password)
search_btn.grid(row=1, column=2, sticky="EW")

mainloop()
