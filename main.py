import streamlit as st
import random

st.title("Jogo de Quizz - Filmes de Terror")

# Perguntas e respostas
perguntas = {
    "Qual é o nome do vilão do filme O Exorcista?": ["Pazuzu", "Satanás", "Lúcifer", "Belzebu"],
    "Em que ano foi lançado o filme A Noite dos Mortos-Vivos?": ["1968", "1978", "1988", "1998"],
    "Qual é o nome da personagem principal do filme O Silêncio dos Inocentes?": ["Clarice Starling", "FBI Agente", "Hannibal Lecter", "Buffalo Bill"],
    "Qual é o nome do filme de terror que conta a história de um grupo de amigos que são perseguidos por um assassino?": ["Sexta-Feira 13", "O Terror de Halloween", "A Noite do Terror", "O Massacre da Serra Elétrica"],
}

respostas = {
    "Qual é o nome do vilão do filme O Exorcista?": "A",
    "Em que ano foi lançado o filme A Noite dos Mortos-Vivos?": "A",
    "Qual é o nome da personagem principal do filme O Silêncio dos Inocentes?": "A",
    "Qual é o nome do filme de terror que conta a história de um grupo de amigos que são perseguidos por um assassino?": "A",
}

# Função para jogar
def jogar():
    placar = 0
    for pergunta, alternativas in perguntas.items():
        st.write(pergunta)
        resposta = st.selectbox("Escolha a resposta", alternativas)
        if resposta == alternativas[ord(respostas[pergunta]) - ord('A')]:
            placar += 1
            st.success("Resposta correta!")
        else:
            st.error("Resposta incorreta!")
    st.write(f"Placar: {placar} pontos")

# Botão para jogar
if st.button("Jogar"):
    jogar()