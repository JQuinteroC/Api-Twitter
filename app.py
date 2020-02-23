from flask import Flask,render_template
from flask import request
import form
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    comment = form.CommentForm(request.form)
    if request.method == 'POST' and comment.validate():
        
        print (comment.producto.data)
        print (comment.fecha_In.data)
        print (comment.fecha_Out.data)

    return render_template('home.html', form = comment)
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500