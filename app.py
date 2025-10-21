from flask import Flask, render_template
import os

app = Flask(__name__)

#log in page
@app.route('/')
def login():
    return render_template('login.html')

#register page
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)
