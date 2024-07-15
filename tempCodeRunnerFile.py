import random
from tkinter import *
# from tkinter import ttk
import string

def pass_gen():
    user = int(input("Range :- "))
    Length = int(input("Length :- "))
    for i in range(user):
        passwords= []
        for c in range(Length):
            alphabet = random.choice(string.ascii_letters)
            numbers = random.choice(string.punctuation)
            symbols = random.choice(string.digits)
            passwords = passwords.append(alphabet, numbers, symbols)
    return passwords


root = Tk()
root.title("PASSWORD GENERATOR")
# root.geometry("250x200")
btn = Button(root, text="Generate Password", command=pass_gen)
btn.grid(row=4, column=4)
lbl = Label(root, font=("times", 15, "bold"))
lbl.grid(row=4, column=2)
root.mainloop()
