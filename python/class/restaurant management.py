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
    sheet[f'e{num}'] = name
    sheet[f'a{num}'] = starters
    sheet[f'b{num}'] = maincourse
    sheet[f'c{num}'] = deserts
    sheet[f'd{num}'] = drinks

    name_e.delete(0,'end')
    starter_E.delete(0,'end')
    deserts_E.delete(0,'end')
    drinks_E.delete(0,'end')
    maincourse_E.delete(0,'end')
    wb.save('Book2.xlsx')
submit = Button(root,text = 'submit', command = Submit)

name_D.grid(row = 1 , column = 1)
starter_D.grid(row =2  , column = 1)
maincourse_D.grid(row = 3 , column = 1)
drinks_D.grid(row = 4 , column =1 )
deserts_D.grid(row = 5  , column = 1)
submit.grid(row = 6 , column =2)


name_e.grid(row = 1, column =2 )
starter_E.grid(row = 2, column =2 )
maincourse_E.grid(row = 3, column = 2 )
drinks_E.grid(row = 4, column = 2 )
deserts_E.grid(row = 5, column = 2 )


root.mainloop()
