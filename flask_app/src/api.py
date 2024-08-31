import requests
from random import shuffle
from typing import List

API_URL = "http://191.252.194.153:8080/api/v1/"

# Gêneros recomendados para cada atividade
atividades_recomendadas = {
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

def obter_musicas(generos: List[str]) -> List[int]:
    ids_musicas = []
    print(generos)
    for genero in generos:
        params = {'genero': genero}
        response = requests.get(url=API_URL+"musicas/pesquisar", params=params)
        
        if response.status_code == 200:
            dados = response.json()
            ids_musicas.extend((musica['id'], musica['genero']) for musica in dados)
            shuffle(ids_musicas)
        else:
            response.raise_for_status()
    return ids_musicas

def obter_musicas_por_atividade(atividade: str) -> List[int]:
    generos = atividades_recomendadas.get(atividade, [])
    return obter_musicas(generos)[:100]

def obter_musicas_por_preferencia(preferencia: list) -> List[int]:
    return obter_musicas(preferencia)[:100]

def obter_usuario_por_id(usuario_id: int):
    # Devem ser implementados na api-java para não quebrar o codigo.
    # FIXME ENDPOINTS A IMPLEMENTAR: .../usuarios?id=XXX
    parametros = {"userID": usuario_id}
    response = requests.get(url=API_URL+'usuarios', params=parametros)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def obter_preferencia_por_usuario(usuario_id: int):
    usuario = obter_usuario_por_id(usuario_id)
    return usuario.get('preferencia', '')

def obter_atividade_por_usuario(usuario_id: int):
    usuario = obter_usuario_por_id(usuario_id)
    return usuario.get('atividade', '')