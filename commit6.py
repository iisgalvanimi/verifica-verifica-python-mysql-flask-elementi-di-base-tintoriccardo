import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",  
  database="DatabaseVerifica"
)

mycursor = mydb.cursor()


print("""1) INSERIRE UN NUOVO VIDEOGIOCO2) ESTRARRE I DATI DAL DB3) ELIMINARE I DATI DAL DB (specificando l'ID)4) ESTRARRE I DATI DAL DB CON SELECT PARTICOLARE""")
inp = int(input())

if inp == 1:
    print("INSERISCI UN NUOVO VIDEOGIOCO")
    Nome = input("Inserisci il nome del videogioco: ")
    Anno = int(input("Inserisci l'anno di uscita: "))
    Genere = input("Inserisci il genere del videogioco: ")
    Piattaforma = input("Inserisci la piattaforma: ")
    Sviluppatore = input("Inserisci il nome dello sviluppatore: ")
    
    sql = "INSERT INTO Videogiochi (Nome, Anno, Genere, Piattaforma, Sviluppatore) VALUES (%s, %s, %s, %s, %s)"
    val = (Nome, Anno, Genere, Piattaforma, Sviluppatore)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserito.")
    mycursor.execute("SELECT * FROM Videogiochi")

