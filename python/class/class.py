from openpyxl import *
from tkinter import*

root = Tk()

workbook = load_workbook(r"C:\vscode\Book2.xlsx")
sheet = workbook.active
def signup():
    username_e = Entry(root, text = "user name")
    email_e = Entry(root, text = "email")
    password_e = Entry(root, text = "password")
    def submit():
        pass
    repassword_e = Entry(root, text = "re-enter password")
    submit = Button(root, text = "submit")
    submit.pack()
    username_e.pack()
    email_e.pack()
    password_e.pack()
    repassword_e.pack()
    Workbook.save(r"C:\vscode\book.xlsx")
def signin():
    username_e = Entry(root, text = "username ")
    password_e = Entry(root, text = "password")
    def sign_in():
        pass
    sign = Button(root, text = "sign in")
    username_e.pack()
    password_e.pack()
    sign.pack()
    Workbook.save(r"C:\vscode\book.xlsx")
up = Button(root,text = "Signup", command = signup)
si = Button(root,text = "Signin", command = signin)
up.pack()
si.pack()

root.mainloop()