from flask import Flask, request, jsonify
import src.utils as utils
import src.config as api

app = Flask(__name__)

# Rota de inicio
@app.route('/', methods=['GET'])
def incio():
    return jsonify({'status': 'API Funcionando!'})

@app.route('/playlists', methods=['POST'])
def playlists_post():
    """"Cria uma playlist baseado em um usuario ou outra filtragem"""
    
    # Verificação de todos os parametros necessarios
    parametros_necessarios = {"nome_da_playlist": None, "id_do_usuario": None, "filtro_de_playlist": None}
    validacao = utils.validacao_de_parametros(parametros_necessarios)
    if validacao:
        return validacao

    musicas_recomendadas = {
        'estudar': ['Lo-fi', 'Jazz', 'Clássica', 'Piano Relaxante'],
        'relaxamento': ['Ambient', 'Chillout', 'Música New Age', 'Acústica'],
        'treino': ['Hip-Hop', 'Trap', 'Rock Alternativo', 'EDM'],
        'cozinhar': ['Bossa Nova', 'Soul', 'Jazz', 'Pop Leve'],
        'viajar': ['Indie Folk', 'Synthwave', 'Pop Rock', 'World Music'],
        'limpeza': ['Pop Energético', 'Funk', 'Dance', 'Disco'],
        'caminhada': ['Indie Pop', 'Reggae', 'Folk', 'Música Eletrônica Leve'],
        'jogar': ['Synthwave', 'Drum & Bass', 'Rock Progressivo', '8-bit'],
        'dançar': ['Funk', 'Reggaeton', 'House Music', 'Pop'],
        'família': ['MPB', 'Country', 'Folk', 'Pop Clássico'],
        'compras': ['Electropop', 'Disco', 'R&B Contemporâneo', 'Synthpop'],
        'desenhar': ['Jazz Contemporâneo', 'Indie Instrumental', 'Lo-fi', 'Clássica'],
        'dormir': ['Música Ambiente', 'Som de Chuva', 'Piano Suave', 'Clássica Relaxante']
    }
    match parametros_necessarios['filtro_de_playlist']:
        case "preferencia":
            # Lógica de playlists geradas com base na atividade
            preferencia = api.preferencias_de_usuarios(parametros_necessarios['id_do_usuario'])
            return jsonify({"status": "200" ,"musicas": api.musicas(musicas_recomendadas[preferencia])})
        case "atividade":
            # Lógica de playlists geradas em preferencias
            return jsonify({"status": "200" ,"musicas": []})

        case "regiao":
            # Lógica de playlists geradas por região
            return jsonify({"status": "200" ,"musicas": []})
    
@app.route('/trends', methods=['GET'])
def musicas_trends():
    # Lógica de tendencias musicais
    response = {}
    return jsonify(response)

@app.route('/musicas', methods=['GET'])
def musicas_por_pessoa():
    # Lógica de musicas baseadas em emoções
    response = {}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
