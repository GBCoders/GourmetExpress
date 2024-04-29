from flask import Flask, request, jsonify
from login import authenticate
from signup import register_user

from flask_sqlalchemy import SQLAlchemy
# instalar o alchem
# e concetar  a tabela
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://id:username:password@localhost/pg_gourmetexpress'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Página inicial'

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    
    if register_user(username, email, password):
        return jsonify({'message': 'Usuário criado com sucesso'})
    else:
        return jsonify({'message': 'Usuário já existe'})
    
    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    if authenticate(email, password):
        return jsonify({'message': 'Login realizado com sucesso'})
    else: return jsonify({'message': 'E-mail ou senha incorretos'})
    

