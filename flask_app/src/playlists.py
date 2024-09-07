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
            print(f"Erro ao buscar músicas para o gênero {genero}: {response.status_code}")
    return ids_musicas

def obter_musicas_por_atividade(atividade: str) -> List[int]:
    """Obter músicas recomendadas com base na atividade do usuário"""
    generos = atividades_recomendadas.get(atividade, [])
    if not generos:
        print(f"Atividade {atividade} não tem gêneros recomendados")
    return obter_musicas(generos)[:50]

def obter_musicas_por_preferencia(preferencias: List[str]) -> List[int]:
    """Obter músicas com base em todas as preferências musicais do usuário"""
    if not preferencias:
        print("Nenhuma preferência musical encontrada para o usuário.")
        return []
    return obter_musicas(preferencias)[:50]