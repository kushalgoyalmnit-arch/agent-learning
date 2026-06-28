from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini"
)

response = llm.invoke(
    "Explain what an API is."
)

print(response.content)