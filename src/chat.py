from langchain_core.prompts import PromptTemplate

question_user = input("Pergunte alguma coisa: ")
while not question_user.strip():
    print("A pergunta não pode ser vazia. Por favor.")
    question_user = input("Pergunte alguma coisa: ")


t="""
CONTEXTO:
{context}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{question_user}

RESPONDA A "PERGUNTA DO USUÁRIO
"""

template = PromptTemplate(
    input_variables=["context", "question_user"],
    template=t
)

text = template.format(
    context=f"{'='*70}\nO chunk recuperado na busca por similaridade na base vetorial vai aqui\n{'='*70}", 
    question_user=question_user)
print(text)
