from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS  # Para permitir peticiones del frontend

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir comunicación entre front y back

# Función para conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM usuarios').fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

# Ruta para agregar un usuario
@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    data = request.json
    nombre = data.get('nombre')
    edad = data.get('edad')

    if not nombre or not edad:
        return jsonify({"error": "Faltan datos"}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', (nombre, edad))
    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Usuario agregado correctamente"}), 201

if __name__ == '__main__':
    app.run(debug=True)
