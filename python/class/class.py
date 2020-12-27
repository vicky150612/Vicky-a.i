from openpyxl import *
from tkinter import*

root = Tk()

workbook = load_workbook(r"C:\vscode\Book2.xlsx")
sheet = workbook.active
z = Entry(root, textvariable = StringVar)
def submit():
    k = z.get()
    row = sheet.max_row
    sheet.cell(row = row+1, column = 1).value = k
    workbook.save(r"C:\vscode\Book2.xlsx")
    z.delete('0','end')
s = Button(root, text = 'submit', command = submit)
z.pack()
s.pack()
root.mainloop()