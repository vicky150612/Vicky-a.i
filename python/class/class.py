import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="15061212", database="shashank"
)
my_cursor = mydb.cursor()
my_cursor.execute('select name from signin_forms')
for db in my_cursor:
    for i in db :
        s = i 
        if s == 'shashank' :
            print('no')
        else :
            print('yes')