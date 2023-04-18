import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def search(query):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Search for a phrase in the PDFs:\n" + query + "\n\n",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
