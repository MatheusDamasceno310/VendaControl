import tkinter as tk

class Aviso:
    """
    Classe responsável por exibir uma janela com uma mensagem.

    Static method::
        mostar_aviso(mensagem): Adiciona uma mensagem que vai ser exibida na janela.
    """

    @staticmethod
    def mostar_aviso(mensagem):
        """
        Adiciona uma mensagem que vai ser exibida na janela.

        Args:
            mensagem (str): A mensagem que vai ser exibida.

        Returns:
            None
        """

        aviso = tk.Tk()

        largura_janela = 400
        altura_janela = 130

        largura_tela = aviso.winfo_screenwidth()
        altura_tela = aviso.winfo_screenheight()

        pos_x = int(largura_tela / 2 - largura_janela / 2)
        pos_y = int(altura_tela / 2 - altura_janela / 2)

        aviso.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
        aviso.title("Aviso")
        aviso.configure(bg="#000013")

        msg_label = tk.Label(aviso, text=mensagem, font=("Arial", 14), fg="white", bg="#000013")
        msg_label.pack(pady=20)

        ok_button = tk.Button(aviso, text="OK", command=aviso.destroy)
        ok_button.configure(cursor="hand2", height=1, width=8)
        ok_button.pack()

        while True:
            try:
                aviso.mainloop()
            except KeyboardInterrupt:
                break