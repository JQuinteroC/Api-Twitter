from flask import Flask,render_template
import form
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500