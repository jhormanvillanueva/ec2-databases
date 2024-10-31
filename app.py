from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/libros')
def libros():
    conn = mysql.connector.connect(
        host="192.168.1.20",
        user="root",
        password="Test!2024",
        database="books_db")
    
    c = conn.cursor()
    c.execute("SELECT * FROM Books")
    books = c.fetchall()
    conn.close()
    return render_template("libros.html", books=books)

@app.route('/health')
def health():
    return jsonify('Ok'),200

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)