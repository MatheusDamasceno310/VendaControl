from repositorys.ProdutoRepository import ProdutoRepository
from helpers.Avisos import Aviso

class ItensVenda:

    @staticmethod
    def adicionar_produto(codigo, quantidade):
        if codigo != '' and quantidade != '':
            try:
                quantidade = int(quantidade)
                if quantidade > 0:
                    produtoBanco = ProdutoRepository.read()
                    codigoValido = "NO"
                    quantidadeValida = "NO"

                    for id, cod, nome, preco, qntd, categoria in produtoBanco:
                        if cod == codigo:
                            if quantidade < qntd:
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