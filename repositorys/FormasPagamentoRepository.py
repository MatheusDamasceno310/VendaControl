import mysql.connector
from repositorys.CriarConexaoRepository import CriarConexaoRepository

class FormasPagamentoRepository:
    """
    Classe responsável por acessar e manipular dados da tabela de "formas_pagamento" no banco de dados "mercadinho_estoque".

    Static method::
        create(nomeFormPag): Cria uma nova forma de pagamento com o nome informado.
        delete(id): Deleta um registro de forma de pagamento no banco de dados.
        read(): Lê e retorna uma lista com todos os registros de formas de pagamento no banco de dados.
    """

    @staticmethod
    def create(nomeFormPag):
        """
        Cria uma nova forma de pagamento com o nome informado.

        Args:
            nomeFormPag (str): O nome da nova forma de pagamento.

        Returns:
            None
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('insert into formas_pagamento(formpag_nome) values ("{}");'.format(nomeFormPag))
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def delete(id):
        """
        Deleta um registro de forma de pagamento no banco de dados.

        Args:
            id (int): O id da forma de pagamento a ser deletada.

        Returns:
            None
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('delete from formas_pagamento where formpag_id = {};'.format(id))
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def read():
        """
        Lê e retorna uma lista com todos os registros de formas de pagamento no banco de dados.

        Returns:
            formPagBanco (list): Uma lista contendo os registros de formas de pagamento.
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('select * from formas_pagamento;')
        formPagBanco = cursor.fetchall()

        return formPagBanco

        cursor.close()
        conexao.close()
