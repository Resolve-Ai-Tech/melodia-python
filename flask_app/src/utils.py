from flask import request, jsonify

def parametrers_validation(required_parametrers: dict):
    # Verifica todos os parametros necessarios

    for parametrer in required_parametrers.keys():
        # Verifica http_method` utilizar
        if request.method == "GET":
            parametrer_get = request.args.get(parametrer)
        elif request.method == "POST":
            parametrer_get = request.form.get(parametrer)

        print(parametrer_get)
        # Emissão de erro caso algum parâmetro necessario esteja vazio
        if not parametrer_get:
            return jsonify({'status': f'Failed {parametrer} parametrer not found'})
        else:
            required_parametrers[parametrer] = parametrer_get


