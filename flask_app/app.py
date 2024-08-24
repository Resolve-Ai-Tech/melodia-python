from flask import Flask, request, jsonify
import src.utils as utils
import psycopg2

app = Flask(__name__)

# Rota de inicio
@app.route('/', methods=['GET'])
def incio():
    return jsonify({'status': 'API Funcionando!'})


@app.route('/playlists', methods=['POST'])
def playlists_post():
    # Exemplo de verificação de todos os parametros necessarios
    parametros_necessarios = {"nome_da_playlist": None, "id_do_usuario": None}
    validacao = utils.validacao_de_parametros(parametros_necessarios)
    if validacao:
        return
    
    # Exemplo de verificação de parametro json opcional POST!
    filtro_de_playlist = request.json.get("filtro")
    
    # Exemplo de verificação de parametro html-encoded opcional POST!
    filtro_de_playlist = request.form.get("filtro")

    # Lógica de playlists geradas com base na atividade
    # Lógica de playlists geradas em preferencias
    # Lógica de playlists geradas por região
    pass

@app.route('/playlists', methods=['POST'])
def playlists_get():
    # Lógica de pegar musicas de playlist
    pass

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
