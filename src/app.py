"""
Assistente Preditivo de Organização Acadêmica
App Streamlit — demo funcional para o pitch.

Rode com: streamlit run src/app.py
"""
import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Assistente Acadêmico", page_icon="📚", layout="centered")

# ------------------------------------------------------------
# 1. Carregar o modelo treinado
# ------------------------------------------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "modelo_risco_academico.pkl")

@st.cache_resource
def carregar_modelo():
    return joblib.load(MODEL_PATH)

try:
    modelo = carregar_modelo()
    modelo_ok = True
except Exception as e:
    modelo_ok = False
    erro_modelo = str(e)

# ------------------------------------------------------------
# 2. Interface
# ------------------------------------------------------------
st.title("📚 Assistente Preditivo de Organização Acadêmica")
st.write(
    "Digite suas demandas da semana e responda algumas perguntas rápidas sobre "
    "seus hábitos de estudo — o assistente organiza sua semana **e** avisa se "
    "seu padrão atual está associado a risco de reprovação."
)

if not modelo_ok:
    st.error(
        "Não consegui carregar o modelo treinado. Rode o notebook "
        "`notebooks/desenvolvimento.ipynb` até o final para gerar o arquivo "
        "`src/model/modelo_risco_academico.pkl`."
    )
    st.caption(f"Detalhe técnico: {erro_modelo}")
    st.stop()

st.divider()

# --- Organização da semana (texto livre) ---
st.subheader("1. Suas demandas da semana")
st.caption("Dica: escreva uma demanda por linha, mencionando o dia (ex: 'sexta: prova de Cálculo')")
demanda = st.text_area(
    "Ex: Prova de Cálculo sexta de manhã / Ler artigo de Redes até quarta",
    placeholder="segunda: revisar exercícios de Redes\nquarta: ler artigo de Redes\nsexta: prova de Cálculo",
    height=140
)

# ------------------------------------------------------------
# Parser simples: identifica o dia da semana em cada linha
# ------------------------------------------------------------
DIAS_SEMANA = [
    ("segunda", "Segunda"), ("terça", "Terça"), ("terca", "Terça"),
    ("quarta", "Quarta"), ("quinta", "Quinta"), ("sexta", "Sexta"),
    ("sábado", "Sábado"), ("sabado", "Sábado"), ("domingo", "Domingo"),
]

def montar_cronograma(texto):
    cronograma = {dia: [] for _, dia in dict(DIAS_SEMANA).items()}
    sem_dia = []

    for linha in texto.split("\n"):
        linha = linha.strip()
        if not linha:
            continue
        linha_lower = linha.lower()
        dia_encontrado = None
        for chave, nome_dia in DIAS_SEMANA:
            if chave in linha_lower:
                dia_encontrado = nome_dia
                break

        if dia_encontrado:
            # remove o marcador de dia do texto exibido (ex: "sexta: prova" -> "prova")
            texto_tarefa = linha
            for chave, _ in DIAS_SEMANA:
                texto_tarefa = texto_tarefa.lower().replace(chave, "")
            texto_tarefa = texto_tarefa.strip(" :-–—").capitalize()
            cronograma[dia_encontrado].append(texto_tarefa if texto_tarefa else linha)
        else:
            sem_dia.append(linha)

    return cronograma, sem_dia

def exibir_cronograma(cronograma, sem_dia):
    dias_ordem = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    cols = st.columns(7)

    for col, dia in zip(cols, dias_ordem):
        with col:
            st.markdown(f"**{dia}**")
            tarefas = cronograma.get(dia, [])
            if tarefas:
                for t in tarefas:
                    # prova/trabalho em destaque (prioridade alta), leitura em tom normal
                    if any(p in t.lower() for p in ["prova", "trabalho", "avaliação", "avaliacao", "entrega"]):
                        st.error(t)
                    else:
                        st.info(t)
            else:
                st.caption("—")

    if sem_dia:
        st.caption("Sem dia identificado (adicione o dia da semana no texto para organizar):")
        for t in sem_dia:
            st.write(f"- {t}")

st.divider()

# --- Hábitos de estudo (usados pelo modelo) ---
st.subheader("2. Seus hábitos (para calcular o risco)")

col1, col2 = st.columns(2)

