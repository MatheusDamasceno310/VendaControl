import mysql.connector
from repositorys.CriarConexaoRepository import CriarConexaoRepository

class ProdutoRepository:
    """
    Classe responsável por acessar e manipular dados da tabela de "produtos" no banco de dados "mercadinho_estoque".

    Static method::
        create(codigoProduto, nomeProduto, precoProduto, quantidadeProduto, categoriaProduto): Cria um novo registro na tabela "produtos".
        delete(id): Deleta um produto da tabela "produtos".
        read(): Lê e retorna todos os registros da tabela "produtos".
        update(id, quantidade): Atualiza a quantidade de um produto na tabela "produtos".
    """

    @staticmethod
    def create(codigoProduto, nomeProduto, precoProduto, quantidadeProduto, categoriaProduto):
        """
        Cria um novo registro na tabela "produtos".

        Args:
            codigoProduto (int): O código do produto a ser adicionado.
            nomeProduto (str): O nome do produto a ser adicionado.
            precoProduto (float): O preço do produto a ser adicionado.
            quantidadeProduto (int): A quantidade do produto a ser adicionado.
            categoriaProduto (int): O id da categoria do produto a ser adicionado.

        Returns:
            None
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('insert into produtos(prod_codigo_produto, prod_nome, prod_preco, prod_quantidade, categ_fk_prod) values ("{}", "{}", {}, {}, {});'.format(codigoProduto, nomeProduto, precoProduto, quantidadeProduto, categoriaProduto))
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def delete(id):
        """
        Deleta um produto da tabela "produtos".

        Args:
            id (int): O id do registro a ser deletado.

        Returns:
            None
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('delete from produtos where prod_id = {};'.format(id))
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def read():
        """
        Lê e retorna todos os registros da tabela "produtos".

        Returns:
            list: Lista com todos os registros da tabela "produtos".
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('select * from produtos;')
        produtosBanco = cursor.fetchall()

        return produtosBanco

        cursor.close()
        conexao.close()

    @staticmethod
    def update(id, quantidade):
        """
        Atualiza a quantidade de um produto na tabela "produtos".

        Args:
            id (int): O id do produto a ser atualizado.
            quantidade (int): A nova quantidade do produto.

        Returns:
            None
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('update produtos set prod_quantidade = {} where prod_id = {};'.format(quantidade, id))
        conexao.commit()

        cursor.close()
        conexao.close()