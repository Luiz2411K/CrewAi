crew é o a main do sistema, no qual é onde se start o código, e se coloca o assunto no qual se está disposto por procura, a aba de agentes, temos os agentes pesquisador e escritor 
que são respectivamente reponsaveis por pesquisar na API da wikipedia utilizando a LLM da Gemini 2.0 flask criando um resumo e pela escrita de no maximo 300 palavras pelo estritor
buscando as palavras chaves feitas pelo pesquisador, a aba de tasks, são as tarefas atribuídas para os agentes, o novo_plan dá detalhes de como o pesquisador deve fazer sua atividade e
a nova_escrita descreve a ativivdade do escritor, a wikipedia_tool, é uma tool personalizada feita para ser consultada pelos agentes.
