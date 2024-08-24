from flask import request, jsonify

def validar_parametros(parametros_necessarios: dict):
    # Verifica todos os parametros necessarios

    for parametro in parametros_necessarios.keys():
        # Verifica http_method` utilizar
        if request.method == "GET":
            pegar_parametro = request.args.get(parametro)
        elif request.method == "POST":
            pegar_parametro = request.form.get(parametro)

        # Emissão de erro caso algum parâmetro necessario esteja vazio
        if not pegar_parametro:
            return jsonify({'status': f'Failed {parametro} parametrer not found'})
        else:
            parametros_necessarios[parametro] = pegar_parametro