with col1:
    studytime = st.select_slider(
        "Tempo de estudo semanal",
        options=[1, 2, 3, 4],
        value=2,
        format_func=lambda x: {1: "<2h", 2: "2-5h", 3: "5-10h", 4: ">10h"}[x]
    )
    failures = st.number_input("Reprovações anteriores", min_value=0, max_value=4, value=0)
    absences = st.number_input("Faltas no período", min_value=0, max_value=93, value=4)
    goout = st.slider("Frequência que sai com amigos (1=baixa, 5=alta)", 1, 5, 3)

with col2:
    walc = st.slider("Consumo de álcool no fim de semana (1=baixo, 5=alto)", 1, 5, 2)
    dalc = st.slider("Consumo de álcool em dias de semana (1=baixo, 5=alto)", 1, 5, 1)
    higher = st.radio("Pretende cursar pós-graduação?", ["yes", "no"], horizontal=True)
    internet = st.radio("Tem acesso à internet em casa?", ["yes", "no"], horizontal=True)

disciplina = st.selectbox("Matéria de referência", ["matematica", "portugues"])

# ------------------------------------------------------------
# 3. Montar o input do modelo (defaults pros demais campos)
# ------------------------------------------------------------
def montar_input():
    return pd.DataFrame([{
        "school": "GP", "sex": "F", "age": 17, "address": "U", "famsize": "GT3",
        "Pstatus": "T", "Medu": 3, "Fedu": 3, "Mjob": "other", "Fjob": "other",
        "reason": "course", "guardian": "mother", "traveltime": 1,
        "studytime": studytime, "failures": failures,
        "schoolsup": "no", "famsup": "yes", "paid": "no", "activities": "no",
        "nursery": "yes", "higher": higher, "internet": internet, "romantic": "no",
        "famrel": 4, "freetime": 3, "goout": goout, "Dalc": dalc, "Walc": walc,
        "health": 3, "absences": absences, "disciplina": disciplina,
    }])

st.divider()

if st.button("🔍 Organizar semana e calcular risco", type="primary", use_container_width=True):

    if demanda.strip():
        st.subheader("📅 Seu cronograma da semana")
        cronograma, sem_dia = montar_cronograma(demanda)
        exibir_cronograma(cronograma, sem_dia)

    st.subheader("⚠️ Risco acadêmico calculado")

    X_input = montar_input()
    proba_aprovado = modelo.predict_proba(X_input)[0][1]
    proba_risco = 1 - proba_aprovado

    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.metric("Probabilidade de risco", f"{proba_risco*100:.0f}%")

    with col_b:
        if proba_risco >= 0.5:
            st.error("Seu padrão atual está associado a **alto risco** de reprovação.")
        elif proba_risco >= 0.3:
            st.warning("Seu padrão atual está associado a **risco moderado**.")
        else:
            st.success("Seu padrão atual está associado a **baixo risco**.")

    # --- Recomendação (regras simples agora; LLM entra depois) ---
    st.subheader("💡 Recomendação personalizada")
    recomendacoes = []
    if failures > 0:
        recomendacoes.append(
            "Você já teve reprovações antes — esse é o fator de maior peso no modelo. "
            "Priorize reforço na matéria onde reprovou."
        )
    if studytime <= 2:
        recomendacoes.append(
            "Seu tempo de estudo semanal está abaixo do padrão associado a aprovação "
            "nos dados analisados. Considere realocar ao menos 2h a mais por semana."
        )
    if absences > 10:
        recomendacoes.append(
            "Suas faltas estão em um patamar que historicamente reduz a chance de "
            "aprovação. Faltas acima de 10 no período pesam bastante no seu risco."
        )
    if goout >= 4 and walc >= 4:
        recomendacoes.append(
            "Frequência social alta combinada com consumo de álcool no fim de semana "
            "aparece como padrão de risco nos dados — não precisa cortar tudo, "
            "mas vale rever o equilíbrio antes de provas."
        )
    if not recomendacoes:
        recomendacoes.append(
            "Seu padrão atual está alinhado com o de alunos aprovados. Continue assim!"
        )

    for r in recomendacoes:
        st.write(f"- {r}")

    st.caption(
        "⚠️ Nota de transparência: essa é uma versão inicial com recomendações "
        "baseadas em regras. A versão completa usa um LLM para gerar recomendações "
        "mais personalizadas cruzando o cronograma da semana com esse risco calculado."
    )
