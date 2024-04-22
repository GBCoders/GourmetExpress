from flask import Flask
from .login import login as authenticate

app = Flask(__name__)

@app.route('/')
def index():
    return 'Página inicial'

@app.route('/login', methods=['POST'])
def login():
    return authenticate()

