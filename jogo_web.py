# Pedra, papel e tesoura — versão web
# Rode com:  streamlit run jogo_web.py
#
# ROTEIRO (escreva o código de cada passo embaixo do comentário):
#
# 1. importar o streamlit (como "st") e o random
#
# 2. criar as memórias dos placares, se ainda não existirem:
#    if "meus_pontos" not in st.session_state:
#        st.session_state.meus_pontos = 0
#    (faça o mesmo para os pontos do computador)
#
# 3. um título com st.title(...)
#
# 4. um if para cada botão:
#    if st.button("🪨 Pedra"):
#        ... sortear, comparar e somar na memória ...
#
# 5. mostrar o placar com st.write(...)
import streamlit as st
import random

if "meus_pontos" not in st.session_state:
    st.session_state.meus_pontos = 0
if "pontos_do_computador" not in st.session_state:
    st.session_state.pontos_do_computador = 0
if "tela" not in st.session_state:
    st.session_state.tela = "menu"
emojis = ["🪨", "📄", "✂️"]
emojis_de = {"pedra": "🪨", "papel": "📄", "tesoura": "✂️"}
faixa = ""
for i in range(20):
    faixa += random.choice(emojis) + " "
if st.session_state.tela == "menu":
    st.title("o melhor jogo de pedra, papel e tesoura do mundo")
    st.write("apenas um pedra, papel e tesoura")
    st.write(faixa)
    if st.button("jogar"):
       st.session_state.tela = "jogo"
       st.rerun()
    st.stop()

st.title("Pedra, Papel e tesoura")

jogada = ""

col1, col2, col3 = st.columns(3)
if col1.button("🪨 Pedra", use_container_width=True):
    jogada = "pedra"
if col2.button("📄 papel", use_container_width=True):
    jogada = "papel"
if col3.button("✂️ tesoura", use_container_width=True):
    jogada = "tesoura"
    
    
    
if jogada != "":
    opçoes = ["pedra", "papel", "tesoura"]
    sorteio = random.choice(opçoes)
    st.write(f"você: {emojis_de [jogada]} x computador: {emojis_de [sorteio]}")

    if jogada == sorteio:
        st.info("empate!")
    elif (jogada == "pedra" and sorteio == "tesoura") or (jogada == "papel" and sorteio == "pedra") or (jogada == "tesoura" and sorteio == "papel"):
        st.success("você ganhou!")
        st.session_state.meus_pontos += 1
    else:
        st.error("você perdeu!")
        st.session_state.pontos_do_computador += 1
c1, c2 = st.columns(2)
c1.metric("você", st.session_state.meus_pontos)
c2.metric("computador", st.session_state.pontos_do_computador)
if st.session_state.meus_pontos >= 3:
    st.balloons()
    st.success("parabens! você ganhou o jogo!")
if st.session_state.pontos_do_computador >=3:
    st.error("o computador ganhou o jogo! tente de novo")

if st.button("reiniciar placar"):
    st.session_state.meus_pontos = 0
    st.session_state.pontos_do_computador = 0