from entities.Categoria import Categoria
from entities.Produto import Produto
from entities.ItensVenda import ItensVenda
from entities.FormasPagamento import FormasPagamento
from entities.Compra import Compra
from repositorys.CategoriaRepository import CategoriaRepository
from repositorys.ProdutoRepository import ProdutoRepository
from repositorys.ItensVendaRepository import ItensVendaRepository
from repositorys.FormasPagamentoRepository import FormasPagamentoRepository
from repositorys.RecebimentoRepository import RecebimentoRepository
from helpers.Avisos import Aviso

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

largura_janela_root = 800
altura_janela_root = 500

largura_tela_root = root.winfo_screenwidth()
altura_tela_root = root.winfo_screenheight()

pos_x_root = int(largura_tela_root/2 - largura_janela_root/2)
pos_y_root = int(altura_tela_root/2 - altura_janela_root/2)

root.geometry(f"{largura_janela_root}x{altura_janela_root}+{pos_x_root}+{pos_y_root}")
root.configure(bg="#2E4053")
root.title("Controler")

framControler = tk.Frame(root)
framControler.config(bg="#808080")
framControler.pack(fill=tk.BOTH, padx=15, pady=15, expand=True)

labOpMenu = tk.Label(framControler)
labOpMenu.config(bg="#808080")
labOpMenu.pack(expand=True)

def janela_categorias():
    """
        Abre uma nova janela para cadastrar categorias.
    """

    categoiasJnl = tk.Tk()

    largura_janela_categoiasJnl = 800
    altura_janela_categoiasJnl = 720

    largura_tela_categoiasJnl = categoiasJnl.winfo_screenwidth()
    altura_tela_categoiasJnl = categoiasJnl.winfo_screenheight()

    pos_x_categoiasJnl = int(largura_tela_categoiasJnl / 2 - largura_janela_categoiasJnl / 2)
    pos_y_categoiasJnl = int(altura_tela_categoiasJnl / 2 - altura_janela_categoiasJnl / 2)

    categoiasJnl.geometry(f"{largura_janela_categoiasJnl}x{altura_janela_categoiasJnl}+{pos_x_categoiasJnl}+{pos_y_categoiasJnl}")
    categoiasJnl.configure(bg="#2E4053")
    categoiasJnl.title("Categorias")

    framCadCateg = tk.Frame(categoiasJnl)
    framCadCateg.config(bg="#808080", height=600, width=1200)
    framCadCateg.pack(fill=tk.BOTH, padx=15, pady=15, expand=True)

    labCadCateg = tk.Label(framCadCateg)
    labCadCateg.config(bg="#808080")
    labCadCateg.pack(expand=True)

    labCadCategTitle = tk.Label(labCadCateg, text='CADASTRAR CATEGORIAS')
    labCadCategTitle.config(bg="#808080", fg="white", font=("Arial", 20))
    labCadCategTitle.pack(padx=3, pady=20)

    '''
        TABELA CATEGORIA
    '''

    labTabelaCateg = tk.Label(labCadCateg)
    labTabelaCateg.config(bg="#2E4053", width=50)
    labTabelaCateg.pack(expand=True)

    tabelaCategorias = ttk.Treeview(labTabelaCateg, columns=('Id', 'Nome', 'QuantidadeDeProdutos'), show='headings')

    tabelaCategorias.heading('Id', text='Id')
    tabelaCategorias.heading('Nome', text='Nome')
    tabelaCategorias.heading('QuantidadeDeProdutos', text='Quantidade De Produtos')

    tabelaCategorias.config(height=20)
    tabelaCategorias.pack()

    '''
        INSERIR CATEGORIA
    '''

    labAdcCateg = tk.Label(labCadCateg)
    labAdcCateg.config(bg="#2E4053", fg="#ffffff", font=("Arial", 20), width=400)
    labAdcCateg.pack(pady=20)

    categoriaBanco = CategoriaRepository.read()
    for id, nome, qntd in categoriaBanco:
        tabelaCategorias.insert('', 'end', values=("{}".format(id), "{}".format(nome), "{}".format(qntd)))

    def adc_categoria():
        """
            Cadastra uma nova categoria.
        """

        valor = nomeCateg.get().strip()
        Categoria.cadastrar_categoria(valor.strip())
        try:
            tabelaCategorias.delete(*tabelaCategorias.get_children())
            categoriaBanco = CategoriaRepository.read()
            for id, nome, qntd in categoriaBanco:
                tabelaCategorias.insert('', 'end', values=("{}".format(id), "{}".format(nome), "{}".format(qntd)))

            nomeCateg.delete(0, 'end')

        except tk.TclError as erro:
            print("Erro ao atualizar a tabela: {}".format(erro))

    def del_categoria():
        """
            Deleta uma categoria que não tenha produtos.
        """

        selected_items = tabelaCategorias.selection()
        for item in selected_items:
            values = tabelaCategorias.item(item, 'values')
            Categoria.deletar_categoria(values[0], values[2])
            try:
                tabelaCategorias.delete(item)

            except tk.TclError as erro:
                print("Erro ao deletar item da tabela: {}".format(erro))

    nomeCateg = tk.Entry(labAdcCateg)
    nomeCateg.config(fg="#000013", font=("Arial", 18))
    nomeCateg.pack(padx=10, side=tk.LEFT)

    btnAdcCateg = tk.Button(labAdcCateg, text="Cadastrar", command=adc_categoria)
    btnAdcCateg.config(cursor="hand2", font=("Arial", 12))
    btnAdcCateg.pack(pady=10, side=tk.LEFT)

    btnDelCateg = tk.Button(labAdcCateg, text="Excluir", command=del_categoria)
    btnDelCateg.config(cursor="hand2", font=("Arial", 12))
    btnDelCateg.pack(pady=10, padx=10, side=tk.LEFT)

    def voltar_pro_menu():
        """
            Volta para o menu do programa.
        """

        root.deiconify()
        categoiasJnl.destroy()

    btnVoltarMenu = tk.Button(labCadCateg, text='Sair', command=voltar_pro_menu)
    btnVoltarMenu.config(cursor="hand2", height=1, width=7, font=("Arial", 14))
    btnVoltarMenu.pack(fill=tk.BOTH, side=tk.BOTTOM, anchor=tk.S, pady=10, padx=20)

    root.withdraw()
    while True:
        try:
            categoiasJnl.mainloop()
        except KeyboardInterrupt:
            break

