from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask import Flask
import os
from dotenv import load_dotenv

metadata=MetaData()

load_dotenv()
app = Flask(__name__)

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")



app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@localhost/{database}'
db = SQLAlchemy(app, metadata=metadata)

