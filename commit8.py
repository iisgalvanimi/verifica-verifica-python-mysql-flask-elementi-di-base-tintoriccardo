import mysql.connector

from flask import Flask, jsonify

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
database="DatabaseVerifica"
)

mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/dati', methods=['GET'])
def get_dati():
    return jsonify(dati)