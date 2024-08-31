from openai import OpenAI
import os


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
PROMPT = input("Welcome to Aperature Science, I am wheatley. What is your query?\n")
MODEL = "gpt-4o-mini"

completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful and comedic assistant based on the character Wheatley from the game Portal 2"},
        {
            "role": "user",
            "content": PROMPT
        }
    ]
)

print(completion.choices[0].message.content)