from flask import request, jsonify

def validacao_de_parametros(parametros_necessarios: dict):
    """Verifica todos os parametros necessarios"""
    
    for parametro in parametros_necessarios.keys():
        # Verifica qual http_method utilizar
        if request.method == "GET":
            pegar_parametro = request.args.get(parametro)
        elif request.method == "POST":
            pegar_parametro = pegar_dado_post(parametro=parametro)

        # Emissão de erro caso algum parâmetro necessario esteja vazio
        if not pegar_parametro:
            return jsonify({'status': f'Failed {parametro} parametrer not found'})
        else:
            parametros_necessarios[parametro] = pegar_parametro
            
def pegar_dado_post(parametro: str):
    """Fornece um dado de uma conexão POST"""
    
    # Verifica se o http_method realmente é POST
    if request.method != "POST":
        return jsonify({"status": "Seu metodo de conexão não é POST!"})
    
    if request.headers.environ["CONTENT_TYPE"] == 'application/json':
        return request.json.get(parametro)
    else:
        return request.form.get(parametro)