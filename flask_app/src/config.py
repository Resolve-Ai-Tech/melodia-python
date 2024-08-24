from psycopg2 import connect

# Configurações do banco de dados
DATABASE_CONFIG = {
    'dbname': 'melodia',
    'user': 'melodia',
    'password': 'melodia',
    'host': 'localhost',
    'port': '5444'
}

# Obter conexão com o banco de dados
def database_connection():
    return connect(**DATABASE_CONFIG)
