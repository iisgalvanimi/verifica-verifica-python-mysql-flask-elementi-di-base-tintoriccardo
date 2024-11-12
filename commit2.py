import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Videogiochi")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)