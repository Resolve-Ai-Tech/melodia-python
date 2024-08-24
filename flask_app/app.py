from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Configurações do banco de dados
DATABASE_CONFIG = {
    'dbname': 'melodia',
    'user': 'melodia',
    'password': 'melodia',
    'host': 'localhost',
    'port': '5444'
}

# Obter conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn

# Rota de inicio
@app.route('/', methods=['GET'])
def home_index():
    return jsonify({'status': 'API Funcionando!'})

# Rota de playlists geradas em preferencias
# Rota de playlists geradas por região
# Rota de playlists geradas com base na atividade
# Rota de tendencias musicais
# Rota de musicas baseadas em emoções

if __name__ == '__main__':
    app.run(debug=True)
