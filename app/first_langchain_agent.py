from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent

from datetime import datetime

load_dotenv()


@tool
def get_time() -> str:
    """
    Returns the current time.
    """
    return datetime.now().strftime("%H:%M:%S")


@tool
def get_day() -> str:
    """
    Returns the current day.
    """
    return datetime.now().strftime("%A")


@tool
def calculator(expression: str) -> str:
    """
    Evaluate mathematical expressions.
    """
    return str(eval(expression))


llm = ChatOpenAI(
    model="gpt-4.1-mini"
)

tools = [
    get_time,
    get_day,
    calculator
]


agent = create_agent(
    model=llm,
    tools=tools
)

response = agent.invoke(
    {
        "messages": [
            (
                "human",
                "What time is it?"
            )
        ]
    }
)

print(response["messages"][-1].content)