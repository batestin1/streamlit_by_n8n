import streamlit as st
import requests

st.title("Jogo de Adivinhas com Pokémon")

def obter_pokemon():
    resposta = requests.get("https://pokeapi.co/api/v2/pokemon/random")
    dados = resposta.json()
    return dados["name"], dados["types"][0]["type"]["name"]

def jogar():
    pokemon, tipo = obter_pokemon()
    st.write("Adivinhe o nome do Pokémon!")
    resposta = st.text_input("Digite o nome do Pokémon")
    if resposta.lower() == pokemon:
        st.success("Acertou! O Pokémon é " + pokemon + " do tipo " + tipo)
    else:
        st.error("Errou! O Pokémon era " + pokemon + " do tipo " + tipo)

if st.button("Jogar"):
    jogar()