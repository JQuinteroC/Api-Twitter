from flask import Flask,render_template
from flask import request
import form
import AnalysisRamoFinal
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    comment = form.CommentForm(request.form)
    consulta = False
    if request.method == 'POST' and comment.validate():
        consulta = True
        producto = comment.producto.data
        fecha1 = comment.fecha_In.data
        fecah2 = comment.fecha_Out.data
        cantidad = comment.cantidadTw.data
        AnalysisRamoFinal.sentimientos(producto, cantidad)
        AnalysisRamoFinal.ciudades(producto, cantidad)
        return render_template('home.html', form = comment, consulta = consulta)
    return render_template('home.html', form = comment, consulta = consulta)
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500