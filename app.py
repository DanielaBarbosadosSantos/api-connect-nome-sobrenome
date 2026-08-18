from flask import Flask, request, jsonify
from routes.user_routes import user_bp

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.before_request
def json_middleware():
    if request.method in ['POST', 'PUT', 'PATCH']:
        if not request.is_json:
            return jsonify({
                "erro": "Tipo de mídia não suportado. A API aceita apenas o formato JSON."
            }), 415

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "API Connect rodando perfeitamente!",
        "codigo": 200
    }), 200

app.register_blueprint(user_bp, url_prefix='/api/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
