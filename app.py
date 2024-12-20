from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, jsonify

# Import do arquivo de configurações
from configuracoes import SECRECT_KEY, SQLALCHEMY_DATABASE_URI

from forms.ContatoClienteForm import ContatoClienteForm
from services.ContatoClienteService import ContatoClienteService

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRECT_KEY


# Rota para a página principal
@app.route("/", methods=['GET', 'POST'])
def home_page():
    return atendimento_cliente()


# Rota para o formulário de contato
@app.route("/contato", methods=['GET', 'POST'])
def atendimento_cliente():

    # Instancia o objeto do formulário
    form_contato = ContatoClienteForm()

    if request.method == 'POST':

        # Verifica se o formulário foi enviado
        if form_contato.validate_on_submit():

            salvar_contato = ContatoClienteService.salvar_contato_atendimento_cliente(form_contato)

            if salvar_contato:
                flash('Sua mensagem foi enviada com sucesso! Em breve retornaremos.', 'success')
            else:
                flash('Ocorreu um erro ao tentar enviar sua mensagem. Tente novamente mais tarde.', 'error')
            return redirect(url_for('atendimento_cliente'))

        else:
            return render_template("form-contato.html", form_contato=form_contato)

    return render_template("form-contato.html", form_contato=form_contato)


def start():
    app.run(host='0.0.0.0', threaded=True, port=5001, debug=True)


# Inicia a aplicação através do método start
start()