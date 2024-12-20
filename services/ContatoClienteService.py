from configuracoes import DBConnection

from entities.ContatoCliente import Base, ContatoCliente


class ContatoClienteService:

    # Salvar contato feito via formulário de atendimento ao cliente
    @staticmethod
    def salvar_contato_atendimento_cliente(form_contato):
        try:
            with DBConnection() as db:
                contato = ContatoCliente(
                    nome_cliente=form_contato.nome_cliente.data,
                    cpf_cliente=form_contato.cpf_cliente.data,
                    email_cliente=form_contato.email_cliente.data,
                    numero_pedido=form_contato.numero_pedido.data,
                    assunto=form_contato.assunto.data,
                    mensagem=form_contato.mensagem.data
                )
                db.session.add(contato)
                db.session.commit()
                return True
        except Exception as e:
            # Em caso de erro o método o rollback deve ser executado
            db.session.rollback()

            # Em caso de exceção, imprima o erro e retorne False para indicar falha no cadastro
            print(f"Erro ao salvar informações no formulário de atendimento ao cliente: {str(e)}")
            return False