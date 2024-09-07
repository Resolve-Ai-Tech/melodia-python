from flask import Flask, jsonify
from src.user import Usuario
from src.utils import validacao_de_parametros
from src import playlists

# App #
app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return jsonify({'status': 'API Funcionando!'}), 200

@app.route('/playlists', methods=['GET'])
def playlists_get():
    parametros_necessarios = {'filtro': None, 'usuarioid': None}
    validacao = validacao_de_parametros(parametros_necessarios)
    if validacao:
        return validacao
    
    filtro = parametros_necessarios['filtro']
    usuario = Usuario(parametros_necessarios['usuarioid'])

    if filtro == 'preferencia':
        musicas = playlists.obter_musicas_por_preferencia(usuario.preferencias_musicais)
    elif filtro == 'atividade':
        musicas = playlists.obter_musicas_por_atividade(usuario.estado_emocional)
    elif filtro == 'regiao':
        musicas = playlists.obter_musicas_por_regiao(usuario.localizacao)
    else:
        return jsonify({'error': f'Filtro de playlist inválido: {filtro}'}), 400

    return jsonify({"musicas": musicas}), 200

@app.route('/trends', methods=['GET'])
def musicas_trends():
    return jsonify({}), 200

@app.route('/musicas', methods=['GET'])
def musicas_por_pessoa():
    return jsonify({}), 200

if __name__ == '__main__':
    app.run(debug=True)
