from flask import Flask, render_template
from dotenv import load_dotenv
from config import Config
from models.db import db
from models.user_model import Student
from flask_migrate import Migrate

import os

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
        return render_template('index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(port=port, debug=True)