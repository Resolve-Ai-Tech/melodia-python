from flask import Flask, jsonify
from src.utils import validacao_de_parametros
from src import playlists

# App #
app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return jsonify({'status': 'API Funcionando!'}), 200

@app.route('/playlists/preferencia', methods=['GET'])
def playlists_preferencia():
    parametros_necessarios = {'dados': None}
    validacao = validacao_de_parametros(parametros_necessarios)
    if validacao:
        return validacao

    preferencias_musicais = parametros_necessarios['dados']
    musicas = playlists.obter_musicas_por_preferencia(preferencias_musicais)
    return jsonify(musicas), 200

@app.route('/playlists/atividade', methods=['GET'])
def playlists_atividade():
    parametros_necessarios = {'dados': None}
    validacao = validacao_de_parametros(parametros_necessarios)
    if validacao:
        return validacao

    estado_emocional = parametros_necessarios['dados']  # Ajuste conforme a estrutura de dados
    musicas = playlists.obter_musicas_por_atividade(estado_emocional)
    return jsonify(musicas), 200

@app.route('/playlists/regiao', methods=['GET'])
def playlists_regiao():
    parametros_necessarios = {'latitude': None, 'longitude': None}
    validacao = validacao_de_parametros(parametros_necessarios)
    if validacao:
        return validacao

    localizacao = playlists.determinar_regiao(**parametros_necessarios)
    musicas = playlists.obter_musicas_por_regiao(localizacao)
    return jsonify(musicas), 200

@app.route('/trends', methods=['GET'])
def musicas_trends():
    return jsonify({}), 200

@app.route('/musicas', methods=['GET'])
def musicas_por_pessoa():
    return jsonify({}), 200

if __name__ == '__main__':
    app.run(debug=True)
