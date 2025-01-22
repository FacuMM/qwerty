# init_db.py - Script para crear la base de datos SQLite
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

conn.commit()
conn.close()
print("Base de datos creada correctamente.")
