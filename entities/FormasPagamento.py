from repositorys.FormasPagamentoRepository import FormasPagamentoRepository
from helpers.Avisos import Aviso

class FormasPagamento:
    """
    Representa uma forma de pagamento.

    Static method::
        cadastrar_forma(nomeFormPag): Cadastra uma nova forma de pagamento.
        deletar_categoria(id, qntd): Deleta uma categoria.
    """

    def __init__(self, nomeFormPag):
        """
        Cria uma nova instância da classe FormasPagamento.

        Args:
            nomeFormPag (str): O nome da forma de pagamento a ser criada.

        Returns:
            None
        """

        self.__nomeFormPag = nomeFormPag.upper()

    def __str__(self):
        """
        Retorna o nome da forma de pagamento.

        Returns:
            str: O nome da forma de pagamento.
        """

        return self.nome_formPag

    @property
    def nome_formPag(self):
        """
        Getter para o nome da forma de pagamento.

        Returns:
            str: O nome da forma de pagamento.
        """

        return self.__nomeFormPag

    @nome_formPag.setter
    def nome_formPag(self, nomeFormPag):
        """
        Setter para o nome da forma de pagamento.

        Args:
            nomeFormPag (str): O novo nome da forma de pagamento.

        Returns:
            None
        """

        self.__nomeFormPag = nomeFormPag

    @staticmethod
    def cadastrar_forma(nomeFormPag):
        """
        Cadastra uma nova forma de pagamento.

        Args:
            nomeFormPag (str): O nome da forma de pagamento a ser cadastrada.

        Returns:
            None
        """

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
        """
        Deleta uma forma de pagamento.

        Args:
            id (int): O id da forma de pagamento a ser deletada.

        Returns:
            None
        """

        FormasPagamentoRepository.delete(id)

