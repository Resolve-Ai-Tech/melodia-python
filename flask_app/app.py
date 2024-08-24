from flask import Flask, request, jsonify
from src.utils import parametrers_validation
import psycopg2

app = Flask(__name__)

# Rota de inicio
@app.route('/', methods=['GET'])
def home_index():
    return jsonify({'status': 'API Funcionando!'})


@app.route('/playlists', methods=['POST'])
def playlists():
    # Verifica todos os parametros necessarios
    required_parametrers = {"playlist_name": None}
    validation = parametrers_validation(required_parametrers)
    if validation:
        return validation

    # Lógica de playlists geradas com base na atividade
    # Lógica de playlists geradas em preferencias
    # Lógica de playlists geradas por região
    return jsonify({'status': f'Playlist {required_parametrers["playlist_name"]} foi criada com sucesso!'})


@app.route('/trends', methods=['GET'])
def musicas_trends():
    # Lógica de tendencias musicais
    pass


@app.route('/musicas', methods=['GET'])
def musicas_por_pessoa()
    # Lógica de musicas baseadas em emoções
    pass


if __name__ == '__main__':
    app.run(debug=True)