def janela_produtos():
    """
        Abre uma nova janela para cadastrar produtos.
    """
    produtosJnl = tk.Tk()

    largura_janela_produtosJnl = 1200
    altura_janela_produtosJnl = 620

    largura_tela_produtosJnl = produtosJnl.winfo_screenwidth()
    altura_tela_produtosJnl = produtosJnl.winfo_screenheight()

    pos_x_produtosJnl = int(largura_tela_produtosJnl / 2 - largura_janela_produtosJnl / 2)
    pos_y_produtosJnl = int(altura_tela_produtosJnl / 2 - altura_janela_produtosJnl / 2)

    produtosJnl.geometry(f"{largura_janela_produtosJnl}x{altura_janela_produtosJnl}+{pos_x_produtosJnl}+{pos_y_produtosJnl}")
    produtosJnl.configure(bg="#2E4053")
    produtosJnl.title("Produtos")

    framCadProd = tk.Frame(produtosJnl)
    framCadProd.config(bg="#808080", height=600, width=1200)
    framCadProd.pack(fill=tk.BOTH, padx=15, pady=15, expand=True)

    labCadProd = tk.Label(framCadProd)
    labCadProd.config(bg="#808080")
    labCadProd.pack(expand=True)

    labCadProdTitle = tk.Label(labCadProd, text='CADASTRAR PRODUTOS')
    labCadProdTitle.config(bg="#808080", fg="white", font=("Arial", 20))
    labCadProdTitle.pack(padx=3, pady=10)

    labProd = tk.Label(labCadProd)
    labProd.config(bg="#808080")
    labProd.pack(expand=True)

    '''
        TABELA PRODUTOS
    '''

    labTabelaProd = tk.Label(labProd)
    labTabelaProd.config(bg="#2E4053", width=40)
    labTabelaProd.pack(side=tk.LEFT, expand=True, padx=20)
    tabelaProdutos = ttk.Treeview(labTabelaProd, columns=('Id', 'Codigo','Nome', 'Preco', 'Quantidade', 'Categoria'), show='headings')

    tabelaProdutos.heading('Id', text='Id')
    tabelaProdutos.heading('Codigo', text='Código')
    tabelaProdutos.heading('Nome', text='Nome')
    tabelaProdutos.heading('Preco', text='Preço (R$)')
    tabelaProdutos.heading('Quantidade', text='Quantidade')
    tabelaProdutos.heading('Categoria', text='Categoria')

    tabelaProdutos.column(0, width=50)
    tabelaProdutos.column(1, width=100)
    tabelaProdutos.column(2, width=260)
    tabelaProdutos.column(3, width=100)
    tabelaProdutos.column(4, width=100)
    tabelaProdutos.column(5, width=160)

    tabelaProdutos.config(height=20)
    tabelaProdutos.pack()

    '''
        INSERIR PRODUTOS
    '''

    labAdcProd = tk.Label(labProd)
    labAdcProd.config(bg="#2E4053", fg="#ffffff", font=("Arial", 20), width=400)
    labAdcProd.pack(side=tk.LEFT, pady=50)

    produtoBanco = ProdutoRepository.read()
    categoriaBanco = CategoriaRepository.read()
    nomeCategProd = ''

    for id, cod, nome, preco, qntd, categoria in produtoBanco:
        for idCateg, nomeCateg, qntdCateg in categoriaBanco:
            if categoria == idCateg:
                nomeCategProd = nomeCateg

        tabelaProdutos.insert('', 'end', values=("{}".format(id), "{}".format(cod), "{}".format(nome), "{}".format(preco), "{}".format(qntd), "{}".format(nomeCategProd)))

    def adc_produto():
        """
            Cadastra um novo produto.
        """

        codigo = inputCodProd.get().strip()
        nome = inputNomeProd.get().strip()
        preco = inputPrecoProd.get().strip()
        categoria = opCategProd.get().strip()

        Produto.cadastrar_produto(codigo, nome.strip(), preco, categoria.strip())
        try:
            tabelaProdutos.delete(*tabelaProdutos.get_children())
            produtoBanco = ProdutoRepository.read()
            categoriaBanco = CategoriaRepository.read()
            nomeCategProd = ''

            for id, cod, nome, preco, qntd, categoria in produtoBanco:
                for idCateg, nomeCateg, qntdCateg in categoriaBanco:
                    if categoria == idCateg:
                        nomeCategProd = nomeCateg

                tabelaProdutos.insert('', 'end', values=("{}".format(id), "{}".format(cod), "{}".format(nome), "{}".format(preco), "{}".format(qntd), "{}".format(nomeCategProd)))

            inputCodProd.delete(0, 'end')
            inputNomeProd.delete(0, 'end')
            inputPrecoProd.delete(0, 'end')
            opCategProd.delete(0, 'end')

        except tk.TclError as erro:
            print("Erro ao atualizar a tabela: {}".format(erro))

    def del_produto():
        """
            Deleta um produto que nunca tenha sido vendido.
        """

        selected_items = tabelaProdutos.selection()
        for item in selected_items:
            values = tabelaProdutos.item(item, 'values')
            deleteValido = 'YES'

            itVendasBanco = ItensVendaRepository.read()
            for id, idVenda, idProduto, qntdVenda, valorVenda in itVendasBanco:
                if idProduto == int(values[0]):
                    deleteValido = 'NO'

            if deleteValido != 'NO':
                Produto.deletar_produto(values[0])
                tabelaProdutos.delete(item)

            else:
                Aviso.mostar_aviso("Erro ao excluir produto ")

    labCodProd = tk.Label(labAdcProd)
    labCodProd.configure(bg="#2E4053")
    labCodProd.pack(padx=10, pady=6)
    codProd = tk.Label(labCodProd, text="Código do Produto:")
    codProd.config(bg="#2E4053", fg="#ffffff", font=("Arial", 12))
    codProd.pack(padx=10, anchor=tk.W)
    inputCodProd = tk.Entry(labCodProd)
    inputCodProd.config(fg="#000013", font=("Arial", 16))
    inputCodProd.pack(padx=10)

    labNomeProd = tk.Label(labAdcProd)
    labNomeProd.configure(bg="#2E4053")
    labNomeProd.pack(padx=10, pady=6)
    nomeProd = tk.Label(labNomeProd, text="Nome do Produto:")
    nomeProd.config(bg="#2E4053", fg="#ffffff", font=("Arial", 12))
    nomeProd.pack(padx=10, anchor=tk.W)
    inputNomeProd = tk.Entry(labNomeProd)
    inputNomeProd.config(fg="#000013", font=("Arial", 16))
    inputNomeProd.pack(padx=10)

    labPrecoProd = tk.Label(labAdcProd)
    labPrecoProd.configure(bg="#2E4053")
    labPrecoProd.pack(padx=10, pady=6)
    precoProd = tk.Label(labPrecoProd, text="Preço do Produto:")
    precoProd.config(bg="#2E4053", fg="#ffffff", font=("Arial", 12))
    precoProd.pack(padx=10, anchor=tk.W)
    inputPrecoProd = tk.Entry(labPrecoProd)
    inputPrecoProd.config(fg="#000013", font=("Arial", 16))
    inputPrecoProd.pack(padx=10)

    labCategProd = tk.Label(labAdcProd)
    labCategProd.configure(bg="#2E4053")
    labCategProd.pack(padx=10, pady=6)
    categProd = tk.Label(labCategProd, text="Categoria do Produto:")
    categProd.config(bg="#2E4053", fg="#ffffff", font=("Arial", 12))
    categProd.pack(anchor=tk.W)

    categoriasBanco = CategoriaRepository.read()
    opCateg = []

    for id, nome, qntd in categoriasBanco:
        opCateg.append(nome)

    opCateg = sorted(opCateg, reverse=False)

    opCategProd = ttk.Combobox(labCategProd, values=opCateg, state='normal')
    opCategProd.config(font=("Arial", 16), width=19)
    opCategProd.pack()

    labBtnsProd = tk.Label(labAdcProd)
    labBtnsProd.configure(bg="#2E4053")
    labBtnsProd.pack(padx=10, pady=6)
    btnAdcProd = tk.Button(labBtnsProd, text="Cadastrar", command=adc_produto)
    btnAdcProd.config(cursor="hand2", font=("Arial", 12))
    btnAdcProd.pack(pady=10, side=tk.LEFT)

    btnDelProd = tk.Button(labBtnsProd, text="Excluir", command=del_produto)
    btnDelProd.config(cursor="hand2", font=("Arial", 12))
    btnDelProd.pack(pady=10, padx=10, side=tk.LEFT)

    def voltar_pro_menu():
        """
            Volta para o menu do programa.
        """

        root.deiconify()
        produtosJnl.destroy()

    btnVoltarMenu = tk.Button(labCadProd, text='Sair', command=voltar_pro_menu)
    btnVoltarMenu.config(cursor="hand2", height=1, width=7, font=("Arial", 14))
    btnVoltarMenu.pack(fill=tk.BOTH, side=tk.BOTTOM, anchor=tk.S, pady=10, padx=20)

    root.withdraw()
    while True:
        try:
            produtosJnl.mainloop()
        except KeyboardInterrupt:
            break

