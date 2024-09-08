from flask import request, jsonify


# Variaveis uteis
API_URL = "http://191.252.194.153:8080/api/v1/"

atividades_recomendadas = {
    "emocoes": {
        "ORGULHOSO": ["Motivacional", "Triunfo", "Empoderamento", "Pop", "Rock"],
        "OUTROS": ["Diversidade Musical", "Exploração", "Instrumental", "Ambient"],
        "CONFUSO": ["Lo-fi", "Jazz Relaxante", "Música Ambiental", "Chillout"],
        "SURPRESO": ["Música Experimental", "Mistério", "Surpresa", "Phonk"],
        "AGITADO": ["Hip-Hop", "Rock Alternativo", "EDM", "Phonk", "Dance"],
        "CALMO": ["Música Ambiente", "Classical Relaxante", "Acústica", "Lo-fi", "Chillout"],
        "ANSIOSO": ["Chillout", "Ambient", "Piano Relaxante", "Phonk"],
        "FELIZ": ["Pop", "Funk", "Reggae", "Dance", "Phonk"],
        "INDIFERENTE": ["Instrumental", "Música de Fundo", "Folk", "Ambient"],
        "DESANIMADO": ["Música Melancólica", "Clássica Triste", "Instrumental"],
        "TRISTE": ["Música Melancólica", "Clássica Triste", "Instrumental Lento", "Phonk"],
        "ESTRESSADO": ["Relaxamento", "Chillout", "Música Ambiental", "Ambient"],
        "MOTIVADO": ["Rock Energético", "Hip-Hop", "Electro", "Phonk", "Dance"],
        "ENERGICO": ["Dance", "EDM", "Pop", "Phonk"],
        "EXCITADO": ["Dance", "Electropop", "Pop Alternativo", "Phonk"],
        "GRATO": ["Música Calma", "Classical Relaxante", "Acústica", "Lo-fi"],
        "DETERMINADO": ["Música Inspiradora", "Rock Motivacional", "Phonk"],
        "APAIXONADO": ["Romântico", "Jazz Suave", "Bossa Nova"],
        "DECEPCIONADO": ["Música Melancólica", "Tristeza Musical"],
        "ENTEDIADO": ["Música Leve", "Alternativa", "Instrumental", "Phonk"],
        "MELANCOLICO": ["Música Melancólica", "Clássica Triste", "Instrumental", "Phonk"],
        "FOCADO": ["Lo-fi", "Música de Estudo", "Piano", "Ambient"],
        "INSPIRADO": ["Música Inspiradora", "Classical Inspiradora", "Phonk"],
        "TENSO": ["Relaxamento", "Ambient", "Música Suave", "Phonk"],
        "CONFIANTE": ["Música Energética", "Pop", "Rock", "Phonk"],
        "SATISFEITO": ["Música Alegre", "Feliz", "Calma", "Phonk"],
        "ESPERANCOSO": ["Música Esperançosa", "Inspiradora", "Positiva"],
        "FRUSTRADO": ["Música Relaxante", "Ambient", "Suave", "Phonk"],
        "RELAXADO": ["Ambient", "Chillout", "Relaxante", "Lo-fi"],
        "CULPADO": ["Música Calmante", "Relaxamento", "Tristeza Suave", "Phonk"]
    },
    "regiao":  {
        "Norte": ["Sertanejo", "Música Popular Brasileira (MPB)", "Samba", "Forró"],
        "Nordeste": ["Axé", "Frevo", "Samba de Roda", "MPB"],
        "Centro-Oeste": ["Sertanejo", "Forró", "Música Gaúcha", "MPB"],
        "Sudeste": ["Samba", "Bossa Nova", "Funk Carioca", "Rock"],
        "Sul": ["Música Gaúcha", "Sertanejo", "Rock", "MPB"]
    }
}

# Functions
def validacao_de_parametros(parametros_necessarios: dict):
    for parametro in parametros_necessarios:
        if request.method == "GET":
            valor = request.args.get(parametro)
        elif request.method == "POST":
            valor = pegar_dado_post(parametro)
        if not valor:
            return jsonify({'status': f'Failed {parametro} parameter not found'})
        parametros_necessarios[parametro] = valor
            
def pegar_dado_post(parametro: str):
    if request.method != "POST":
        return jsonify({"status": "Seu método de conexão não é POST!"})
    
    if request.headers.get("CONTENT_TYPE") == 'application/json':
        return request.json.get(parametro)
    return request.form.get(parametro)