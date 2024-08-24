from flask import Flask, jsonify
from src.utils import parametrers_validation
import psycopg2

app = Flask(__name__)

# Rota de inicio
@app.route('/', methods=['GET'])
def incio():
    return jsonify({'status': 'API Funcionando!'})


@app.route('/playlists', methods=['POST'])
def playlists():
    # Verifica todos os parametros necessarios
    parametros_necessarios = {"playlist_name": None}
    validacao = parametrers_validation(parametros_necessarios)
    if validacao:
        return validacao

    # Lógica de playlists geradas com base na atividade
    # Lógica de playlists geradas em preferencias
    # Lógica de playlists geradas por região
    return jsonify({'status': f'Playlist {parametros_necessarios["playlist_name"]} foi criada com sucesso!'})


@app.route('/trends', methods=['GET'])
def musicas_trends():
    # Lógica de tendencias musicais
    pass


@app.route('/musicas', methods=['GET'])
def musicas_por_pessoa():
    # Lógica de musicas baseadas em emoções
    pass


if __name__ == '__main__':
    app.run(debug=True)