def janela_estoque():
    """
        Abre uma nova janela para adicionar e remover produtos em estoque.
    """

    estoqueJnl = tk.Tk()

    largura_janela = 1200
    altura_janela = 600

    largura_tela = estoqueJnl.winfo_screenwidth()
    altura_tela = estoqueJnl.winfo_screenheight()

    pos_x = int(largura_tela / 2 - largura_janela / 2)
    pos_y = int(altura_tela / 2 - altura_janela / 2)

    estoqueJnl.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    estoqueJnl.configure(bg="#2E4053")
    estoqueJnl.title("Produtos")

    framEstoque = tk.Frame(estoqueJnl)
    framEstoque.config(bg="#808080", height=600, width=1200)
    framEstoque.pack(fill=tk.BOTH, padx=15, pady=15, expand=True)

    labEstoque = tk.Label(framEstoque)
    labEstoque.config(bg="#808080")
    labEstoque.pack(expand=True)

    labEstoqueTitle = tk.Label(labEstoque, text='Estoque')
    labEstoqueTitle.config(bg="#808080", fg="white", font=("Arial", 20))
    labEstoqueTitle.pack(padx=3, pady=10)

    labEstoq = tk.Label(labEstoque)
    labEstoq.config(bg="#808080")
    labEstoq.pack(expand=True)

    '''
        TABELA PRODUTOS
    '''

    def on_select(event):
        """
            Passa o código do item na linha selecionada para um input.
        """

        try:
            selected_items = tabelaProdutos.selection()
            for item in selected_items:
                values = tabelaProdutos.item(item, 'values')

            inputCodProd.delete(0, 'end')
            inputCodProd.insert(0, values[1])

        except Exception as erro:
            print(erro)

    labTabelaProd = tk.Label(labEstoq)
    labTabelaProd.config(bg="#2E4053", width=40)
    labTabelaProd.pack(side=tk.LEFT, expand=True, padx=20)

    tabelaProdutos = ttk.Treeview(labTabelaProd, columns=('Id', 'Codigo','Nome', 'Preco', 'Quantidade', 'Categoria'), show='headings')

    tabelaProdutos.heading('Id', text='Id')
    tabelaProdutos.heading('Codigo', text='Código')
    tabelaProdutos.heading('Nome', text='Nome')
    tabelaProdutos.heading('Preco', text='Preço (R$)')
    tabelaProdutos.heading('Quantidade', text='Quantidade')
    tabelaProdutos.heading('Categoria', text='Categoria')

    tabelaProdutos.column(0, width=50)
    tabelaProdutos.column(1, width=100)
    tabelaProdutos.column(2, width=260)
    tabelaProdutos.column(3, width=100)
    tabelaProdutos.column(4, width=100)
    tabelaProdutos.column(5, width=160)

    tabelaProdutos.config(height=20)
    tabelaProdutos.pack()

    '''
        ESTOQUE DOS PRODUTOS
    '''

    labAdcEstoq = tk.Label(labEstoq)
    labAdcEstoq.config(bg="#2E4053", fg="#ffffff", font=("Arial", 20), width=400)
    labAdcEstoq.pack(side=tk.LEFT, pady=50)

    produtoBanco = ProdutoRepository.read()
    categoriaBanco = CategoriaRepository.read()
    nomeCategProd = ''

    for id, cod, nome, preco, qntd, categoria in produtoBanco:
        for idCateg, nomeCateg, qntdCateg in categoriaBanco:
            if categoria == idCateg:
                nomeCategProd = nomeCateg

        tabelaProdutos.insert('', 'end', values=("{}".format(id), "{}".format(cod), "{}".format(nome), "{}".format(preco), "{}".format(qntd), "{}".format(nomeCategProd)))

    tabelaProdutos.bind("<ButtonRelease-1>", on_select)

    def adicionar_estoque():
        """
            Adiciona uma quantidade do produto no estoque.
        """

        codigo = inputCodProd.get().strip()
        quantidade = inputQntdProd.get().strip()
        Produto.estoque("ADICIONAR", codigo, quantidade)

        try:
            tabelaProdutos.delete(*tabelaProdutos.get_children())
            produtoBanco = ProdutoRepository.read()
            categoriaBanco = CategoriaRepository.read()
            nomeCategProd = ''

            for id, cod, nome, preco, qntd, categoria in produtoBanco:
                for idCateg, nomeCateg, qntdCateg in categoriaBanco:
                    if categoria == idCateg:
                        nomeCategProd = nomeCateg

                tabelaProdutos.insert('', 'end', values=("{}".format(id), "{}".format(cod), "{}".format(nome), "{}".format(preco), "{}".format(qntd), "{}".format(nomeCategProd)))

            inputCodProd.delete(0, 'end')
            inputQntdProd.delete(0, 'end')

        except tk.TclError as erro:
            print("Erro ao atualizar a tabela: {}".format(erro))

    def remover_estoque():
        """
            Remove uma quantidade do produto no estoque.
        """

        codigo = inputCodProd.get().strip()
        quantidade = inputQntdProd.get().strip()
        Produto.estoque("REMOVER", codigo, quantidade)

        try:
            tabelaProdutos.delete(*tabelaProdutos.get_children())
            produtoBanco = ProdutoRepository.read()
            categoriaBanco = CategoriaRepository.read()
            nomeCategProd = ''

            for id, cod, nome, preco, qntd, categoria in produtoBanco:
                for idCateg, nomeCateg, qntdCateg in categoriaBanco:
                    if categoria == idCateg:
                        nomeCategProd = nomeCateg

                tabelaProdutos.insert('', 'end', values=(
                "{}".format(id), "{}".format(cod), "{}".format(nome), "{}".format(preco), "{}".format(qntd),
                "{}".format(nomeCategProd)))

            inputCodProd.delete(0, 'end')
            inputQntdProd.delete(0, 'end')

        except tk.TclError as erro:
            print("Erro ao atualizar a tabela: {}".format(erro))

    labCodProd = tk.Label(labAdcEstoq)
    labCodProd.configure(bg="#2E4053")
    labCodProd.pack(padx=10, pady=6)
    codProd = tk.Label(labCodProd, text="Código do Produto:")
    codProd.config(bg="#2E4053", fg="#ffffff", font=("Arial", 12))
    codProd.pack(padx=10, anchor=tk.W)
    inputCodProd = tk.Entry(labCodProd)
    inputCodProd.config(fg="#000013", font=("Arial", 16))
    inputCodProd.pack(padx=10)

    labQntdProd = tk.Label(labAdcEstoq)
    labQntdProd.configure(bg="#2E4053")
    labQntdProd.pack(padx=10, pady=6)
    qntdProd = tk.Label(labQntdProd, text="Quantidade:")
    qntdProd.config(bg="#2E4053", fg="#ffffff", font=("Arial", 12))
    qntdProd.pack(padx=10, anchor=tk.W)
    inputQntdProd = tk.Entry(labQntdProd)
    inputQntdProd.config(fg="#000013", font=("Arial", 16))
    inputQntdProd.pack(padx=10)

    labBtnsProd = tk.Label(labAdcEstoq)
    labBtnsProd.configure(bg="#2E4053")
    labBtnsProd.pack(padx=10, pady=6)
    btnAddProd = tk.Button(labBtnsProd, text="Adicionar", command=adicionar_estoque)
    btnAddProd.config(cursor="hand2", font=("Arial", 12))
    btnAddProd.pack(pady=10, side=tk.LEFT)
    btnRmvProd = tk.Button(labBtnsProd, text="Remover", command=remover_estoque)
    btnRmvProd.config(cursor="hand2", font=("Arial", 12))
    btnRmvProd.pack(pady=10, padx=10, side=tk.LEFT)

    def voltar_pro_menu():
        """
            Volta para o menu do programa.
        """

        root.deiconify()
        estoqueJnl.destroy()

    btnVoltarMenu = tk.Button(labEstoque, text='Sair', command=voltar_pro_menu)
    btnVoltarMenu.config(cursor="hand2", height=1, width=7, font=("Arial", 14))
    btnVoltarMenu.pack(fill=tk.BOTH, side=tk.BOTTOM, anchor=tk.S, pady=20, padx=20)

    root.withdraw()
    while True:
        try:
            estoqueJnl.mainloop()
        except KeyboardInterrupt:
            break

