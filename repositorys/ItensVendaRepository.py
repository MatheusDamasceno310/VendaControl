import mysql.connector

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

        Parâmetros:
        - idVenda: o id da venda relacionada ao item.
        - idProduto: o id do produto relacionado ao item.
        - qntdVenda: a quantidade de produtos vendidos no item.
        - valorVenda: o valor total do item de venda.
        """

        conexao = mysql.connector.connect(host='localhost', user='root', password='9009', database='mercadinho_estoque')
        cursor = conexao.cursor()

        cursor.execute('insert into itens_venda(venda_fk_itvnd, prod_fk_itvnd, itvnd_qntd, itvnd_preco_total) values ({}, {}, {}, {});'.format(idVenda, idProduto, qntdVenda, valorVenda))
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def read():
        """
        Lê e retorna todos os itens de venda do banco de dados.

        Retorna: uma lista de tuplas, onde cada tupla representa um item de venda.
        """

        conexao = mysql.connector.connect(host='localhost', user='root', password='9009', database='mercadinho_estoque')
        cursor = conexao.cursor()

        cursor.execute('select * from itens_venda;')
        itVendasBanco = cursor.fetchall()

        return itVendasBanco

        cursor.close()
        conexao.close()