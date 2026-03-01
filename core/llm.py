from langchain.chat_models import init_chat_model
from langchain_community.tools.tavily_search import TavilySearchResults
from core.config import GROQ_API_KEY, LLM_MODEL, TAVILY_MAX_RESULTS


def get_model():
    return init_chat_model(model=LLM_MODEL, api_key=GROQ_API_KEY)


def get_search_tools():
    return [TavilySearchResults(max_results=TAVILY_MAX_RESULTS)]
