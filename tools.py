from tavily import TavilyClient

from dotenv import load_dotenv
from langchain.tools import tool
from typing import Dict,Any
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


load_dotenv()
tavily=TavilyClient()
@tool 
def web_search(query: str) -> Dict[str, Any]:
    """ To search the web for information"""

    return tavily.search(query)
