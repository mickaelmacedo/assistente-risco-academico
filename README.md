# 📚 [Nome do Projeto] — Assistente Preditivo de Organização Acadêmica

> Organiza sua semana e avisa, com base em dados reais, quando seu padrão de estudo está te levando à reprovação.

---

## 👥 Equipe

| Nome completo | Papel no projeto |
|---|---|
| [Nome 1] | [ex: Modelagem / ML] |
| [Nome 2] | [ex: Front-end / Streamlit] |
| [Nome 3] | [ex: Dados / EDA] |
| [Nome 4] | [ex: LLM / Prompt engineering] |

---

## 🎯 O Problema

Estudantes universitários lidam com múltiplas demandas simultâneas (provas, leituras, trabalhos em grupo) e costumam perceber que estão em risco de reprovação só quando já é tarde — quando as notas parciais já caíram.

Ferramentas de organização tradicionais (agenda, Google Calendar, apps de produtividade) resolvem o problema de **"o que fazer"**, mas não o de **"o que vai acontecer se eu continuar assim"**. Não existe, na maioria dos apps de estudo, um sinal de alerta baseado em padrões reais de comportamento acadêmico.

Esse é o problema que o [Nome do Projeto] resolve: transformar o registro de demandas da semana em um cronograma **e** em um alerta preditivo de risco acadêmico, com recomendações concretas — não genéricas — para reverter o quadro.

---

## 💡 A Solução

O aluno digita livremente suas demandas da semana (ex: *"Ler o artigo de Redes para quarta"*, *"Prova de Cálculo sexta de manhã"*). O sistema:

1. **Organiza** — identifica matéria, tipo de tarefa e prioridade, e monta um cronograma visual da semana.
2. **Avalia risco** — cruza o padrão de estudo do aluno (tempo dedicado, faltas, histórico) com um modelo preditivo treinado em dados reais de desempenho acadêmico, sinalizando risco por matéria.
3. **Recomenda** — um LLM traduz o sinal de risco em orientação prática e personalizada (ex: *"seu tempo de estudo em Cálculo está bem abaixo do padrão associado a bons resultados — considere realocar horas de [matéria X]"*), em vez de conselhos genéricos como "estude mais".

**[Inserir aqui print ou GIF da demo rodando]**

---

## 🧠 Técnicas Usadas

| Técnica | Onde é usada | Por quê |
|---|---|---|
| [ex: Regressão Logística / Random Forest] | Predição de risco de reprovação | [justificar: interpretabilidade, lida bem com poucas features, etc.] |
| [ex: Análise Exploratória de Dados] | Entender padrões no dataset | Identificar quais variáveis (faltas, tempo de estudo, reprovações anteriores) mais influenciam o resultado |
| [ex: LLM via API] | Geração de recomendações personalizadas | Traduz saída numérica do modelo em linguagem natural acionável |
| [ex: NLP simples / regras] | Interpretar demandas em texto livre | Extrair matéria, tipo de tarefa e urgência do texto digitado pelo aluno |

Modelo(s) treinado(s) com base no **Student Performance Dataset** (Cortez & Silva, UCI Machine Learning Repository) — dados reais de desempenho de estudantes, incluindo casos de reprovação, faltas, tempo de estudo e apoio familiar.

---

## 📊 Resultados

| Métrica | Valor | Por que essa métrica |
|---|---|---|
| Recall | [xx%] | Prioriza detectar alunos em risco real — o custo de um falso negativo (não avisar quem vai reprovar) é maior que o de um falso positivo |
| Acurácia | [xx%] | Métrica geral de referência |
| [Matriz de confusão / outra] | [inserir] | [justificativa] |

**[Inserir gráfico ou imagem da matriz de confusão / comparação entre modelos]**

---

## ⚙️ Como Rodar

```bash
# 1. Clonar o repositório
git clone [link-do-repo]
cd meu-projeto-ia

# 2. Criar ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Rodar a aplicação
streamlit run src/app.py
```

> Testado em máquina limpa em [data]. Se algo não funcionar, abra uma issue ou consulte `notebooks/desenvolvimento.ipynb` para reproduzir o treino do modelo do zero.

---

## 🤖 Uso de IA no Desenvolvimento

Documentação transparente de como e onde usamos LLMs durante a construção do projeto:

- **[Etapa/ferramenta usada, ex: geração de boilerplate do Streamlit]** — [LLM implementou, equipe revisou e ajustou X e Y]
- **[Etapa, ex: debugging]** — [uso pontual para identificar erro em Z]
- **[Etapa, ex: redação do relatório]** — [uso para revisão de texto, conteúdo técnico definido pela equipe]

Toda decisão de modelagem, escolha de métricas e arquitetura da solução foi definida e justificada pela equipe — o LLM foi usado como ferramenta de implementação, não de decisão.

---

## ⚠️ Limitações Conhecidas

- O dataset base (UCI Student Performance) é de estudantes do ensino médio português, não universitários brasileiros — os padrões comportamentais são um ponto de partida, não uma calibração perfeita para o nosso contexto.
- [Outras limitações específicas do modelo/dados]

Mais detalhes sobre ética e limitações em `relatorio/relatorio_tecnico.pdf`, seção 5.

---

## 🎥 Vídeo Demo (Backup)

[Link do vídeo de 2-3 min mostrando a demo funcionando]

---

## 📁 Estrutura do Repositório

```
meu-projeto-ia/
├── README.md
├── notebooks/
│   └── desenvolvimento.ipynb
├── src/
│   └── app.py
├── data/
├── relatorio/
│   └── relatorio_tecnico.pdf
├── slides/
│   └── pitch.pdf
└── requirements.txt
```
