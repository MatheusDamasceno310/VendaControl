import mysql.connector

class VendasRepository:
    """
    Classe responsável por acessar e manipular dados da tabela de "vendas" no banco de dados "mercadinho_estoque".

    Static method::
        create(valorTotal): Cria uma nova venda no banco de dados.
        read(): Lê e retorna todas as vendas do banco de dados.
    """

    @staticmethod
    def create(valorTotal):
        """
        Cria uma nova venda no banco de dados.

        Args:
            valorTotal (float): Valor total da venda.
        """

        conexao = mysql.connector.connect(host='localhost', user='root', password='9009', database='mercadinho_estoque')
        cursor = conexao.cursor()

        cursor.execute('insert into vendas(venda_valor_total) values ({});'.format(valorTotal))
        conexao.commit()

        cursor.close()
        conexao.close()



    @staticmethod
    def read():
        """
        Lê e retorna todas as vendas do banco de dados.

        Returns:
            list: Lista contendo as vendas.
        """

        conexao = mysql.connector.connect(host='localhost', user='root', password='9009', database='mercadinho_estoque')
        cursor = conexao.cursor()

        cursor.execute('select * from vendas;')
        vendasBanco = cursor.fetchall()

        return vendasBanco

        cursor.close()
        conexao.close()