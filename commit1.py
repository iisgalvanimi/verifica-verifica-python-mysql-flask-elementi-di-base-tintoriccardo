
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS DatabaseVerifica")
mycursor.execute("USE DatabaseVerifica")

#tabella
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Videogiochi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255),
    Anno INT,
    Genere VARCHAR(255),
    Piattaforma VARCHAR(255),
    Sviluppatore VARCHAR(255)
)
""")

# inserire i dati nella tabella 
sql = "INSERT INTO Videogiochi (Nome, Anno, Genere, Piattaforma, Sviluppatore) VALUES (%s, %s, %s, %s, %s)"

val = [
  ('The Legend of Zelda: Breath of the Wild', 2017, 'Azione/Avventura', 'Nintendo Switch', 'Nintendo'),
  ('The Witcher 3: Wild Hunt', 2015, 'GDR', 'PC/PS4/Xbox One', 'CD Projekt Red'),
  ('Cyberpunk 2077', 2020, 'RPG', 'PC/PS5/Xbox Series X', 'CD Projekt Red'),
  ('Minecraft', 2011, 'Sandbox', 'PC/PS4/Xbox One/Switch', 'Mojang'),
  ('Grand Theft Auto V', 2013, 'Azione/Avventura', 'PC/PS4/Xbox One', 'Rockstar Games'),
  ('Fortnite', 2017, 'Battle Royale', 'PC/PS4/Xbox One/Switch', 'Epic Games'),
  ('Red Dead Redemption 2', 2018, 'Azione/Avventura', 'PC/PS4/Xbox One', 'Rockstar Games'),
  ('Overwatch', 2016, 'FPS', 'PC/PS4/Xbox One/Switch', 'Blizzard Entertainment'),
  ('Hades', 2020, 'Roguelike', 'PC/Switch', 'Supergiant Games'),
  ('Animal Crossing: New Horizons', 2020, 'Simulazione', 'Nintendo Switch', 'Nintendo')
]


mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
