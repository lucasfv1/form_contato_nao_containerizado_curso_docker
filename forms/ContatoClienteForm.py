from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, InputRequired


class ContatoClienteForm(FlaskForm):

    nome_cliente = StringField('Nome', validators=[DataRequired()])
    cpf_cliente = StringField('CPF', validators=[DataRequired()])
    email_cliente = StringField('Email', validators=[DataRequired()])
    numero_pedido = StringField('Número do pedido', validators=[DataRequired()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired()])