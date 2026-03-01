from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from core.llm import get_model, get_search_tools
from agents.prompts import (
    HOSPITAL_RECEPTION_PROMPT,
    DIAGNOSIS_TREATMENT_PROMPT,
    BILLING_PROMPT,
    CUSTOMER_SERVICE_PROMPT,
    INSURANCE_PROMPT,
    SUPERVISOR_PROMPT,
)


def _create_agent(model, tools, prompt, name):
    return create_react_agent(model, tools, prompt=prompt, name=name)


def build_healthcare_supervisor():
    model = get_model()
    tools = get_search_tools()

    agents = [
        _create_agent(model, tools, HOSPITAL_RECEPTION_PROMPT, "hospital_reception_agent"),
        _create_agent(model, tools, DIAGNOSIS_TREATMENT_PROMPT, "diagnosis_treatment_agent"),
        _create_agent(model, tools, BILLING_PROMPT, "billing_agent"),
        _create_agent(model, tools, CUSTOMER_SERVICE_PROMPT, "customer_service_agent"),
        _create_agent(model, tools, INSURANCE_PROMPT, "insurance_agent"),
    ]

    supervisor = create_supervisor(
        model=get_model(),
        agents=agents,
        prompt=SUPERVISOR_PROMPT,
        add_handoff_back_messages=True,
        output_mode="full_history",
    ).compile()

    return supervisor
