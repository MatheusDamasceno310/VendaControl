from repositorys.CategoriaRepository import CategoriaRepository
from helpers.Avisos import Aviso

class Categoria:
    """
    Representa uma categoria de produtos.

    Static method::
        cadastrar_categoria(nomeCategoria): Cadastra uma nova categoria.
        deletar_categoria(id, qntd): Deleta uma categoria.
    """

    def __init__(self, nomeCategoria):
        """
        Cria uma nova instância da classe Categoria.

        Args:
            nomeCategoria (str): O nome da categoria a ser criada.

        Returns:
            None
        """

        self.__nomeCategoria = nomeCategoria.upper()
        self.__qntdCategoria = 0

    def __str__(self):
        """
        Retorna o nome da categoria.

        Returns:
            str: O nome da categoria.
        """

        return self.nome_categoria

    @property
    def nome_categoria(self):
        """
        Getter para o nome da categoria.

        Returns:
            str: O nome da categoria.
        """

        return self.__nomeCategoria

    @nome_categoria.setter
    def nome_categoria(self, nomeCategoria):
        """
        Setter para o nome da categoria.

        Args:
            nomeCategoria (str): O novo nome da categoria.

        Returns:
            None
        """

        self.__nomeCategoria = nomeCategoria

    @property
    def qntd_categoria(self):
        """
        Getter para a quantidade de produtos dna categoria.

        Returns:
            int: A quantidade de produtos dna categoria.
        """

        return self.__qntdCategoria

    @qntd_categoria.setter
    def qntd_categoria(self, qntdCategoria):
        """
        Setter para a quantidade de produtos da categoria.

        Args:
            qntdCategoria (int): A nova quantidade de produtos da categoria.

        Returns:
            None
        """

        self.__qntdCategoria = qntdCategoria

    @staticmethod
    def cadastrar_categoria(nomeCategoria):
        """
        Cadastra uma nova categoria.

        Args:
            nomeCategoria (str): O nome da categoria a ser cadastrada.

        Returns:
            None
        """

        categoriaBanco = CategoriaRepository.read()
        categoriaValida = 'YES'
        categ = Categoria(nomeCategoria)

        if nomeCategoria != '':
            for id, nome, qntd in categoriaBanco:
                if nome == categ.nome_categoria:
                    categoriaValida = 'NO'

            if categoriaValida == 'YES':
                CategoriaRepository.create(categ.nome_categoria, categ.qntd_categoria)

            else:
                Aviso.mostar_aviso("Categoria já cadastrada!")

        else:
            Aviso.mostar_aviso("Não é possivel cadastrar nome em branco!")

    @staticmethod
    def deletar_categoria(id, qntd):
        """
        Deleta uma categoria.

        Args:
            id (int): O id da categoria a ser deletada.
            qntd (int): a quantidade de produtos da categoria a ser deletada.

        Returns:
            None
        """

        if qntd == '0':
            CategoriaRepository.delete(id)

        else:
            Aviso.mostar_aviso("Essa categoria contém produtos!")

