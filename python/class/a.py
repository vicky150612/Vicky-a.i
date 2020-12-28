from openpyxl import *
wb = load_workbook(r"C:\vscode\Book2.xlsx")
sheet = wb.active
sheet['A1'] = 'shashank'
wb.save(r"C:\vscode\Book1.xlsx")
