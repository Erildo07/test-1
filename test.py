import tkinter as tk
from tkinter import messagebox

def enviar():
    nome = entry_nome.get()
    email = entry_email.get()
    messagebox.showinfo("Dados do Formulário", f"Nome: {nome}\nEmail: {email}")

# Criando a janela principal
root = tk.Tk()
root.title("Formulário Simples")

# Criando os rótulos e campos de entrada
label_nome = tk.Label(root, text="Nome:")
label_nome.pack()

entry_nome = tk.Entry(root)
entry_nome.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()

# Criando o botão de enviar
botao_enviar = tk.Button(root, text="Enviar", command=enviar)
botao_enviar.pack()

# Executando o loop principal
root.mainloop()
