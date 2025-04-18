from crewai import Crew
from tasks import novo_plan, nova_escrita
from Agent import novo_escritor, novo_pesquisador

## Formando processo ##

crew = Crew(
    agents=[novo_pesquisador,novo_escritor,],
    tasks=[novo_plan, nova_escrita],
    verbose=True
)

## start do processo

result = crew.kickoff(inputs={"topico do artigo:":"Enzo Ferrari"})
print(result)
