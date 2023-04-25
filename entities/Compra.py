from repositorys.ItensVendaRepository import ItensVendaRepository
from repositorys.VendasRepository import VendasRepository
from repositorys.FormasPagamentoRepository import FormasPagamentoRepository
from repositorys.RecebimentoRepository import RecebimentoRepository

class Compra:
    """
    Representa a finalização da compra.

    Static method::
        finalizar_compra: Finaliza a compra.
    """

    @staticmethod
    def finalizar_compra(valorTotal, itensLista, formaDePg):
        """
        Finaliza a compra.

        Args:
            valorTotal (float): O preço total da compra.
            itensLista (list): A lista com os produtos a serem comprados.
            formaDePg (str): A forma de pagamento da compra.

        Returns:
            None
        """

        VendasRepository.create(valorTotal)

        vendasBanco = VendasRepository.read()
        ultimaVenda = vendasBanco[-1]
        idUltimaVenda = ultimaVenda[0]

        for id, cod, nome, preco, quantidade, total in itensLista:
            ItensVendaRepository.create(idUltimaVenda, id, quantidade, total)

        formPagBanco = FormasPagamentoRepository.read()
        for id, nome in formPagBanco:
            if nome == formaDePg:
                RecebimentoRepository.create(idUltimaVenda, id)





