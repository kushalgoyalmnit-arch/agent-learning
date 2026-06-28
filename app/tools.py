from langchain.tools import tool
from datetime import datetime


@tool
def get_time() -> str:
    """
    Returns current time.
    """
    return datetime.now().strftime("%H:%M:%S")


@tool
def calculator(expression: str) -> str:
    """
    Evaluate mathematical expressions.
    """
    return str(eval(expression))

@tool
def get_day() -> str:
    """
    Returns current day.
    """
    return datetime.now().strftime("%A")