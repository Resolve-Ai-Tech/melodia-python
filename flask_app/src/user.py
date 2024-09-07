from requests import get_api
from utils import API_URL

class Usuario:
    def __init__(self, usuario_id: int):        
        self.usuario_id = usuario_id
        self.nome = None
        self.preferencias_musicais = []
        self.localizacao = None
        self.estado_emocional = None
        self.dados_completos = {}
        self._carregar_dados()

    def _carregar_dados(self):
        response = get_api(url=API_URL + "usuarios/" + str(self.usuario_id))
        if response.status_code == 200:
            dados = response.json()
            self.dados_completos = dados
            self.nome = dados.get('nome')
            self.preferencias_musicais = dados.get('preferenciasMusicais', [])
            self.estado_emocional = dados.get('estadoEmocionalAtual')
            self.localizacao = dados.get('localização')
        else:
            response.raise_for_status()

    def obter_preferencias(self):
        return self.preferencias_musicais

    def obter_localizacao(self):
        return self.localizacao

    def obter_estado_emocional(self):
        return self.estado_emocional
    
    def obter_dados_completos(self):
        return self.dados_completos
