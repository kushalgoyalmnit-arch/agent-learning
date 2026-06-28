from openai import OpenAI
from dotenv import load_dotenv

from tools import calculator, get_time

load_dotenv()

client = OpenAI()


def run_agent(question):

    # Agent reasoning
    if any(x in question for x in ["+", "-", "*", "/"]):

        expression = question.replace(
            "What is",
            ""
        ).strip()

        result = calculator(expression)

        prompt = f"""
        User asked:

        {question}

        Calculator result:
        {result}

        Explain the answer.
        """
    elif "time" in question.lower():
        current_time = get_time()

        prompt = f"""
        User asked:
        {question}

        Current time:
        {current_time}

        Answer the user.
        """

    else:

        prompt = question

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":

    question = input("Question: ")

    answer = run_agent(question)

    print()
    print(answer)