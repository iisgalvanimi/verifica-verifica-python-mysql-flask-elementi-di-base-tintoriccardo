import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)

mycursor = mydb.cursor()


mycursor.execute("USE DatabaseVerifica")


modId = input("Inserisci l'ID del videogioco che vuoi modificare: ")

print("""1) MODIFICARE IL NOME DEL VIDEOGIOCO2) MODIFICARE L'ANNO DI USCITA3) MODIFICARE IL GENERE4) MODIFICARE LA PIATTAFORMA5) MODIFICARE LO SVILUPPATORE""")

inp = int(input())  


if inp == 1:
    Nuovo_nome = input("Inserisci il nuovo nome del videogioco: ")
    update_query = """
    UPDATE Videogiochi 
    SET Nome = %s 
    WHERE id = %s
    """
    dati = (Nuovo_nome, modId)
    mycursor.execute(update_query, dati)
    mydb.commit()


elif inp == 2:
    Nuovo_anno = int(input("Inserisci il nuovo anno di uscita: "))
    update_query = """
    UPDATE Videogiochi 
    SET Anno = %s 
    WHERE id = %s
    """
    dati = (Nuovo_anno, modId)
    mycursor.execute(update_query, dati)
    mydb.commit()


elif inp == 3:
    Nuovo_genere = input("Inserisci il nuovo genere: ")
    update_query = """
    UPDATE Videogiochi 
    SET Genere = %s 
    WHERE id = %s
    """
    dati = (Nuovo_genere, modId)
    mycursor.execute(update_query, dati)
    mydb.commit()


elif inp == 4:
    Nuova_piattaforma = input("Inserisci la nuova piattaforma: ")
    update_query = """
    UPDATE Videogiochi 
    SET Piattaforma = %s 
    WHERE id = %s
    """
    dati = (Nuova_piattaforma, modId)
    mycursor.execute(update_query, dati)
    mydb.commit()


elif inp == 5:
    Nuovo_sviluppatore = input("Inserisci il nuovo sviluppatore: ")
    update_query = """
    UPDATE Videogiochi 
    SET Sviluppatore = %s 
    WHERE id = %s
    """
    dati = (Nuovo_sviluppatore, modId)
    mycursor.execute(update_query, dati)
    mydb.commit()
