import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

st.title("Relatório de Análise de Dados")

def carregar_arquivo():
    arquivo = st.file_uploader("Selecione um arquivo CSV")
    if arquivo is not None:
        df = pd.read_csv(arquivo)
        return df

def analisar_dados(df):
    # Separa colunas numéricas e não numéricas
    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    colunas_nao_numericas = df.select_dtypes(exclude=[np.number]).columns

    # Gera describe para colunas numéricas
    describe = df[colunas_numericas].describe()

    # Gera contagem distinta para colunas não numéricas
    contagem_distinta = {}
    for coluna in colunas_nao_numericas:
        contagem_distinta[coluna] = df[coluna].value_counts()

    # Gera wordcloud para colunas não numéricas
    wordcloud = {}
    for coluna in colunas_nao_numericas:
        texto = ' '.join(df[coluna].astype(str))
        wordcloud[coluna] = WordCloud(width=800, height=400).generate(texto)

    return describe, contagem_distinta, wordcloud

def visualizar_analise(describe, contagem_distinta, wordcloud):
    st.write("Describe:")
    st.write(describe)

    st.write("Contagem Distinta:")
    for coluna, contagem in contagem_distinta.items():
        st.write(f"{coluna}:")
        st.write(contagem)

    st.write("Wordcloud:")
    for coluna, wc in wordcloud.items():
        st.write(f"{coluna}:")
        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        st.pyplot()

df = carregar_arquivo()
if df is not None:
    describe, contagem_distinta, wordcloud = analisar_dados(df)
    visualizar_analise(describe, contagem_distinta, wordcloud)