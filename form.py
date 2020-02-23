from wtforms import From
from wtforms import StringField, TextField

class CommentForm(From):
    producto = StringField()