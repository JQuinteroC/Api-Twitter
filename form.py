from wtforms import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms import validators
from wtforms.fields.html5 import DateField

class CommentForm(Form):
    producto = SelectField('Producto', choices=[('ch','chocoramo'),('ga','gansito'),('pq','ponqué gala'), ('ts','tostacos')])
    fecha_In = DateField("Fecha ininio", format = '%Y-%m-%d')
    fecha_Out = DateField("Fecha fin", format = '%Y-%m-%d', validators = (validators.Optional(),))