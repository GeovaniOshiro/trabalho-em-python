import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk

# , usecols=['Quantidade Vendida']

def carregar_dados():   
    df = pd.read_csv('dados.csv')
    print(df)

def exibir_grafico():
    df = pd.read_csv('dados.csv')
    Data = df['Data']
    Produto = df['Produto']
    Preco = df['PRECOS']
    qtd = df['Quantidade Vendida']
    dados1 = df.head()
    sns.pairplot(df)
    plt.show()
    texto.config(text= dados1)

root = tk.Tk()
root.title("Visualizador de Dadods")

btn = tk.Button(root, text="carregar Dados", command=carregar_dados)
btn.pack()

btn_grafico = tk.Button(root, text="Exbibir Grafico", command=exibir_grafico)
btn_grafico.pack()

texto = tk.Label(root, text='')
texto.pack()

root.mainloop()