from core.config import *  # noqa: F401,F403 - triggers truststore + dotenv setup
from agents.healthcare import build_healthcare_supervisor
from core.output import pretty_print_messages

# Set to True for interactive input, False for pre-defined demo query
INTERACTIVE = False

SAMPLE_QUERY = (
    "A 45-year-old patient named Rajesh Kumar visits the hospital with complaints of "
    "persistent chest pain and shortness of breath for the past 3 days. He has a family "
    "history of heart disease. He has a health insurance policy with Star Health Insurance, "
    "policy number SH-2024-789456, with coverage up to 5 lakhs INR. "
    "Process his complete hospital journey from appointment to insurance claim."
)


def get_query():
    if INTERACTIVE:
        print("Enter patient details (symptoms, age, insurance info):")
        return input("> ").strip()
    return SAMPLE_QUERY


def run(query: str):
    supervisor = build_healthcare_supervisor()

    for chunk in supervisor.stream(
        {"messages": [{"role": "user", "content": query}]},
    ):
        pretty_print_messages(chunk, last_message=True)


if __name__ == "__main__":
    run(get_query())