def janela_vendas():
    """
        Abre uma nova janela para gerenciar as compras dos clientes.
    """

    def atualizarPreco(novoPreco):
        displayPrecoLab.config(text=str(novoPreco))
        displayPreco.set(novoPreco)

    def puxarPreco():
        return displayPreco.get()

    vendasJnl = tk.Tk()

    largura_janela = 800
    altura_janela = 400

    largura_tela = vendasJnl.winfo_screenwidth()
    altura_tela = vendasJnl.winfo_screenheight()

    pos_x = int(largura_tela / 2 - largura_janela / 2)
    pos_y = int(altura_tela / 2 - altura_janela / 2)

    vendasJnl.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    vendasJnl.configure(bg="#2E4053")
    vendasJnl.title("Vendas")

    framVendas = tk.Frame(vendasJnl)
    framVendas.config(bg="#808080")
    framVendas.pack(fill=tk.BOTH, padx=15, pady=15, expand=True)

    labCadVendas = tk.Label(framVendas)
    labCadVendas.config(bg="#808080")
    labCadVendas.pack(expand=True)

    labVend = tk.Label(labCadVendas)
    labVend.config(bg="#808080")
    labVend.pack(expand=True)

    produtoBanco = ProdutoRepository.read()

    '''
        VENDA
    '''

    itensVenda = []
    lista = []
    valorTotal = 0.0

    '''
        TABELA VENDA
    '''

    labItensVenda = tk.Label(labVend)
    labItensVenda.config(bg="#2E4053", width=40)
    labItensVenda.pack(side=tk.LEFT, expand=True, padx=20, anchor=tk.N)

    labTabelaVenda = tk.Label(labItensVenda)
    labTabelaVenda.config(bg="#2E4053", width=40)
    labTabelaVenda.pack(side=tk.LEFT, expand=True, padx=5)

    tabelaVendaTitle = tk.Label(labTabelaVenda, text='LISTA DE COMPRAR')
    tabelaVendaTitle.config(bg="#2E4053", fg="white", font=("Arial", 20))
    tabelaVendaTitle.pack(padx=3, pady=10)

    tabelaVenda = ttk.Treeview(labTabelaVenda, columns=('Id', 'Codigo', 'Nome', 'Preco', 'Quantidade', 'PrecoTotal'), show='headings')

    tabelaVenda.heading('Id', text='Id')
    tabelaVenda.heading('Codigo', text='Código')
    tabelaVenda.heading('Nome', text='Nome')
    tabelaVenda.heading('Preco', text='Preço (R$)')
    tabelaVenda.heading('Quantidade', text='Quantidade')
    tabelaVenda.heading('PrecoTotal', text='Preço Total (R$)')

    tabelaVenda.column(0, width=50)
    tabelaVenda.column(1, width=100)
    tabelaVenda.column(2, width=260)
    tabelaVenda.column(3, width=100)
    tabelaVenda.column(4, width=100)
    tabelaVenda.column(5, width=100)

    tabelaVenda.config(height=20)
    tabelaVenda.pack(pady=6)

    labRmvItem = tk.Label(labTabelaVenda)
    labRmvItem.config(bg="#2E4053")
    labRmvItem.pack(side=tk.LEFT)

    def remover_da_compra():
        """
            Remove um produto da lista de compra do cliente.
        """

        valorTotal = 0.0
        selected_items = tabelaVenda.selection()
        for item in selected_items:
            values = tabelaVenda.item(item, 'values')
            for itens in itensVenda:
                if itens[0] == int(values[0]):
                    posicao = itensVenda.index(itens)
                    itensVenda.pop(posicao)
                    tabelaVenda.delete(item)

            for itens in itensVenda:
                valorTotal += itens[5]

            atualizarPreco(valorTotal)

    btnRemItem = tk.Button(labRmvItem, text='Remover Produto', command=remover_da_compra)
    btnRemItem.config(cursor="hand2", height=1, width=15, font=("Arial", 14))
    btnRemItem.pack(side=tk.LEFT, pady=10)

    def add_qntd_item():
        """
            Adiciona uma quantidade do produto na lista de compra do cliente.
        """

        valorTotal = 0.0
        selected_items = tabelaVenda.selection()
        for item in selected_items:
            values = tabelaVenda.item(item, 'values')
            valores = list(values)

            aumentoValido = 'NO'
            for i, produtos in enumerate(produtoBanco):
                produtos = list(produtos)
                if produtos[1] == valores[1]:
                    reducao = produtos[4] - 1
                    if reducao >= 0:
                        produtos[4] -= 1
                        produtoBanco[i] = tuple(produtos)
                        aumentoValido = 'YES'

            if aumentoValido == 'YES':
                for itens in itensVenda:
                    if itens[0] == int(valores[0]):
                        itens[4] += 1
                        itens[5] += float(valores[3])

                valores[4] = int(valores[4]) + 1
                valores[5] = float(valores[5]) + float(valores[3])
                tabelaVenda.item(selected_items, values=(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5]))

                for itens in itensVenda:
                    valorTotal += itens[5]

                atualizarPreco(valorTotal)

            else:
                Aviso.mostar_aviso("Sem quantidade em estoque!")

    def rem_qntd_item():
        """
            Remove uma quantidade do produto ou o produto da lista de compra do cliente.
        """

        valorTotal = 0.0
        selected_items = tabelaVenda.selection()
        for item in selected_items:
            values = tabelaVenda.item(item, 'values')
            valores = list(values)
            if int(valores[4]) > 1:
                for itens in itensVenda:
                    if itens[0] == int(valores[0]):
                        for i, produtos in enumerate(produtoBanco):
                            produtos = list(produtos)
                            if produtos[1] == itens[1]:
                                produtos[4] += 1
                                produtoBanco[i] = tuple(produtos)

                        itens[4] -= 1
                        itens[5] -= float(valores[3])

                valores[4] = int(valores[4]) - 1
                valores[5] = float(valores[5]) - float(valores[3])
                tabelaVenda.item(selected_items, values=(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5]))

            else:
                if int(valores[4]) > 0:
                    for itens in itensVenda:
                        if itens[0] == int(valores[0]):
                            for i, produtos in enumerate(produtoBanco):
                                produtos = list(produtos)
                                if produtos[1] == itens[1]:
                                    produtos[4] += 1
                                    produtoBanco[i] = tuple(produtos)

                for itens in itensVenda:
                    if itens[0] == int(valores[0]):
                        posicao = itensVenda.index(itens)
                        itensVenda.pop(posicao)
                        tabelaVenda.delete(item)

            for itens in itensVenda:
                valorTotal += itens[5]

            atualizarPreco(valorTotal)

    btnAddQntdItem = tk.Button(labRmvItem, text='Add', command=add_qntd_item)
    btnAddQntdItem.config(cursor="hand2", width=5, font=("Arial", 14))
    btnAddQntdItem.pack(side=tk.LEFT, pady=10, padx=20)
    btnRemQntdItem = tk.Button(labRmvItem, text='Rem', command=rem_qntd_item)
    btnRemQntdItem.config(cursor="hand2", width=5, font=("Arial", 14))
    btnRemQntdItem.pack(side=tk.RIGHT, pady=10)

    labTotalVenda = tk.Label(labTabelaVenda)
    labTotalVenda.config(bg="#595959")
    labTotalVenda.pack(side=tk.RIGHT, pady=20)
    labTotal = tk.Label(labTotalVenda, text="Total: R$")
    labTotal.config(bg="#595959", fg="#ffffff", font=("Arial", 14))
    labTotal.pack(side=tk.LEFT, anchor=tk.W)

    displayPreco = tk.StringVar()
    displayPreco.set("0")

    displayPrecoLab = tk.Label(labTotalVenda, text=displayPreco.get())
    displayPrecoLab.config(bg="#ffffff", fg="#000000", font=("Arial", 16), width=10)
    displayPrecoLab.pack(padx=20, pady=10)

    def adicionar_na_compra():
        """
            Adiciona os produtos do cliente na lista de compra dele.
        """

        try:
            valorTotal = 0.0
            codigo = inputCodVend.get().strip()
            quantidade = inputQntdVend.get().strip()
            lista = ItensVenda.adicionar_produto(codigo, quantidade, itensVenda)
            produtoNovo = "YES"

            if len(itensVenda) > 0 and len(lista) > 0:
                for itens in itensVenda:
                    if itens[0] == lista[0]:
                        produtoNovo = "NO"
                        itens[4] += lista[4]
                        itens[5] += lista[5]

            if produtoNovo == "YES":
                itensVenda.append(lista)

            quantidadeValida = 'NO'
            for i, produtos in enumerate(produtoBanco):
                produtos = list(produtos)
                if produtos[1] == codigo:
                    reducaoQntd = produtos[4] - int(quantidade)
                    if reducaoQntd >= 0:
                        produtos[4] = reducaoQntd
                        quantidadeValida = 'YES'
                        produtoBanco[i] = tuple(produtos)

            if quantidadeValida == 'YES':
                tabelaBusca.delete(*tabelaBusca.get_children())
                tabelaVenda.delete(*tabelaVenda.get_children())

                for id, cod, nome, preco, quantidade, total in itensVenda:
                    tabelaVenda.insert('', 'end', values=("{}".format(id), "{}".format(cod), "{}".format(nome), "{}".format(preco), "{}".format(quantidade), "{}".format(total)))

                inputCodVend.delete(0, 'end')
                inputQntdVend.delete(0, 'end')

                for itens in itensVenda:
                    valorTotal += itens[5]

                atualizarPreco(str(valorTotal))

            else:
                Aviso.mostar_aviso("Sem quantidade em estoque!")

        except tk.TclError as erro:
            print("Erro ao atualizar a tabela: {}".format(erro))

        except TypeError as erro:
            print(erro)

    '''
        BUSCA
    '''

    def on_select2(event):
        """
            Passa o codigo do item na linha selecionada para um input.
        """
        try:
            selected_items = tabelaBusca.selection()
            for item in selected_items:
                values = tabelaBusca.item(item, 'values')

            inputCodVend.delete(0, 'end')
            inputCodVend.insert(0, values[1])

        except Exception as erro:
            print(erro)

    labTabelaBusca = tk.Label(labVend)
    labTabelaBusca.config(bg="#2E4053")
    labTabelaBusca.pack(side=tk.LEFT, expand=True, anchor=tk.N)

    tabelaBuscaTitle = tk.Label(labTabelaBusca, text='BUSCA')
    tabelaBuscaTitle.config(bg="#2E4053", fg="white", font=("Arial", 20))
    tabelaBuscaTitle.pack(padx=3, pady=10)

    tabelaBusca = ttk.Treeview(labTabelaBusca, columns=('Id', 'Codigo', 'Nome', 'Preco', 'Quantidade', 'Categoria'), show='headings')

    tabelaBusca.heading('Id', text='Id')
    tabelaBusca.heading('Codigo', text='Código')
    tabelaBusca.heading('Nome', text='Nome')
    tabelaBusca.heading('Preco', text='Preço (R$)')
    tabelaBusca.heading('Quantidade', text='Quantidade')
    tabelaBusca.heading('Categoria', text='Categoria')

    def buscar_codigo():
        """
            Busca um produto cadastrado pelo código dele.
        """

        busca = inputBuscarProd.get().strip()

        try:
            tabelaBusca.delete(*tabelaBusca.get_children())

            categoriaBanco = CategoriaRepository.read()
            nomeCategProd = ''

            for id, cod, nome, preco, qntd, categoria in produtoBanco:
                for idCateg, nomeCateg, qntdCateg in categoriaBanco:
                    if categoria == idCateg:
                        nomeCategProd = nomeCateg

                if cod[:len(busca)] == busca:
                    tabelaBusca.insert('', 'end', values=("{}".format(id), "{}".format(cod), "{}".format(nome), "{}".format(preco), "{}".format(qntd), "{}".format(nomeCategProd)))

            inputBuscarProd.delete(0, 'end')

        except tk.TclError as erro:
            print("Erro ao atualizar a tabela: {}".format(erro))

    def buscar_nome():
        """
            Busca um produto cadastrado pelo nome dele.
        """

        busca = inputBuscarProd.get().strip()

        try:
            tabelaBusca.delete(*tabelaBusca.get_children())
            categoriaBanco = CategoriaRepository.read()
            nomeCategProd = ''

            for id, cod, nome, preco, qntd, categoria in produtoBanco:
                for idCateg, nomeCateg, qntdCateg in categoriaBanco:
                    if categoria == idCateg:
                        nomeCategProd = nomeCateg

                if nome[:len(busca)] == busca.upper():
                    tabelaBusca.insert('', 'end', values=("{}".format(id), "{}".format(cod), "{}".format(nome), "{}".format(preco), "{}".format(qntd), "{}".format(nomeCategProd)))

            inputBuscarProd.delete(0, 'end')

        except tk.TclError as erro:
            print("Erro ao atualizar a tabela: {}".format(erro))

    tabelaBusca.column(0, width=50)
    tabelaBusca.column(1, width=100)
    tabelaBusca.column(2, width=190)
    tabelaBusca.column(3, width=100)
    tabelaBusca.column(4, width=100)
    tabelaBusca.column(5, width=140)

    tabelaBusca.config(height=12)
    tabelaBusca.pack(pady=6)

    tabelaBusca.bind("<ButtonRelease-1>", on_select2)

    labBuscarProd = tk.Label(labTabelaBusca)
    labBuscarProd.configure(bg="#2E4053")
    labBuscarProd.pack(padx=10, pady=10)
    inputBuscarProd = tk.Entry(labBuscarProd)
    inputBuscarProd.config(fg="#000013", font=("Arial", 16))
    inputBuscarProd.pack(padx=10, side=tk.LEFT)
    btnBuscarCodigo = tk.Button(labBuscarProd, text='Buscar Código', command=buscar_codigo, default="active")
    btnBuscarCodigo.config(cursor="hand2", height=1, width=12, font=("Arial", 10))
    btnBuscarCodigo.pack(side=tk.LEFT, padx=3)
    btnBuscarNome = tk.Button(labBuscarProd, text='Buscar Nome', command=buscar_nome, default="active")
    btnBuscarNome.config(cursor="hand2", height=1, width=12, font=("Arial", 10))
    btnBuscarNome.pack(side=tk.LEFT, padx=3)


    labItemVenda = tk.Label(labTabelaBusca)
    labItemVenda.configure(bg="#2E4053")
    labItemVenda.pack(pady=20)
    labCodVend = tk.Label(labItemVenda)
    labCodVend.configure(bg="#2E4053")
    labCodVend.pack(padx=12, side=tk.LEFT)
    codVend = tk.Label(labCodVend, text="Código do Produto:")
    codVend.config(bg="#2E4053", fg="#ffffff", font=("Arial", 12))
    codVend.pack(padx=10, anchor=tk.W)
    inputCodVend = tk.Entry(labCodVend)
    inputCodVend.config(fg="#000013", font=("Arial", 16), width=17)
    inputCodVend.pack(padx=10)
    labQntdVend = tk.Label(labItemVenda)
    labQntdVend.configure(bg="#2E4053")
    labQntdVend.pack(padx=12, side=tk.LEFT)
    qntdVend = tk.Label(labQntdVend, text="Quantidade:")
    qntdVend.config(bg="#2E4053", fg="#ffffff", font=("Arial", 12))
    qntdVend.pack(padx=10, anchor=tk.W)
    inputQntdVend = tk.Entry(labQntdVend)
    inputQntdVend.config(fg="#000013", font=("Arial", 16), width=17)
    inputQntdVend.pack(padx=10)

    '''
        ITENS E FINALIZACAO
    '''

    labAdcVenda = tk.Label(labTabelaBusca)
    labAdcVenda.configure(bg="#595959")
    labAdcVenda.pack()
    btnAdcCompra = tk.Button(labAdcVenda, text='Adicionar na Compra', command=adicionar_na_compra, default="active")
    btnAdcCompra.config(cursor="hand2", height=1, width=25, font=("Arial", 14))
    btnAdcCompra.pack(side=tk.LEFT, padx=30, pady=20)

    def pagamento_compra():
        """
            Abre uma nova janela para a finalização da compra.
        """

        if puxarPreco() != '':
            pgtoJnl = tk.Tk()
            largura_janela_pgtoJnl = 500
            altura_janela_pgtoJnl = 250

            largura_tela_pgtoJnl = pgtoJnl.winfo_screenwidth()
            altura_tela_pgtoJnl = pgtoJnl.winfo_screenheight()

            pos_x_pgtoJnl = int(largura_tela_pgtoJnl / 2 - largura_janela_pgtoJnl / 2)
            pos_y_pgtoJnl = int(altura_tela_pgtoJnl / 2 - altura_janela_pgtoJnl / 2)

            pgtoJnl.geometry(f"{largura_janela_pgtoJnl}x{altura_janela_pgtoJnl}+{pos_x_pgtoJnl}+{pos_y_pgtoJnl}")
            pgtoJnl.title("Pagamento")
            pgtoJnl.configure(bg="#808080")

            labPag = tk.Label(pgtoJnl, text="Escolha a Forma de Pagamento:", font=("Arial", 14), fg="white", bg="#808080")
            labPag.pack(pady=10)

            formPagBanco = FormasPagamentoRepository.read()
            opFormPag = []

            for id, nome in formPagBanco:
                opFormPag.append(nome)

            opFormPag = sorted(opFormPag, reverse=False)

            opFormPagCompra = ttk.Combobox(pgtoJnl, values=opFormPag, state='normal')
            opFormPagCompra.config(font=("Arial", 16), width=19)
            opFormPagCompra.pack(pady=10)

            labVerTroco = tk.Label(pgtoJnl)
            labVerTroco.config(bg="#808080")
            labVerTroco.pack(pady=20)

            def calcular_troco():
                """
                    Calcula qual o troco do cliente com base no dinheiro que ele deu.
                """

                try:
                    valorRecebido = inputRecb.get()
                    valorDaCompra = puxarPreco()
                    valorDaCompra = str(valorDaCompra).replace(',', '.')

                    try:
                        if float(valorRecebido) > 0:
                            valorDoTroco = float(valorRecebido) - float(valorDaCompra)

                            if valorDoTroco >= 0:
                                inputTroco.delete(0, 'end')
                                inputTroco.insert(0, valorDoTroco)

                            else:
                                Aviso.mostar_aviso("Tá faltando R${}".format(valorDoTroco*-1))

                        else:
                            Aviso.mostar_aviso("Não é possivel pagar com R$0 ou menos!")

                    except ValueError as erro:
                        print(erro)

                except tk.TclError as erro:
                    print("Erro ao atualizar a tabela: {}".format(erro))

            labRecb = tk.Label(labVerTroco)
            labRecb.config(bg="#2E4053")
            labRecb.pack(side=tk.LEFT)
            txtRecb = tk.Label(labRecb, text="Valor Recebido: ")
            txtRecb.config(font=("Arial", 10), bg=("#2E4053"), fg=("#ffffff"))
            txtRecb.pack(anchor=tk.W)
            inputRecb = tk.Entry(labRecb)
            inputRecb.config(font=("Arial", 12), width=15, fg="#000013")
            inputRecb.pack()

            btnCalcular = tk.Button(labVerTroco, text="Calcular Troco", command=calcular_troco)
            btnCalcular.config(cursor="hand2", font=("Arial", 12))
            btnCalcular.pack(side=tk.LEFT, anchor=tk.S, padx=10)

            labTroco = tk.Label(labVerTroco)
            labTroco.config(bg="#2E4053")
            labTroco.pack(side=tk.RIGHT)
            txtTroco = tk.Label(labTroco, text="Troco da Compra: ")
            txtTroco.config(font=("Arial", 10), bg=("#2E4053"), fg=("#ffffff"))
            txtTroco.pack(anchor=tk.W)
            inputTroco = tk.Entry(labTroco)
            inputTroco.config(font=("Arial", 12), width=15, fg="#000013")
            inputTroco.pack()

            def finalizar_compra():
                """
                    Finaliza a compra e manda os dados da compra para a o banco de dados.
                """

                formaDePg = opFormPagCompra.get()
                if formaDePg.strip() != '':
                    total = float(puxarPreco())
                    Compra.finalizar_compra(total, itensVenda, formaDePg)

                    try:
                        tabelaVenda.delete(*tabelaVenda.get_children())
                        atualizarPreco(0)

                    except tk.TclError as erro:
                        print("Erro ao atualizar a tabela: {}".format(erro))

                    pgtoJnl.destroy()

                else:
                    Aviso.mostar_aviso("Adicione a forma de pagamento!")

            btnFinalizar = tk.Button(pgtoJnl, text="Finalizar", command=finalizar_compra)
            btnFinalizar.configure(cursor="hand2", height=1, width=8, font=("Arial", 14))
            btnFinalizar.pack()

            while True:
                try:
                    pgtoJnl.mainloop()
                except KeyboardInterrupt:
                    break

        else:
            Aviso.mostar_aviso("Adicione um item à lista de compras!")

    btnPagCompra = tk.Button(labAdcVenda, text='Pagamento', command=pagamento_compra, default="active")
    btnPagCompra.config(cursor="hand2", height=1, width=25, font=("Arial", 14))
    btnPagCompra.pack(side=tk.LEFT, padx=30, pady=20)

    vendasJnl.state('zoomed')
    vendasJnl.attributes('-fullscreen', False)
    def voltar_pro_menu():
        """
            Volta para o menu do programa.
        """

        root.deiconify()
        vendasJnl.destroy()

    btnVoltarMenu = tk.Button(labCadVendas, text='Sair', command=voltar_pro_menu)
    btnVoltarMenu.config(cursor="hand2", height=1, width=7, font=("Arial", 14))
    btnVoltarMenu.pack(side=tk.BOTTOM, anchor=tk.S, pady=40, padx=20)

    root.withdraw()
    while True:
        try:
            vendasJnl.mainloop()
        except KeyboardInterrupt:
            break

