import tkinter as tk
from tkinter import messagebox
import requests

# Função para consultar a API de câmbio e converter o valor
def converter():
    try:
        moeda_origem = moeda_origem_var.get()
        moeda_destino = moeda_destino_var.get()
        valor = float(valor_entry.get())

        # URL da API de câmbio
        url = f"https://v6.exchangerate-api.com/v6/SUA_API_KEY/latest/{moeda_origem}"

        # Consultando a API
        resposta = requests.get(url)
        dados = resposta.json()

        if resposta.status_code == 200:
            # Verificando se a moeda de destino existe nos dados
            if moeda_destino in dados['conversion_rates']:
                taxa_conversao = dados['conversion_rates'][moeda_destino]
                valor_convertido = valor * taxa_conversao
                resultado_var.set(f"Valor convertido: {valor_convertido:.2f} {moeda_destino}")
            else:
                messagebox.showerror("Erro", "Moeda de destino inválida.")
        else:
            messagebox.showerror("Erro", "Falha ao consultar a API.")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Criação da interface gráfica com Tkinter
root = tk.Tk()
root.title("cambio APP")
root.geometry("400x300")

# Variáveis para entrada e exibição
moeda_origem_var = tk.StringVar(value="BRL")
moeda_destino_var = tk.StringVar(value="USD")
resultado_var = tk.StringVar()

# Rótulos e entradas para a interface
tk.Label(root, text="Valor a ser convertido:").pack(pady=5)
valor_entry = tk.Entry(root)
valor_entry.pack(pady=5)

tk.Label(root, text="Escolha a moeda de origem:").pack(pady=5)
moedas_origem = ["BRL", "USD", "EUR"]
moeda_origem_menu = tk.OptionMenu(root, moeda_origem_var, *moedas_origem)
moeda_origem_menu.pack(pady=5)

tk.Label(root, text="Escolha a moeda de destino:").pack(pady=5)
moedas_destino = ["BRL", "USD", "EUR"]
moeda_destino_menu = tk.OptionMenu(root, moeda_destino_var, *moedas_destino)
moeda_destino_menu.pack(pady=5)

# Botão para realizar a conversão
converter_button = tk.Button(root, text="Converter", command=converter)
converter_button.pack(pady=10)

# Rótulo para exibir o resultado
tk.Label(root, textvariable=resultado_var, font=("Helvetica", 12)).pack(pady=10)

# Iniciar a interface
root.mainloop()
