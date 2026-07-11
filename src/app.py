"""
Assistente Preditivo de Organização Acadêmica
App Streamlit — ponto de entrada da demo.

Rode com: streamlit run src/app.py
"""
import streamlit as st

st.set_page_config(page_title="Assistente Acadêmico", page_icon="📚")

st.title("📚 Assistente Preditivo de Organização Acadêmica")
st.write("Digite suas demandas da semana para organizar seu cronograma.")

# TODO: carregar modelo treinado
# import joblib
# modelo = joblib.load("src/model/modelo_risco_academico.pkl")

demanda = st.text_area("Suas demandas da semana", placeholder="Ex: Prova de Cálculo sexta de manhã")

if st.button("Organizar semana"):
    st.info("Em construção: aqui vai entrar o cronograma + o alerta de risco + a recomendação do LLM.")
