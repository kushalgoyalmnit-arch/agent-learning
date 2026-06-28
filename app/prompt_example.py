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
    in simple terms.
    """
)

formatted_prompt = prompt.invoke(
    {
        "topic": "LangChain"
    }
)

response = llm.invoke(formatted_prompt)

print(response.content)