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
    
    if not exists:
        print(f"L'ID {selezionaId} non è presente nel database. Riprova.")
    else:

        delete_query = "DELETE FROM Videogiochi WHERE id = %s"
        mycursor.execute(delete_query, (selezionaId,))
        mydb.commit()
        print(f"Il videogioco con ID {selezionaId} è stato eliminato con successo.")
        errore = False 
