from repositorys.ItensVendaRepository import ItensVendaRepository
from repositorys.VendasRepository import VendasRepository
from repositorys.FormasPagamentoRepository import FormasPagamentoRepository
from repositorys.RecebimentoRepository import RecebimentoRepository

class Compra:

    @staticmethod
    def finalizar_compra(valorTotal, itensLista, formaDePg):
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





