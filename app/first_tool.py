from langchain.tools import tool


@tool
def get_time() -> str:
    """
    Returns current time.
    """

    from datetime import datetime

    return datetime.now().strftime("%H:%M:%S")


print(get_time.invoke({}))