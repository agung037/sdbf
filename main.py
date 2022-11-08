from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "jsadjhadjh73736s7ds7d6k3j4"


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        jurusan = request.form['jurusan']
        conn = get_db_connection()
        conn.execute('INSERT INTO mahasiswa (nim, nama, jurusan) VALUES (?, ?, ?)', (nim, nama, jurusan))
        conn.commit()
        conn.close()
        return redirect('/')

    conn = get_db_connection()
    mahasiswa = conn.execute('SELECT * FROM mahasiswa').fetchall()
    conn.close()
    return render_template('index.html', mahasiswa=mahasiswa)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))