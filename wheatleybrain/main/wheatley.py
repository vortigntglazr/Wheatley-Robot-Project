# basic import to add the api
from openai import OpenAI
import os

# defining the api key  
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
MODEL = "gpt-4o-mini"  # using gpt-4o-mini


# creating a "brain" instance to loop so that the query doesn't end as soon as the first prompt has gone thru
def brain():
    print("Welcome to Aperture Science, I am Wheatley. What is your query?")
    while True:  # loop de loop
        PROMPT = input("> ")  # prompt
        if PROMPT == "sudo exit":  # ubuntu reference :skull:
            print("Goodbye!")
            quit()

        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system",
                 "content": "You are a helpful and comedic assistant based on the character Wheatley from the game Portal 2"},
                # gaben no sue pls MIT license go hard
                {
                    "role": "user",
                    "content": PROMPT
                }
            ],
            max_tokens=300
        )
        response_content = completion.choices[0].message.content
        print(response_content)  # print to terminal yuh


if __name__ == "__main__":
    brain()  # run yuh
