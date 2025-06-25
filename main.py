### Calculadora de IMC
```python
import streamlit as st

# Título do aplicativo
st.title("Calculadora de IMC")

# Função para calcular o IMC
def calcular_imc(peso, altura):
    """
    Calcula o IMC com base no peso e altura.
    
    Parâmetros:
    peso (float): Peso em kg
    altura (float): Altura em metros
    
    Retorno:
    float: Valor do IMC
    """
    return peso / (altura ** 2)

# Interface para entrada de dados
st.subheader("Insira seus dados:")
peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
altura = st.number_input("Altura (m)", min_value=0.0, step=0.01)

# Botão para calcular o IMC
if st.button("Calcular IMC"):
    imc = calcular_imc(peso, altura)
    
    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Magreza"
    elif imc < 25:
        classificacao = "Normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    # Mostrar resultado
    st.success(f"Seu IMC é: {imc:.2f} - {classificacao}")
```

### App para Prever Preço de Casas
```python
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Título do aplicativo
st.title("App para Prever Preço de Casas")

# Dados de exemplo
dados = {
    "Tamanho": [100, 200, 300, 400, 500],
    "Preço": [100000, 200000, 300000, 400000, 500000]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Interface para entrada de dados
st.subheader("Insira o tamanho da casa:")
tamanho = st.number_input("Tamanho (m²)", min_value=0.0, step=0.1)

# Botão para prever o preço
if st.button("Prever Preço"):
    # Preparar dados para treinamento
    X = df[["Tamanho"]]
    y = df["Preço"]
    
    # Treinar modelo
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    # Fazer previsão
    preco = modelo.predict([[tamanho]])
    
    # Mostrar resultado
    st.success(f"O preço previsto é: R${preco[0]:.2f}")
```

### Dashboard com Dados de PIB do Brasil
```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Título do aplicativo
st.title("Dashboard com Dados de PIB do Brasil")

# Dados de exemplo
dados = {
    "Ano": [2010, 2011, 2012, 2013, 2014],
    "PIB": [1000, 1200, 1500, 1800, 2000]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Interface para upload de dados
st.subheader("Upload de dados:")
arquivo = st.file_uploader("Selecione um arquivo CSV", type=["csv"])

# Botão para mostrar gráfico
if st.button("Mostrar Gráfico"):
    if arquivo is not None:
        df = pd.read_csv(arquivo)
    
    # Mostrar gráfico
    fig = px.line(df, x="Ano", y="PIB")
    st.plotly_chart(fig)
    
    # Mostrar análise descritiva
    media = df["PIB"].mean()
    st.write(f"Média do PIB: {media:.2f}")
```

### Interface para Subir um CSV e Mostrar Estatísticas Básicas
```python
import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Interface para Subir um CSV e Mostrar Estatísticas Básicas")

# Interface para upload de dados
st.subheader("Upload de dados:")
arquivo = st.file_uploader("Selecione um arquivo CSV", type=["csv"])

# Botão para mostrar estatísticas
if st.button("Mostrar Estatísticas"):
    if arquivo is not None:
        df = pd.read_csv(arquivo)
        
        # Mostrar estatísticas básicas
        st.write("Estatísticas Básicas:")
        st.write(df.describe())
```

Esses exemplos demonstram como criar aplicações web simples utilizando Python e a biblioteca Streamlit para diferentes temas. Cada exemplo inclui uma interface de usuário, processamento de dados e visualização de resultados. Além disso, os códigos são comentados e incluem docstrings para facilitar a compreensão e o uso.