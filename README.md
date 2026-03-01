# Multi-Agent AI Workflows

Real-world multi-agent systems built with **LangGraph**, **LangChain**, and **Groq**. Each demo uses a supervisor pattern to orchestrate specialized agents that work together to complete complex workflows.

## Demos

### 1. Healthcare — Hospital to Insurance Claim

Simulates a complete patient journey through a hospital system.

```
Patient Arrives → Reception → Diagnosis → Billing → Customer Service → Insurance Claim
```

| Agent | Role |
|-------|------|
| Hospital Reception | Patient registration, department & doctor assignment |
| Diagnosis & Treatment | Clinical diagnosis, tests, treatment plan |
| Billing | Itemized hospital bill generation (INR) |
| Customer Service | Bill review, insurance claim preparation |
| Insurance | Claim processing, approval/denial decision |

```bash
python run_healthcare.py
```

### 2. Stock Market — NSE Stock Recommendations

Analyzes Indian stock market (NSE) and provides buy/sell recommendations.

```
Research Stocks → Fetch Market Data → Analyze News → Recommend Buy/Sell
```

| Agent | Role |
|-------|------|
| Stock Finder | Identifies 2 promising NSE-listed stocks |
| Market Data | Fetches price, volume, trends, technical indicators |
| News Analyst | Summarizes recent news and sentiment |
| Price Recommender | Buy/Sell/Hold decision with target price |

```bash
python run_stock.py
```

## Project Structure

```
├── run_healthcare.py          # Entry point — healthcare demo
├── run_stock.py               # Entry point — stock market demo
├── agents/
│   ├── __init__.py
│   ├── healthcare.py          # Healthcare agent supervisor setup
│   ├── prompts.py             # Healthcare agent prompts
│   ├── stock.py               # Stock market agent supervisor setup
│   └── stock_prompts.py       # Stock market agent prompts
├── core/
│   ├── __init__.py
│   ├── config.py              # Environment config (API keys, model)
│   ├── llm.py                 # LLM and tools factory
│   └── output.py              # Output formatting utilities
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-name>
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Get API keys (both are free)

| Service | Free Tier | Get Key |
|---------|-----------|---------|
| **Groq** | 100k tokens/day | [console.groq.com](https://console.groq.com) |
| **Tavily** | 1000 searches/month | [tavily.com](https://tavily.com) |

### 4. Configure environment

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```
GROQ_API_KEY=gsk_your_key_here
TAVILY_API_KEY=tvly-your_key_here
```

### 5. Run a demo

```bash
python run_healthcare.py    # Healthcare workflow
python run_stock.py         # Stock market analysis
```

## Interactive vs Static Mode

Each demo has an `INTERACTIVE` flag at the top of the run file:

```python
# Set to True for interactive input, False for pre-defined demo query
INTERACTIVE = False
```

| Mode | Flag | Behavior |
|------|------|----------|
| **Static** | `INTERACTIVE = False` | Runs automatically with a pre-defined sample query |
| **Interactive** | `INTERACTIVE = True` | Prompts you to type your own query at runtime |

To switch modes, edit the flag in `run_healthcare.py` or `run_stock.py`.

## Customization

- **Change LLM model** — Edit `LLM_MODEL` in `core/config.py`
- **Modify agent behavior** — Edit prompts in `agents/prompts.py` or `agents/stock_prompts.py`
- **Add a new workflow** — Create `agents/your_workflow.py` + `agents/your_prompts.py` + `run_your_workflow.py`
- **Change demo query** — Modify `SAMPLE_QUERY` in the respective `run_*.py` file

## Tech Stack

- **LangGraph** — Multi-agent orchestration with supervisor pattern
- **LangChain** — Agent framework and tool integration
- **Groq** — Fast, free-tier LLM inference (Llama 3.3 70B)
- **Tavily** — Web search tool for real-time data

## SSL Note (Corporate VPN/Proxy)

If you're behind a corporate proxy (e.g., Zscaler), the project uses `truststore` to automatically use your system's certificate store. No additional SSL configuration needed.
