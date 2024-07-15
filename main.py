import random
from tkinter import *
import string

def pass_gen(user, Length):
    all_passwords = []
    for i in range(user):
        password = []
        for c in range(Length):
            alphabet = random.choice(string.ascii_letters)
            numbers = random.choice(string.digits)
            symbols = random.choice(string.punctuation)
            password.append(alphabet)
            password.append(numbers)
            password.append(symbols)
        all_passwords.append(''.join(password))
    return all_passwords

def show_passwords():
    try:
        user = int(entry_user.get())
        Length = int(entry_length.get())
        passwords = pass_gen(user, Length)
        lbl.config(text="\n".join(passwords))
    except ValueError:
        lbl.config(text="Please enter valid numbers")

root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry("400x300")

Label(root, text="Range:").grid(row=0, column=0, padx=10, pady=10)
entry_user = Entry(root)
entry_user.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Length:").grid(row=1, column=0, padx=10, pady=10)
entry_length = Entry(root)
entry_length.grid(row=1, column=1, padx=10, pady=10)

btn = Button(root, text="Generate Password", command=show_passwords)
btn.grid(row=2, column=1, pady=10)

lbl = Label(root, font=("times", 10), justify=CENTER)
lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()



# def pass_gen(user, Length):
 
#     all_passwords = []
#     for i in range(user):
#         password = []
#         for c in range(Length):
#             alphabet = random.choice(string.ascii_letters)
#             numbers = random.choice(string.digits)
#             symbols = random.choice(string.punctuation)
#             password.append(alphabet)
#             password.append(numbers)
#             password.append(symbols)
#         all_passwords.append(''.join(password))
#     return all_passwords

# root = Tk()
# root.title("PASSWORD GENERATOR")
# root.geometry("250x200")

# def show_passwords():
#     user = int(input("Range :- "))
#     Length = int(input("Length :- "))
#     passwords = pass_gen()
#     lbl.config(text="\n".join(passwords))

# btn = Button(root, text="Generate Password", command=show_passwords)
# # btn.grid(row=0, column=0)
# btn.grid(row=2, column=2)
# lbl = Label(root, font=("times", 15))
# lbl.grid(row=4, column=2)

# root.mainloop()