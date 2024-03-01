from tkinter import *

lista = {}


def add_item():
    novo_item = item.get().title()
    novo_qtd = qtd.get()
    lista[novo_item] = float(novo_qtd)
    item.delete(0, "end")
    qtd.delete(0, 'end')
    # caixa_saida.insert(END, f"{novo_item:<12} : {novo_qtd:>5.1f}\n")


def imprime_lista():
    for item, qtd in lista.items():
        caixa_saida.insert(END, f"{item:<12} : {qtd:>5.1f}\n")


def janela():
    jan = Tk()
    jan.title("Lista de Compras")
    inst = Label(jan, text="Aplicação para gerar lista de compras")
    inst.grid(padx=20, pady=10)

    quadro = Frame(jan, relief="raised", borderwidth=1)
    quadro.grid(padx=10, pady=10)

    rotulo_item = Label(quadro, text="Item:")
    rotulo_item.grid()
    global item
    item = Entry(quadro)
    item.grid(padx=30)
    rotulo_qtd = Label(quadro, text="Quantidade:")
    rotulo_qtd.grid()
    global qtd
    qtd = Entry(quadro)
    qtd.grid(padx=30)
    add = Button(quadro, text="  Adicionar Item  ", command=add_item)
    add.grid(pady=10)

    imprimir = Button(jan, text="  Visualizar Lista  ", command=imprime_lista)
    imprimir.grid(pady=10)
    global caixa_saida
    caixa_saida = Text(jan, width=50, height=10)
    caixa_saida.grid(padx=20)

    fechar = Button(jan, text="  Fechar  ", command="exit")
    fechar.grid(pady=10)

    jan.mainloop()


janela()
