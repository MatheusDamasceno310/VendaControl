from repositorys.CategoriaRepository import CategoriaRepository
from helpers.Avisos import Aviso

class Categoria:
    def __init__(self, nomeCategoria):
        self.__nomeCategoria = nomeCategoria.upper()
        self.__qntdCategoria = 0

    def __str__(self):
        return self.nome_categoria

    @property
    def nome_categoria(self):
        return self.__nomeCategoria

    @nome_categoria.setter
    def nome_categoria(self, nomeCategoria):
        self.__nomeCategoria = nomeCategoria

    @property
    def qntd_categoria(self):
        return self.__qntdCategoria

    @qntd_categoria.setter
    def qntd_categoria(self, qntdCategoria):
        self.__qntdCategoria = qntdCategoria

    @staticmethod
    def cadastrar_categoria(nomeCategoria):
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
        if qntd == '0':
            CategoriaRepository.delete(id)

        else:
            Aviso.mostar_aviso("Essa categoria contém produtos!")

if __name__ == "__main__":
    Aviso.mostar_aviso("Sem categ")
