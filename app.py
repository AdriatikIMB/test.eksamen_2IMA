from flask import Flask, render_template, redirect, request, url_for
import mysql.connector

app = Flask(__name__)

#Funksjon for å koble til databasen
def get_db_connection():
    mysql.connector.connect(
        user="adriatikveseli",
        password="Adriatik.123",
        database="restaurant",
        host="10.2.4.76",
        port=3306
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods =['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSET INTO testeksamen (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)