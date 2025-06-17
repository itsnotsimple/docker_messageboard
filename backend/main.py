from flask import Flask, request, jsonify
import psycopg2
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def connect_db():
    return psycopg2.connect(
        dbname=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        host='db'
    )

@app.route('/api/notes', methods=['GET', 'POST'])
def notes():
    conn = connect_db()
    cur = conn.cursor()
    if request.method == 'POST':
        content = request.get_json().get('text')
        cur.execute("INSERT INTO notes (text) VALUES (%s)", (content,))
        conn.commit()
    cur.execute("SELECT * FROM notes ORDER BY id DESC")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)