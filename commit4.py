import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)

errore = True
while errore:
    mycursor = mydb.cursor()
    mycursor.execute("USE DatabaseVerifica")
    

    selezionaId = input("Inserisci l'ID del videogioco che vuoi eliminare: ")
    

    sql = "SELECT EXISTS(SELECT 1 FROM Videogiochi WHERE id = %s)"
    mycursor.execute(sql, (selezionaId,))
    exists = mycursor.fetchone()[0]
    
    
