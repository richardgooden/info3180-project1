from flask import Flask





UPLOAD_FOLDER = './app/static/uploads/'
SECRET_KEY = 'somesecurekey'

app = Flask(__name__)
app.config.from_object(__name__)

from app import views