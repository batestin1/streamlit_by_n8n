import streamlit as st
import requests
import random

st.title("Jogo de Forca - Rick e Morty")

def obter_personagem():
    resposta = requests.get("https://rickandmortyapi.com/api/character")
    dados = resposta.json()
    personagens = dados["results"]
    personagem = random.choice(personagens)
    return personagem["name"]

def jogar():
    personagem = obter_personagem()
    palavra = ["_"] * len(personagem)
    tentativas = 6
    st.write("Adivinhe o nome do personagem!")
    while tentativas > 0 and "_" in palavra:
        st.write(" ".join(palavra))
        letra = st.text_input("Digite uma letra")
        if letra in personagem:
            for i, l in enumerate(personagem):
                if l == letra:
                    palavra[i] = letra
        else:
            tentativas -= 1
            st.write(f"Incorreto! {tentativas} tentativas restantes")
    if "_" not in palavra:
        st.success("Acertou! O personagem é " + personagem)
    else:
        st.error("Errou! O personagem era " + personagem)

if st.button("Jogar"):
    jogar()