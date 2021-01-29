from tkinter import *
import mysql.connector
from tkinter import messagebox 
import smtplib
import random

window = Tk()
window.geometry("500x200")
window.title("hi")

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="15061212", database="shashank"
)
my_ = mydb.cursor()

def signup():
    new = Tk()
    new.title("shashank")
    window.destroy()
    username_e = Entry(new)
    email_e = Entry(new)
    password_e = Entry(new,show = "*")
    repassword_e = Entry(new,show = "*")
    Label(new,text ='username 👉' ).grid(row = 1,column = 1)
    Label(new,text = 'email 👉').grid(row = 2, column = 1)
    Label(new,text = 'password 👉').grid(row = 3, column = 1)
    Label(new,text = 're-enter password 👉').grid(row = 4, column =1 )
    my_.execute('select * from signin_forms')
    def submit():
        username = username_e.get()
        email = email_e.get()
        password = password_e.get()
        repassword = repassword_e.get()
        for db in my_:
            for i in db :
                if i == username :
                    messagebox.showwarning('username','username not avalible')
                    king = Tk()
                    Label(king , text = 'please restart the process').grid()
                    new.destroy()
                    king.mainloop()
                    break
                elif i == email :
                    messagebox.showwarning("email", "Email is already used please use another email")
                    king = Tk()
                    Label(king , text = 'please restart the process').grid()
                    new.destroy()
                    king.mainloop()
                    break
                elif password != repassword :
                    messagebox.showerror("password", "passwords are not mathing")
                    king = Tk()
                    Label(king , text = 'please restart the process').grid()
                    new.destroy()
                    king.mainloop()
                    break
                else:
                    my_.execute("insert into signin_forms (name,email,password) values (%s, %s, %s)",(username,email,password))
                    username_e.delete(0,'end')
                    email_e.delete(0,'end')
                    password_e.delete(0,'end')
                    repassword_e.delete(0,'end')
                    messagebox.showinfo("account", "account has been created sucssesfully") 
                    root = Tk()
                    new.destroy()
                    root.title("shashank")
                    root.mainloop()
                    mydb.commit()
                    break
    submit_b = Button(new, text="submit",command = submit)
    submit_b.grid(row = 5, column = 2)
    username_e.grid(row = 1 ,column = 2)
    email_e.grid(row = 2, column =2 )
    password_e.grid(row = 3, column = 2)
    repassword_e.grid(row = 4, column = 2)
    new.mainloop()


def login():
    new = Tk()
    window.destroy()
    Label(new, text= 'username👉').grid(row = 1,column = 1)
    Label(new, text= 'password👉').grid(row = 2,column = 1)
    username_e = Entry(new)
    password_e = Entry(new, show = "*")
    def forg():
        z = str(random.randint(10000,99999))
        new_w = Tk()
        new.destroy()
        email_e = Entry(new_w)
        email_e.grid()
        def check():
            new_k = Tk()
            new_w.destroy()
            code_e = Entry(new_k, textvariable = IntVar())
            code_e.grid()
            def Submit():
                code = code_e.get()
                if z == code :
                    print('hi')
                else:
                    print("bye")
            submit = Button(new_k, text = 'submit',command = Submit)
            submit.grid()
        def sendEmail():
            email = email_e.get()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('iamshashankpeddi@gmail.com', 'Vicky@1506')
            server.sendmail('iamshashankpeddi@gmail.com', email, f"your verification code is{z}")
            server.close()
            check()
        c = Button(new_w,text = 'send code',command = sendEmail)
        c.grid()
        new_w.mainloop()
    forget = Button(new , text = 'forget password? ',bd = 0,command = forg)
    forget.grid(row = 4,column = 3)
    my_.execute("SELECT * FROM shashank.signin_forms")
    def sign_in():
        username = username_e.get()
        password = password_e.get()
        for db in my_:
            c = (list(db))
            if c[0] == username :
                if c[2] != password :
                    messagebox.showerror("password", "email or password is incorrect !")
                    password_e.delete(0,'end')
                else :
                    root = Tk()
                    new.destroy()
                    messagebox.showinfo("login", "login succsessful")
                    root.mainloop()
            else:
                pass
    sign = Button(new, text="sign in", command = sign_in)
    username_e.grid(row = 1,column = 2)
    password_e.grid(row = 2,column = 2)
    sign.grid(row = 3,column = 2)


up = Button(window, text="Signup", command=signup)
log = Button(window, text="login", command=login)
up.grid(row = 4,column = 5,padx = 100, pady = 90)
log.grid(row = 4,column = 1,padx = 100, pady = 10)

mydb.commit()
window.mainloop()