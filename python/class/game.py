from tkinter import *
import mysql.connector

root = Tk()


mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="15061212", database="shashank"
)
my_cursor = mydb.cursor()


def signup():
    username_e = Entry(root, text="user")
    email_e = Entry(root, text="email")
    password_e = Entry(root, text="password")

    def submit():
        username = username_e.get()
        email = email_e.get()
        password = password_e.get()
        my_cursor.execute('select name from signin_forms')
        for db in my_cursor:
            for i in db :
                s = i 
                if s == username :
                    print('not avalible')
                else :
                    None

    repassword_e = Entry(root, text="re-enter password")
    submit_b = Button(root, text="submit",command = submit)
    submit_b.pack()
    username_e.pack()
    email_e.pack()
    password_e.pack()
    repassword_e.pack()
    my_cursor.execute(
        "insert into signin_forms (name,email,password) values(%s,%s,%s) ",
        ("shashank", "iamshashank", "1506"),
    )


def signin():
    username_e = Entry(root, text="username ")
    password_e = Entry(root, text="password")

    def sign_in():
        pass

    sign = Button(root, text="sign in")
    username_e.pack()
    password_e.pack()
    sign.pack()


up = Button(root, text="Signup", command=signup)
si = Button(root, text="Signin", command=signin)
up.pack()
si.pack()

mydb.commit()
root.mainloop()