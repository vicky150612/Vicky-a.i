from tkinter import *
from tkinter import ttk
from openpyxl import *

root = Tk()
root.title("my_restrant")

wb = load_workbook('Book2.xlsx')
sheet = wb.active

name_D = Label(root,text = 'Name : ')
starter_D = Label(root,text = 'starter : ')
maincourse_D = Label(root,text = 'main course : ')
deserts_D = Label(root,text = 'deserts : ')
drinks_D = Label(root,text = 'drinks : ')

name_e = Entry(root,textvariable = StringVar())
starter_E =ttk.Combobox(root, width = 27, textvariable = StringVar())
maincourse_E =ttk.Combobox(root, width = 27, textvariable = StringVar())
deserts_E =ttk.Combobox(root, width = 27, textvariable = StringVar())
drinks_E =ttk.Combobox(root, width = 27, textvariable = StringVar())

starter_E['values'] = ['manchurian','tandoori']
maincourse_E['values'] = ['Biriyani','chicken']
deserts_E['values'] = ['khaja','ice cream']
drinks_E['values'] = ['sprite','coca-cola']

def Submit():
    name = name_e.get()
    starters = starter_E.get()
    maincourse = maincourse_E.get()
    deserts = deserts_E.get()
    drinks = drinks_E.get()
    
    num = str(sheet.max_row)
    sheet[f'a{num}'] = name
    sheet[f'b{num}'] = starters
    sheet[f'c{num}'] = maincourse
    sheet[f'd{num}'] = deserts
    sheet[f'e{num}'] = drinks

    name_e.delete(0,'end')
    starter_E.delete(0,'end')
    deserts_E.delete(0,'end')
    drinks_E.delete(0,'end')
    maincourse_E.delete(0,'end')
    wb.save('Book2.xlsx')
submit = Button(root,text = 'submit', command = Submit)

name_D.grid()
maincourse_D.grid()
drinks_D.grid()
deserts_D.grid()
starter_D.grid()
submit.grid()


name_e.grid()
starter_E.grid()
maincourse_E.grid()
drinks_E.grid()
deserts_E.grid()


root.mainloop()
