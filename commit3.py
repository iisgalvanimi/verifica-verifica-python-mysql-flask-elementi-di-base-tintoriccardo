import mysql.connector

# Connessione al database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)

mycursor = mydb.cursor()

print("INSERISCI UN NUOVO VIDEOGIOCO")

Nome = input("Inserisci il nome del videogioco: ")
Anno = int(input("Inserisci l'anno di uscita: "))
Genere = input("Inserisci il genere del videogioco: ")
Piattaforma = input("Inserisci la piattaforma (ad esempio, PC, PS4, Xbox): ")
Sviluppatore = input("Inserisci il nome dello sviluppatore: ")

sql = "INSERT INTO Videogiochi (Nome, Anno, Genere, Piattaforma, Sviluppatore) VALUES (%s, %s, %s, %s, %s)"
val = (Nome, Anno, Genere, Piattaforma, Sviluppatore)


mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserito.")
