from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    password = password_input.get()
    email = email_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Website', message = "Hmmm... There' s something wrong with your input. "
                                                       "Please try again.")
    else:
        is_ok = messagebox.askokcancel(title='Website', message=f"This are the detail entered:\n"
                                                                f"Email: {email}\nPassword: {password}\n "
                                                                f"Is it okay to save?")

    if is_ok:
        with open ("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady=20, bg='white')

canvas = Canvas(width=200 ,height=200, bg = 'white', highlightthickness=0 )
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img, )
canvas.grid(column = 1, row = 0)

website_label = Label(text = 'Website:', bg = 'white')
website_label.grid(column = 0, row = 1)

website_input = Entry(width=50)
website_input.grid(column = 1,  row = 1, columnspan = 2)

email_label = Label(text = 'Email/Username:', bg = 'white')
email_label.grid(column = 0, row = 2)

email_input = Entry(width = 50)
email_input.grid(column = 1,  row = 2, columnspan = 2)
email_input.insert(END, 'your@email.com')

password_label = Label(text = 'Password:', bg = 'white')
password_label.grid(column = 0, row = 3)

password_input = Entry(width = 30)
password_input.grid(column = 1, row = 3)

generate_password = Button(text = 'Generate Password', command=generate_password)
generate_password.grid(column = 2, row = 3)

add_button = Button(text = 'Add', width = 45, command = save)
add_button.grid(column = 1, row = 4, columnspan = 2)

window.mainloop()