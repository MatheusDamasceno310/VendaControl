import mysql.connector
from repositorys.CriarConexaoRepository import CriarConexaoRepository

class RecebimentoRepository:
    """
    Classe responsável por acessar e manipular dados da tabela de "recebimemntos" no banco de dados "mercadinho_estoque".

    Static method::
        create(idVenda, idFormPag): Cria um novo registro na tabela "recebimentos".
        read(): Lê e retorna todos os registros da tabela "recebimentos".
    """

    @staticmethod
    def create(idVenda, idFormPag):
        """
        Cria um novo registro na tabela "recebimentos".

        Args:
            idVenda (int): O código da venda que vai ter o recebimento.
            idFormPag (int): O código da forma de pagamento que vai ter o recebimento.

        Returns:
            None
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('insert into recebimentos(venda_fk_receb, formpag_fk_receb) values ({}, {});'.format(idVenda, idFormPag))
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def read():
        """
        Lê e retorna todos os registros da tabela "recebimentos".

        Returns:
            list: Lista com todos os registros da tabela "recebimentos".
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('select * from recebimentos;')
        recebBanco = cursor.fetchall()

        return recebBanco

        cursor.close()
        conexao.close()