import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
database="DatabaseVerifica",
)

mycursor = mydb.cursor()


try:

    selectAnno = int(input("Qual è l'anno di uscita dei videogiochi che vuoi vedere?: "))
    

    mycursor.execute("USE DatabaseVerifica")
    sql = "SELECT * FROM Videogiochi WHERE Anno = %s"
    mycursor.execute(sql, (selectAnno,))
    myresult = mycursor.fetchall()



        
except ValueError:
   
    print("Errore: Valore non valido. Riprova con un anno valido.")
