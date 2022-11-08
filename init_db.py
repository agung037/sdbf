import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())


cur  = connection.cursor()

cur.execute("INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (?, ?, ?)", ('Agung Kurniawan', "TK-1717", "Sistem Informasi"))
cur.execute("INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (?, ?, ?)", ('Susanto', "SA-8383", "Teknik Geologi"))


connection.commit()
connection.close()