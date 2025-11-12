from flask import Flask, render_template
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)

# Route para sa login page
@app.route('/')
def login():
    return render_template('login.html')

# Route para sa register page
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)
