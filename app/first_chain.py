from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini"
)

prompt = PromptTemplate.from_template(
    """
    Explain {topic}
    like I'm five years old.
    """
)

chain = prompt | llm

response = chain.invoke(
    {
        "topic": "API"
    }
)

print(response.content)