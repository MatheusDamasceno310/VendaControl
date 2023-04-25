from entities.Categoria import Categoria
from repositorys.ProdutoRepository import ProdutoRepository
from repositorys.CategoriaRepository import CategoriaRepository
from helpers.Avisos import Aviso

class Produto(Categoria):
    """
    Representa um produto.

    Static method::
        cadastrar_produto(codProduto, nomeProduto, precoProduto, categProduto): Cadastra um novo produto.
        deletar_produto(id): Deleta um produto.
        estoque(tipo, codigo, quantidade): Adicionar e remove uma quantidade do produto.
    """

    def __init__(self, codigoProduto, nomeProduto, precoProduto, categoria):
        """
        Cria uma nova instância da classe Produto.

        Args:
            codigoProduto (str): O código a ser criado.
            nomeProduto (str): O nome do produto a ser criada.
            precoProduto (float): O preço do produto a ser criada.
            categoria (str): A categoria do produto a ser criado.

        Returns:
            None
        """

        super().__init__(categoria)
        self.__codigoProduto = codigoProduto
        self.__nomeProduto = nomeProduto.upper()
        self.__precoProduto = precoProduto
        self.__quantidadeEstoque = 0

    def __str__(self):
        """
        Retorna a representação em string do produto.

        Returns:
            str: A representação em string do produto.
        """

        return 'Código: {}, produto {}, categoria {}, {:.0f} em estoque, preço R$ {:.2f}'.format(self.codigo_produto, self.nome_produto, self.nome_categoria, self.quantidade_estoque, self.preco_produto)

    @property
    def codigo_produto(self):
        """
        Getter para o código do produto.

        Returns:
            str: O código do produto.
        """

        return self.__codigoProduto

    @codigo_produto.setter
    def codigo_produto(self, codigoProduto):
        """
        Setter para o código do produto.

        Args:
            nomeCategoria (str): O novo código do produto.

        Returns:
            None
        """

        self.__codigoProduto = codigoProduto

    @property
    def nome_produto(self):
        """
        Getter para o nome do produto.

        Returns:
            str: O nome do produto.
        """

        return self.__nomeProduto

    @nome_produto.setter
    def nome_produto(self, nomeProduto):
        """
        Setter para o nome do produto.

        Args:
            nomeCategoria (str): O novo nome do produto.

        Returns:
            None
        """

        self.__nomeProduto = nomeProduto

    @property
    def preco_produto(self):
        """
        Getter para o preço do produto.

        Returns:
            float: O preço do produto.
        """

        return self.__precoProduto

    @preco_produto.setter
    def preco_produto(self, precoProduto):
        """
        Setter para o preço do produto.

        Args:
            precoProduto (float): O novo preço do produto.

        Returns:
            None
        """

        self.__precoProduto = precoProduto

    @property
    def quantidade_estoque(self):
        """
        Getter para a quantidade em estoque do produto.

        Returns:
            int: A quantidade em estoque do produto.
        """

        return self.__quantidadeEstoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidadeEstoque):
        """
        Setter para a quantidade em estoque do produto.

        Args:
            quantidadeEstoque (int): A nova quantidade em estoque do produto.

        Returns:
            None
        """

        self.__quantidadeEstoque = quantidadeEstoque

    @staticmethod
    def cadastrar_produto(codProduto, nomeProduto, precoProduto, categProduto):
        """
        Cadastra um novo produto.

        Args:
            codProduto (str): O código a ser cadastrado.
            nomeProduto (str): O nome do produto a ser cadastrado.
            precoProduto (float): O preço do produto a ser cadastrado.
            categProduto (str): A categoria do produto a ser cadastrada.

        Returns:
            None
        """

        produtoBanco = ProdutoRepository.read()
        produtoValido = 'YES'

        if codProduto != '' and nomeProduto != '' and precoProduto != '' and categProduto != '':
            try:
                prod = Produto(codProduto, nomeProduto, float(precoProduto), categProduto)

                for id, cod, nome, preco, qntd, categoria in produtoBanco:
                    if cod == prod.codigo_produto or nome == prod.nome_produto:
                        produtoValido = 'NO'

                if produtoValido == 'YES':
                    categoriaBanco = CategoriaRepository.read()
                    idCateProd = 'NO'

                    for id, nome, qntd in categoriaBanco:
                        if prod.nome_categoria == nome:
                            idCateProd = id

                    if idCateProd != 'NO':
                        ProdutoRepository.create(prod.codigo_produto, prod.nome_produto, prod.preco_produto, prod.quantidade_estoque, idCateProd)

                    else:
                        Aviso.mostar_aviso("Categoria não cadastrada!")

                else:
                    Aviso.mostar_aviso("Produto já cadastrado!")

            except ValueError as erro:
                Aviso.mostar_aviso("{}!".format(erro))

        else:
            Aviso.mostar_aviso("Preencha todos os campos!")

    @staticmethod
    def deletar_produto(id):
        """
        Deleta um produto.

        Args:
            id (int): O id do produto a ser deletado.

        Returns:
            None
        """

        ProdutoRepository.delete(id)

    @staticmethod
    def estoque(tipo, codigo, quantidade):
        """
        Adicionar e remove uma quantidade do produto.

        Args:
            tipo (str): O tipo de altetração qu vai ser feita.
            codigo (str): O código do produto que vai ser alterado.
            quantidade (int): A quantidade do produto que vai ser adicionada ou removida.

        Returns:
            None
        """

        try:
            if int(quantidade) > 0:
                produtoBanco = ProdutoRepository.read()
                codigoExistente = 'NO'
                for id, cod, nome, preco, qntd, categoria in produtoBanco:
                    if cod == codigo:
                        categoriaBanco = CategoriaRepository.read()
                        for idCateg, nomeCateg, qntdCateg in categoriaBanco:
                            if categoria == idCateg:
                                prod = Produto(cod, nome, preco, nomeCateg)
                                if tipo == "ADICIONAR":
                                    prod.quantidade_estoque = int(qntd) + int(quantidade)
                                elif tipo == "REMOVER":
                                    prod.quantidade_estoque = int(qntd) - int(quantidade)
                                codigoExistente = id

                if codigoExistente != 'NO':
                    if prod.quantidade_estoque >= 0:
                        ProdutoRepository.update(codigoExistente, prod.quantidade_estoque)

                    else:
                        Aviso.mostar_aviso("Não é possivel deixar estoque negativo!")

                else:
                    Aviso.mostar_aviso("Código não cadastrado!")

            else:
                Aviso.mostar_aviso("Não é possivel adicionar quantidade \nnula ou negativa!")

        except ValueError as erro:
            Aviso.mostar_aviso("{}!".format(erro))