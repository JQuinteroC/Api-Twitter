from wtforms import Form
from wtforms import SelectField
from wtforms import validators
from wtforms.fields.html5 import IntegerField
from wtforms.fields.html5 import DateField

class CommentForm(Form):
    producto = SelectField('Producto', choices=[
        ('chocoramo','chocoramo'),('ponqué gala','ponqué gala'), ('tostacos','tostacos'),
        ('papas caseras','papas caseras'), ('galletas ramo','galletas ramo')])
    fecha_In = DateField("Fecha ininio", format = '%Y-%m-%d', validators = [validators.Required()])
    fecha_Out = DateField("Fecha fin", format = '%Y-%m-%d', validators = [validators.Required()])
    cantidadTw = IntegerField("Cant. de tweets", [validators.Required(), validators.NumberRange(10,500)])
