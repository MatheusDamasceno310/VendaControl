import mysql.connector
from repositorys.CriarConexaoRepository import CriarConexaoRepository

class CategoriaRepository:
    """
    Classe responsável por acessar e manipular dados da tabela de "categorias" no banco de dados "mercadinho_estoque".

    Static method::
        create(nomeCategoria, qntdCategoria): Cria um novo registro na tabela "categorias".
        delete(id): Deleta uma categoria da tabela "categorias".
        read(): Lê e retorna todos os registros da tabela "categorias".
    """

    @staticmethod
    def create(nomeCategoria, qntdCategoria):
        """
        Cria um novo registro na tabela "categorias".

        Args:
            nomeCategoria (str): O nome da categoria a ser adicionada.
            qntdCategoria (int): A quantidade de produtos que tem cadastrado nessa categoria.

        Returns:
            None
        """
        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('insert into categorias(categ_nome, categ_quantidade) values ("{}", {});'.format(nomeCategoria, qntdCategoria))
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def delete(id):
        """
        Deleta uma categoria da tabela "categorias".

        Args:
            id (int): O id do registro a ser deletado.

        Returns:
            None
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('delete from categorias where categ_id = {};'.format(id))
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def read():
        """
        Lê e retorna todos os registros da tabela "categorias".

        Returns:
            list: Lista com todos os registros da tabela "categorias".
        """

        conexao = CriarConexaoRepository.criar_conexao()
        cursor = conexao.cursor()

        cursor.execute('select * from categorias;')
        categoriasBanco = cursor.fetchall()

        return categoriasBanco

        cursor.close()
        conexao.close()
