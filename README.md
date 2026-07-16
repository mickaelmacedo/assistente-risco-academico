# 📚 — Assistente Acadêmico

> Organiza sua semana e avisa, com base em dados reais, quando seu padrão de estudo está te levando à reprovação.

---

## 👥 Equipe

| Nome completo |  
| Mickael Lopes de Souza Macedo |  
| [Nome 2] |  
| [Nome 3] |  
| [Nome 4] |  

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

** https://youtu.be/Lrvl19ucZik **

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

### Pré-requisitos

- **Python 3.11 ou superior** ([baixar aqui](https://www.python.org/downloads/))
- **Git** (para clonar o repositório)
- Conexão com a internet (para baixar as dependências e o dataset)

### 1. Clonar o repositório

```bash
git clone https://github.com/mickaelmacedo/assistente-risco-academico.git
cd assistente-risco-academico
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

Ativar:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Baixar os dados

Baixe os dois arquivos abaixo e salve dentro da pasta `data/`:

- [student-mat.csv](https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv)
- [student-por.csv](https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-por.csv)

Fonte original: [Student Performance Dataset — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/320/student+performance)

### 5. Rodar o notebook (treina o modelo)

```bash
jupyter notebook notebooks/desenvolvimento.ipynb
```

Rode todas as células em ordem (**Executar Tudo** / *Run All*). Isso gera o arquivo `src/model/modelo_risco_academico.pkl`, necessário para o app funcionar.

> Alternativa: se estiver usando o VS Code, abra o arquivo `.ipynb` direto por lá — ele tem suporte nativo a notebooks (extensões **Python** e **Jupyter**).

### 6. Rodar o app de demonstração

Com o modelo já treinado (passo anterior), rode:

```bash
streamlit run src/app.py
```

O navegador deve abrir automaticamente em `http://localhost:8501`. Se não abrir, copie e cole esse endereço manualmente.

### Problemas comuns

| Erro | Causa provável | Solução |
|---|---|---|
| `ModuleNotFoundError` | Ambiente virtual não ativado, ou dependência faltando | Confirme que o `venv` está ativo (aparece `(venv)` no terminal) e rode `pip install -r requirements.txt` de novo |
| `FileNotFoundError` nos dados | CSVs não estão em `data/` | Revise o passo 4 |
| App carrega mas mostra erro de modelo | Notebook não foi executado até o fim | Rode o passo 5 completo antes do passo 6 |


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
(https://youtu.be/Lrvl19ucZik)

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