def janela_formaspgmt():
    """
        Abre uma nova janela para cadastrar as formas de pagamento.
    """

    formPagJnl = tk.Tk()

    largura_janela_formPagJnl = 800
    altura_janela_formPagJnl = 600

    largura_tela_formPagJnl = formPagJnl.winfo_screenwidth()
    altura_tela_formPagJnl = formPagJnl.winfo_screenheight()

    pos_x_formPagJnl = int(largura_tela_formPagJnl / 2 - largura_janela_formPagJnl / 2)
    pos_y_formPagJnl = int(altura_tela_formPagJnl / 2 - altura_janela_formPagJnl / 2)

    formPagJnl.geometry(f"{largura_janela_formPagJnl}x{altura_janela_formPagJnl}+{pos_x_formPagJnl}+{pos_y_formPagJnl}")
    formPagJnl.configure(bg="#2E4053")
    formPagJnl.title("Formas de Pagamento")

    framCadFormPag = tk.Frame(formPagJnl)
    framCadFormPag.config(bg="#000013", height=600, width=1200)
    framCadFormPag.pack(fill=tk.BOTH, padx=15, pady=15, expand=True)

    labCadFormPag = tk.Label(framCadFormPag)
    labCadFormPag.config(bg="#808080")
    labCadFormPag.pack(expand=True)

    labCadFormPagTitle = tk.Label(labCadFormPag, text='CADASTRAR FORMAS DE PAGAMENTO')
    labCadFormPagTitle.config(bg="#808080", fg="white", font=("Arial", 20))
    labCadFormPagTitle.pack(padx=3, pady=20)

    '''
        TABELA FORMAS DE PAGAMENTO
    '''

    labTabelaFormPag = tk.Label(labCadFormPag)
    labTabelaFormPag.config(bg="#2E4053", width=50)
    labTabelaFormPag.pack(expand=True)

    tabelaFormPag = ttk.Treeview(labTabelaFormPag, columns=('Id', 'Nome'), show='headings')

    tabelaFormPag.heading('Id', text='Id')
    tabelaFormPag.heading('Nome', text='Nome')

    tabelaFormPag.config(height=15)
    tabelaFormPag.pack()

    '''
        INSERIR FORMA DE PAGAMNETO
    '''

    labAdcFormPag = tk.Label(labCadFormPag)
    labAdcFormPag.config(bg="#2E4053", fg="#ffffff", font=("Arial", 20), width=400)
    labAdcFormPag.pack(pady=20)

    formPagBanco = FormasPagamentoRepository.read()
    for id, nome in formPagBanco:
        tabelaFormPag.insert('', 'end', values=("{}".format(id), "{}".format(nome)))

    def adc_formPag():
        """
            Cadastra uma forma de pagamento.
        """

        valor = nomeFormPag.get().strip()
        FormasPagamento.cadastrar_forma(valor.strip())
        try:
            tabelaFormPag.delete(*tabelaFormPag.get_children())
            formPagBanco = FormasPagamentoRepository.read()
            for id, nome in formPagBanco:
                tabelaFormPag.insert('', 'end', values=("{}".format(id), "{}".format(nome)))

            nomeFormPag.delete(0, 'end')

        except tk.TclError as erro:
            print("Erro ao atualizar a tabela: {}".format(erro))

    def del_formPag():
        """
            Deleta uma forma de pagamento.
        """

        selected_items = tabelaFormPag.selection()
        for item in selected_items:
            values = tabelaFormPag.item(item, 'values')
            deleteValido = 'YES'

            formPagBanco = FormasPagamentoRepository.read()
            recebBanco = RecebimentoRepository.read()

            for idFormPg, nomeFormP in formPagBanco:
                if idFormPg == int(values[0]):
                    for recebimento in recebBanco:
                        if recebimento[2] == idFormPg:
                            deleteValido = 'NO'

            if deleteValido != 'NO':
                tabelaFormPag.delete(item)

            else:
                Aviso.mostar_aviso("Erro ao excluir forma de pagamanto ")

    nomeFormPag = tk.Entry(labAdcFormPag)
    nomeFormPag.config(fg="#808080", font=("Arial", 18))
    nomeFormPag.pack(padx=10, side=tk.LEFT)

    btnAdcFormPag = tk.Button(labAdcFormPag, text="Cadastrar", command=adc_formPag)
    btnAdcFormPag.config(cursor="hand2", font=("Arial", 12))
    btnAdcFormPag.pack(pady=10, side=tk.LEFT)

    btnDelFormPag = tk.Button(labAdcFormPag, text="Excluir", command=del_formPag)
    btnDelFormPag.config(cursor="hand2", font=("Arial", 12))
    btnDelFormPag.pack(pady=10, padx=10, side=tk.LEFT)

    def voltar_pro_menu():
        """
            Volta para o menu do programa.
        """

        root.deiconify()
        formPagJnl.destroy()

    btnVoltarMenu = tk.Button(labCadFormPag, text='Sair', command=voltar_pro_menu)
    btnVoltarMenu.config(cursor="hand2", height=1, width=7, font=("Arial", 14))
    btnVoltarMenu.pack(fill=tk.BOTH, side=tk.BOTTOM, anchor=tk.S, pady=10, padx=20)

    root.withdraw()
    while True:
        try:
            formPagJnl.mainloop()
        except KeyboardInterrupt:
            break

