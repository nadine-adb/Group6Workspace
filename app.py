from flask import Flask, render_template

app = Flask(__name__)

# This route will show the login page
@app.route('/')
def home():
    # This command tells Flask to find 'login.html' inside the 'templates' folder and show it.
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)