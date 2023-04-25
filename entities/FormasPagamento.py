from repositorys.FormasPagamentoRepository import FormasPagamentoRepository
from helpers.Avisos import Aviso

class FormasPagamento:
    def __init__(self, nomeFormPag):
        self.__nomeFormPag = nomeFormPag.upper()

    def __str__(self):
        return self.nome_formPag

    @property
    def nome_formPag(self):
        return self.__nomeFormPag

    @nome_formPag.setter
    def nome_formPag(self, nomeFormPag):
        self.__nomeFormPag = nomeFormPag

    @staticmethod
    def cadastrar_forma(nomeFormPag):
        formPagBanco = FormasPagamentoRepository.read()
        formaValida = 'YES'
        formPag = FormasPagamento(nomeFormPag)

        if nomeFormPag != '':
            for id, nome in formPagBanco:
                if nome == formPag.nome_formPag:
                    formaValida = 'NO'

            if formaValida == 'YES':
                FormasPagamentoRepository.create(formPag.nome_formPag)

            else:
                Aviso.mostar_aviso("Forma de Pagamento já cadastrada!")

        else:
            Aviso.mostar_aviso("Não é possivel cadastrar forma em branco!")

    @staticmethod
    def deletar_forma(id):
        FormasPagamentoRepository.delete(id)

