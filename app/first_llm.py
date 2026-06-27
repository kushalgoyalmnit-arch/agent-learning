from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

question = input("Ask something: ")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=question
)

print("\nResponse:\n")
print(response.output_text)