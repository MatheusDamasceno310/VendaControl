from entities.Categoria import Categoria
from repositorys.ProdutoRepository import ProdutoRepository
from repositorys.CategoriaRepository import CategoriaRepository
from helpers.Avisos import Aviso

class Produto(Categoria):

    def __init__(self, codigoProduto, nomeProduto, precoProduto, categoria):
        super().__init__(categoria)
        self.__codigoProduto = codigoProduto
        self.__nomeProduto = nomeProduto.upper()
        self.__precoProduto = precoProduto
        self.__quantidadeEstoque = 0

    def __str__(self):
        return 'Código: {}, produto {}, categoria {}, {:.0f} em estoque, preço R$ {:.2f}'.format(self.codigo_produto, self.nome_produto, self.nome_categoria, self.quantidade_estoque, self.preco_produto)

    @property
    def codigo_produto(self):
        return self.__codigoProduto

    @codigo_produto.setter
    def codigo_produto(self, codigoProduto):
        self.__codigoProduto = codigoProduto

    @property
    def nome_produto(self):
        return self.__nomeProduto

    @nome_produto.setter
    def nome_produto(self, nomeProduto):
        self.__nomeProduto = nomeProduto

    @property
    def preco_produto(self):
        return self.__precoProduto

    @preco_produto.setter
    def preco_produto(self, precoProduto):
        self.__precoProduto = precoProduto

    @property
    def quantidade_estoque(self):
        return self.__quantidadeEstoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidadeEstoque):
        self.__quantidadeEstoque = quantidadeEstoque

    @staticmethod
    def cadastrar_produto(codProduto, nomeProduto, precoProduto, categProduto):
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
        ProdutoRepository.delete(id)

    @staticmethod
    def estoque(tipo, codigo, quantidade):
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

if __name__ == "__main__":
    prod = Produto(111, "mouse", 10.2, "Info")
    print(prod.__str__())
