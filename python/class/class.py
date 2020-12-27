from openpyxl import *
from tkinter import*

root = Tk()

workbook = load_workbook(r"C:\vscode\Book2.xlsx")
sheet = workbook.active
def signin():
    username_e = Entry(root, text = "user name")
    email_e = Entry(root, text = "email")
    password_e = Entry(root, text = "")
    repassword_e = Entry(root, text = "")
    submit = Button(root, text = "")
def signup():
    username_e = Entry(root, text = "")
    password_e = Entry(root, text = "")
    sign = Button(root, text = "")
up = Button(root,text = "Signup", command = signup)
si = Button(root,text = "Signin", command = signin)

root.mainloop()