'''
    TELA DE MENU
'''

labelOPTitle = tk.Label(labOpMenu, text='MENU')
labelOPTitle.config(bg="#808080", fg="white", font=("Arial", 20))
labelOPTitle.pack(padx=3, expand=True)

btnOPCateg = tk.Button(labOpMenu, text='Categorias', command=janela_categorias)
btnOPCateg.config(cursor="hand2", font=("Arial", 15), height=1, width=60)
btnOPCateg.pack(pady=10)

btnOPProd = tk.Button(labOpMenu, text='Produtos', command=janela_produtos)
btnOPProd.config(cursor="hand2", font=("Arial", 15), height=1, width=60)
btnOPProd.pack(pady=10)

btnOPEstq = tk.Button(labOpMenu, text='Estoque', command=janela_estoque)
btnOPEstq.config(cursor="hand2", font=("Arial", 15), height=1, width=60)
btnOPEstq.pack(pady=10)

btnOPVend = tk.Button(labOpMenu, text='Vendas', command=janela_vendas)
btnOPVend.config(cursor="hand2", font=("Arial", 15), height=1, width=60)
btnOPVend.pack(pady=10)

btnOPFag = tk.Button(labOpMenu, text='Formas de Pagamento', command=janela_formaspgmt)
btnOPFag.config(cursor="hand2", font=("Arial", 15), height=1, width=60)
btnOPFag.pack(pady=10)

root.mainloop()
