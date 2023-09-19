from flask import Flask, jsonify, request
from flask_cors import CORS

from database import Database
from eventNow_database import EventDatabase



import json

db = Database("bolt://44.203.246.65:7687", "neo4j", "rattle-primitives-admirals")
eventDB = EventDatabase(db)

app = Flask(__name__)

CORS(app)


@app.route('/cadastro', methods=['POST'])
def receber_dados():
    try:
        # Obtenha os dados enviados na solicitação POST
        dados = request.get_json() 
        
        eventDB.create_usuario(dados['nome'],dados['sobrenome'],dados['email'],dados['senha'])
        
        return jsonify({'mensagem': 'sucesso'})

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao receber dados', 'error': str(e)}), 500


    

app.run(port=5000,host='localhost',debug=True)