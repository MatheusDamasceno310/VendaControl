import mysql.connector
class CriarConexaoRepository:
    """
    Classe responsável por conectar todos os repositories ao banco de dados.

    Static method::
        criar_conexao(): Cria uma conexão com o banco de dados.
    """

    @staticmethod
    def criar_conexao():
        """
        Cria uma conexão com o banco de dados.

        Returns:
            str: A conexão com o banco de dados.
        """

        conexao = mysql.connector.connect(host='localhost', user='root', password='9009', database='mercadinho_estoque')
        return conexao