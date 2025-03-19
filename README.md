# Conversor de Moedas com API 💱

## Descrição
O **Conversor de Moedas com API** é um projeto desenvolvido em Python que permite ao usuário converter valores entre diferentes moedas, como **BRL** (real brasileiro), **USD** (dólar americano) e **EUR** (euro), utilizando uma API de câmbio em tempo real. O programa oferece uma interface simples e intuitiva desenvolvida com **Tkinter**, onde o usuário pode inserir o valor desejado e selecionar as moedas de origem e destino para obter o valor convertido.

Este projeto foi desenvolvido para pessoas que desejam realizar conversões de moedas de maneira rápida e prática, sem precisar abrir vários sites de câmbio.

## Tecnologias usadas
- **Python**: Linguagem de programação principal utilizada para o desenvolvimento.
- **Tkinter**: Biblioteca para criar a interface gráfica.
- **Requests**: Biblioteca para consumir a API de câmbio.
- **API ExchangeRate-API**: Fornece as taxas de câmbio em tempo real para converter moedas.

## Passo a passo para rodar

### 1. Instalar as dependências:
Para rodar o projeto, você precisa ter o **Python** instalado no seu computador. Depois, instale as bibliotecas necessárias com o seguinte comando:

```bash
pip install requests
```

### 2. Obter a chave da API:
O projeto utiliza a **ExchangeRate-API** para buscar as taxas de câmbio em tempo real. Você precisa se cadastrar e obter sua chave de API gratuita:
- Acesse: [ExchangeRate-API](https://www.exchangerate-api.com/)
- Após o cadastro, substitua `"SUA_API_KEY"` no código pela chave fornecida.

### 3. Rodar o projeto:
Depois de obter a chave da API e ajustar o código, basta rodar o arquivo Python:

```bash
python CambioAPP.py
```

A interface gráfica será aberta, e você poderá inserir o valor e escolher as moedas para realizar a conversão.

### 4. Interagir com a interface:
- Insira o valor que deseja converter no campo de texto.
- Escolha a moeda de origem (BRL, USD ou EUR).
- Escolha a moeda de destino (BRL, USD ou EUR).
- Clique no botão "Converter" para ver o valor convertido.


## Possíveis melhorias futuras

- **Suporte a mais moedas**: A API de câmbio pode ser expandida para incluir outras moedas, permitindo conversões mais diversificadas.
- **Histórico de conversões**: Adicionar uma funcionalidade para salvar o histórico de conversões realizadas, permitindo ao usuário consultar os valores convertidos previamente.
- **Interface com gráficos**: Incorporar gráficos que mostram a variação das taxas de câmbio ao longo do tempo.
- **Aprimorar a UI/UX**: Tornar a interface mais interativa e responsiva, com uma aparência mais moderna e agradável.
- **Cadastro de usuário**: Criar um sistema de login para que os usuários possam salvar suas preferências de moedas e históricos de conversão.

## 📝 Autor
**Arthur Abreu** - Desenvolvedor do CambioAPP
