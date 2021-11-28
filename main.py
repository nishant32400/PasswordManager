from tkinter import *  # * imports classes not methods
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list1 = [choice(letters) for _ in range(randint(8, 10))]
    password_list2 = [choice(symbols) for _ in range(randint(2, 4))]
    password_list3 = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)
    password = "".join(password_list)  # For joining lists, dictionary, tuples we can use "".join() function.

    # password = ""
    # for char in password_list:
    #   password += char

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Using pyperclip--> generated password automatically copied to clipboard and can be
    # used straight away.
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()  # Can't directly access website_entry we have to first create a variable and then
    # use it
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="prompt", message="don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="website",
                                       message=f"details entered- \nEmail:{email} \nWebsite:{website} \npassword:{password} \nis it ok to save?")  # it returns a boolean
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)  # For deleting use full file name instead of variable name
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password_generator")
window.config(pady=20, padx=20, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
lock_image = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=lock_image)  # positions(100,100)
# canvas.create_text(100, 100, text="hey you")  # positions(100,100)
canvas.grid(column=1, row=0)

# Website Entry and Website label
label1 = Label(text="Website: ", bg=YELLOW)
label1.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()  # move the cursor to the designated label
website_entry.grid(column=1, row=1)

# Email Entry and Email label
label2 = Label(text="Email/Username: ", bg=YELLOW)
label2.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "nishant32400@gmail.com")  # insert method will insert a string at location specified in the entry
email_entry.grid(column=1, row=2)

# Password Entry  and Password label and generate password button
label3 = Label(text="Password", bg=YELLOW)
label3.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

genpass_button = Button(text="Generate Password", command=generate_password)
genpass_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4)

window.mainloop()
