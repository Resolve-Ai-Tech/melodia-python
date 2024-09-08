from random import shuffle
from typing import List
from requests import get as get_api
from src.utils import atividades_recomendadas, API_URL


def obter_musicas(generos: List[str]) -> List[int]:
    """Obter IDs de músicas com base em uma lista de gêneros"""
    ids_musicas = []
    for genero in generos:
        params = {'genero': genero}
        response = get_api(url=API_URL + "musicas/pesquisar", params=params)
        if response.status_code == 200:
            dados = response.json()
            ids_musicas.extend(musica['id'] for musica in dados)
            shuffle(ids_musicas)
        else:
            return f"Erro ao buscar músicas para o gênero {genero}: {response.status_code}"
    return ids_musicas

def obter_musicas_por_atividade(atividade: str) -> List[int]:
    """Obter músicas recomendadas com base na atividade do usuário"""
    generos = atividades_recomendadas['emocoes'].get(atividade, [])
    print(generos)
    if not generos:
        return f"Emoção {atividade} não tem gêneros recomendados"
    return obter_musicas(generos)[:50]

def obter_musicas_por_preferencia(preferencias: List[str]) -> List[int]:
    """Obter músicas com base em todas as preferências musicais do usuário"""
    if not preferencias:
        return "Nenhuma preferência musical encontrada."
    return obter_musicas(preferencias)[:50]

def obter_musicas_por_regiao(regiao: any) -> List[int]:
    """Obter músicas com base em todas as preferências musicais do usuário"""
    recomendacao = atividades_recomendadas['regiao'].get(regiao, [])
    print(recomendacao, regiao)
    if not recomendacao:
        return "Nenhuma região encontrada."
    return obter_musicas(recomendacao)[:50]

def determinar_regiao(latitude, longitude):
    latitude = int(latitude)
    longitude = int(longitude)
    if -5 <= latitude <= 5 and -75 <= longitude <= -60:
        return "Norte"
    elif 5 < latitude <= 15 and -60 <= longitude <= -35:
        return "Nordeste"
    elif 10 <= latitude <= 20 and -65 <= longitude <= -50:
        return "Centro-Oeste"
    elif 20 <= latitude <= 25 and -55 <= longitude <= -45:
        return "Sudeste"
    elif 25 <= latitude <= 30 and -55 <= longitude <= -40:
        return "Sul"
    else:
        return "Desconhecido"