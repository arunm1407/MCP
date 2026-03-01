from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from core.llm import get_model, get_search_tools
from agents.stock_prompts import (
    STOCK_FINDER_PROMPT,
    MARKET_DATA_PROMPT,
    NEWS_ANALYST_PROMPT,
    PRICE_RECOMMENDER_PROMPT,
    STOCK_SUPERVISOR_PROMPT,
)


def _create_agent(model, tools, prompt, name):
    return create_react_agent(model, tools, prompt=prompt, name=name)


def build_stock_supervisor():
    model = get_model()
    tools = get_search_tools()

    agents = [
        _create_agent(model, tools, STOCK_FINDER_PROMPT, "stock_finder_agent"),
        _create_agent(model, tools, MARKET_DATA_PROMPT, "market_data_agent"),
        _create_agent(model, tools, NEWS_ANALYST_PROMPT, "news_analyst_agent"),
        _create_agent(model, tools, PRICE_RECOMMENDER_PROMPT, "price_recommender_agent"),
    ]

    supervisor = create_supervisor(
        model=get_model(),
        agents=agents,
        prompt=STOCK_SUPERVISOR_PROMPT,
        add_handoff_back_messages=True,
        output_mode="full_history",
    ).compile()

    return supervisor
