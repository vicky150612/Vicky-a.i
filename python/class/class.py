import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="15061212", database="shashank"
)
my_cursor = mydb.cursor()
my_cursor.execute(
    "insert into signin_forms (name,email,password) values(%s,%s,%s) ",
    ("shashank", "iamshashank", "1506"),
)
mydb.commit()
