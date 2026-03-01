from core.config import *  # noqa: F401,F403 - triggers truststore + dotenv setup
from agents.stock import build_stock_supervisor
from core.output import pretty_print_messages

# Set to True for interactive input, False for pre-defined demo query
INTERACTIVE = False

SAMPLE_QUERY = "Give me good stock recommendation from NSE"


def get_query():
    if INTERACTIVE:
        print("Enter your stock market query:")
        return input("> ").strip()
    return SAMPLE_QUERY


def run(query: str):
    supervisor = build_stock_supervisor()

    for chunk in supervisor.stream(
        {"messages": [{"role": "user", "content": query}]},
    ):
        pretty_print_messages(chunk, last_message=True)


if __name__ == "__main__":
    run(get_query())
