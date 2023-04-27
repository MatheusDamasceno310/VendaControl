from repositorys.ProdutoRepository import ProdutoRepository
from helpers.Avisos import Aviso

class ItensVenda:
    """
    Representa os itens qua vão ser comprados.

    Static method::
        Adiciona um produto na lista de itens da venda, caso o código seja válido e a quantidade esteja disponível em estoque.
    """

    @staticmethod
    def adicionar_produto(codigo, quantidade, itensVenda):
        """
        Adiciona um produto na lista de itens da venda, caso o código seja válido e a quantidade esteja disponível em estoque.

        Args:
            codigo (str): O código do produto a ser adicionado.
            quantidade (str): A quantidade do produto a ser adicionado.
            itensVenda (list): Os produtos escolhidos pelo cliente

        Returns:
            list ou None: Retorna uma lista com o id, código, nome, preço unitário, quantidade e preço total do produto adicionado, caso seja possível adicioná-lo.
        """

        if codigo != '' and quantidade != '':
            try:
                quantidade = int(quantidade)
                if quantidade > 0:
                    produtoBanco = ProdutoRepository.read()
                    codigoValido = "NO"
                    quantidadeValida = "NO"

                    for id, cod, nome, preco, qntd, categoria in produtoBanco:
                        if cod == codigo:
                            if quantidade <= qntd and quantidade > 0:
                                codigoValido = [id, cod, nome, preco, quantidade, preco * quantidade]
                                quantidadeValida = "YES"

                    if quantidadeValida == "YES":
                        if codigoValido != 'NO':
                            return codigoValido

                        else:
                            Aviso.mostar_aviso("Código não cadastrado!")

                    else:
                        Aviso.mostar_aviso("Não há essa quantidade em estoque!")

                else:
                    Aviso.mostar_aviso("Não é possivel comprar \n0 produtos ou menos!")

            except ValueError as erro:
                Aviso.mostar_aviso("{}!".format(erro))

        else:
            Aviso.mostar_aviso("Preencha todos os campos!")
