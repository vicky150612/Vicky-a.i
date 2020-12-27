from datetime import datetime
import pyttsx3
import pywhatkit as kit
from tkinter import *


root = Tk()
root.geometry('500x305')
root.title('A.I')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
count = 0


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


king = Entry(root, textvariable=StringVar())
options = [
    'time',
    'myself',
    'name',
    'youtube',
    'whatsapp',
    'google',
]

f = Label(root, text='name in the box 👉', fg='red')
selected = StringVar()
selected.set(options[0])


def ff():
    e = Label(root, text='command in the box 👉', fg='red')
    d = OptionMenu(root, selected, *options)
    e.grid(column=1, row=2)
    d.grid(column=2, row=2)
    w = Button(root, text='set the command', command=query)
    w.grid(column=2, row=3)


a = Button(root, text='set the name', command=ff)


def query():
    name = king .get()
    command = selected.get()
    if command == 'time':
        now = datetime.today()
        time = now.strftime('%H-%M')
        date = now.strftime('%d/%m/%y')
        day = now.strftime("%A")
        label1 = Label(root, text=f'Time is : {time}'
                                  f'\nDay is : {day}'
                                  f'\nDate is : {date}')
        speak(f'{time} {day} {date}')
        label1.grid(column=0, row=4)
    elif command == 'myself':
        speak(f'your name is {name}')
        speak(f'{name} is so smart')
    elif command == 'name':
        speak(name)
        l1 = Label(root, text=f' I know your name is : {name}')
        l1.grid(column=0, row=5)
    elif command == 'youtube':
        l1 = Label(root, text='please enter what do you want to see')
        e1 = Entry(root)

        def kk():
            video = e1.get()
            kit.playonyt(video)

        b1 = Button(root, text='play the video', command=kk)
        l1.grid(column=0, row=6)
        e1.grid(column=0, row=7)
        b1.grid(column=0, row=8)
    elif command == 'google':
        l1 = Label(root, text='please enter what do you want to search in google in the box')
        e1 = Entry(root)

        def hhh():
            search = e1.get()
            kit.search(search)
        b1 = Button(root, text='search', command=hhh)
        b1.grid(column=0, row=11)
        l1.grid(column=0, row=9)
        e1.grid(column=0, row=10)
    elif command == 'whatsapp':
        e1 = Entry(root)
        e2 = Entry(root)
        l1 = Label(root, text='number of the person 👉 ')
        l2 = Label(root, text='type your message 👉 ')
        today_date = datetime.now()
        time_hor = today_date.hour
        time_min = today_date.minute + 1

        def kkk():

            num = f'{e1.get()}'
            msg = e2.get()
            kit.sendwhatmsg(num, msg, time_hor, time_min)
        b1 = Button(root, text='send', command=kkk)

        b1.grid(column=0, row=14)
        e1.grid(column=1, row=12)
        e2.grid(column=1, row=13)
        l2.grid(column=0, row=13)
        l1.grid(column=0, row=12)


f.grid(column=1, row=1)
king.grid(column=2, row=1)
a.grid(column=2, row=3)
root.mainloop()
