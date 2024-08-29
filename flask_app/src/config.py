import psycopg2
from requests import request

# Configurações do banco de dados
DATABASE_CONFIG = {
    'dbname': 'melodia',
    'user': 'melodia',
    'password': 'melodia',
    'host': 'localhost',
    'port': '5444'
}

# Obter conexão com o banco de dados
api = psycopg2.connect(**DATABASE_CONFIG)

def pegar_usuario(usuario_id: int):
    with api:
        with api.cursor() as sql:
            sql.execute('SELECT nome FROM usuarios WHERE id=%s', (usuario_id,))
            resposta = sql.fetchone()
    return resposta[0]
            

def preferencias_de_usuarios(usuario_id: int):
    with api:
        with api.cursor() as sql:
            sql.execute('SELECT atividade FROM atividades_usuarios WHERE usuario_id=%s', (usuario_id,))
            resposta = sql.fetchone()
    return resposta[0]

def musicas(filtro: str, limit: int = 100):
    #resposta = request("GET", "")
    with api:
        with api.cursor() as sql:
            generos = tuple([genero for genero in filtro])
            sql_parametros = ', '.join(['%s'] * len(filtro))
            sql.execute(f"SELECT id, titulo FROM musicas WHERE genero IN ({sql_parametros}) order by ", generos)
            resposta = sql.fetchall()
    return resposta
