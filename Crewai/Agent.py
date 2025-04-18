from crewai import Agent
from wikipedia_tool import wiki_tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import os

## Chamada de modelo da gemini ##
llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                           verbose=True ,
                           temperature=0.5,
                           google_api_key=os.getenv("AIzaSyC9bHJd5FHp1w76EvlsuZrS0lpvV5ACpwk"))

##Criando pesquisador com custon tools ##

novo_pesquisador = Agent(
    role= "Pesquisador do artigo",
    goal="Fornecer informações relevantes sobre {topico} fornecer um resumo com os pontos mais importantes",
    backstory="Você está trabalhando no planejamento de um artigo sobre o tema: {topico}."
              "Você coleta informações que ajudem o público a aprender algo e tomar decisões informadas."
              "Seu trabalho servirá de base para que o Redator de Conteúdo escreva um artigo sobre esse tema.",
    allow_delegation=False,
    llm = llm,
    tools=[wiki_tool],
    verbose=True
)
##Criando escritor com custon tools ##

novo_escritor = Agent(
    role= "Escritor do artigo",
    goal= "Faça um artigo factualmente preciso, com opinião de modo que agregue ao conteúdo do {topico} de no maximo 300 palavras",
    backstory= "Você é trabalha escrevendo um artigo de opinião sobre o tema: {topico}"
               "Você baseia sua escrita no trabalho do Pesquisador do artigo, no qual fornece um resumo para você"
               "Você segue os principais objetivos e a direção do esboço, conforme fornecido pelo Planejador de Conteúdo."
               "Você também oferece insights objetivos e imparciais, sustentando-os com as informações fornecidas pelo Planejador de Conteúdo.",
    allow_delegation=False,
    llm = llm,
    tools=[wiki_tool],
    verbose=True
)
