from dotenv import load_dotenv
load_dotenv()
import os
import requests

def wikipedia_search(query: str) -> str:
    url = "https://pt.wikipedia.org/w/api.php"  # versão em português

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": query,
        "redirects": 1,
    }

    response = requests.get(url, params=params)
    data = response.json()

    pages = data["query"]["pages"]
    for page_id in pages:
        page = pages[page_id]
        if "extract" in page:
            return page["extract"]

    return "Não foi encontrado nenhum artigo correspondente na Wikipedia."

from langchain.tools import Tool

wiki_tool = Tool(
    name="Wikipedia Search",
    func=wikipedia_search,
    description="Use esta ferramenta para buscar informações enciclopédicas na Wikipedia em português."
)

