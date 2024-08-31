from flask import Flask, request, jsonify
from src import api, utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    """Retorna uma mensagem indicando que a API está funcionando."""
    return jsonify({'status': 'API Funcionando!'}), 200

@app.route('/playlists', methods=['GET'])
def playlists_get():
    parametros_necessarios = {'filtro': None, 'usuarioID': None}
    validacao = utils.validacao_de_parametros(parametros_necessarios)
    if validacao:
        print('oush')
        return validacao
    
    filtro = parametros_necessarios['filtro']
    usuario_id = parametros_necessarios['usuarioID']
    
    #usuario = api.obter_usuario_por_id(usuario_id=usuario_id)
    
    if filtro == 'preferencia':
        musicas = api.obter_musicas_por_preferencia(preferencia=["Rock", "Jazz"]) #usuario["preferencia"])
    elif filtro == 'atividade':
        musicas = api.obter_musicas_por_atividade(atividade=usuario["atividade"])
    elif filtro == 'regiao':
        musicas = api.obter_musicas_por_regiao(região=usuario["localização"])
    else:
        return jsonify({'error': 'Filtro de playlist inválido'}), 400

    return jsonify({"status": "200", "musicas": musicas}), 200

@app.route('/trends', methods=['GET'])
def musicas_trends():
    """Retorna as tendências musicais atuais."""
    response = {}
    return jsonify(response), 200

@app.route('/musicas', methods=['GET'])
def musicas_por_pessoa():
    """Retorna músicas recomendadas com base nas emoções do usuário."""
    response = {}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
