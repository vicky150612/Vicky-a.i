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
                    print('username not avalible')
                else :
                    None

    repassword_e = Entry(root, text="re-enter password")
    submit_b = Button(root, text="submit",command = submit)
    submit_b.grid()
    username_e.grid()
    email_e.grid()
    password_e.grid()
    repassword_e.grid()
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
    username_e.grid()
    password_e.grid()
    sign.grid()


up = Button(root, text="Signup", command=signup)
si = Button(root, text="Signin", command=signin)
up.grid()
si.grid()

mydb.commit()
root.mainloop()