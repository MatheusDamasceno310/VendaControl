import mysql.connector
from repositorys.CriarConexaoRepository import CriarConexaoRepository

class ItensVendaRepository:
    """
    Classe responsável por acessar e manipular dados da tabela de "itens_venda" no banco de dados "mercadinho_estoque".

    Static method::
        create(idVenda, idProduto, qntdVenda, valorVenda): Cria um novo item de venda no banco de dados.
        read(): Lê e retorna todos os itens de venda do banco de dados.
    """

    @staticmethod
    def create(idVenda, idProduto, qntdVenda, valorVenda):
        """
        Cria um novo item de venda no banco de dados.

        Args:
            idVenda (int): O id da venda relacionada ao item.
            idProduto (int): O id do produto relacionado ao item.
            qntdVenda (int): A quantidade de produtos vendidos no item.
            valorVenda (float): O valor total do item de venda.

        Returns:
            None
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('insert into itens_venda(venda_fk_itvnd, prod_fk_itvnd, itvnd_qntd, itvnd_preco_total) values ({}, {}, {}, {});'.format(idVenda, idProduto, qntdVenda, valorVenda))
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def read():
        """
        Lê e retorna todos os itens de venda do banco de dados.

        Returns:
            list: Lista de tuplas, onde cada tupla representa um item de venda.
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('select * from itens_venda;')
        itVendasBanco = cursor.fetchall()

        return itVendasBanco

        cursor.close()
        conexao.close()