# wheatley.py
# basic import to add the api
from openai import OpenAI
import os
from pydub import AudioSegment
from pydub.playback import play
# defining the api key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
MODEL = "gpt-4o-mini"  # using gpt-4o-mini


# creating a "brain" instance to loop so that the query doesn't end as soon as the first prompt has gone thru
def brain() -> object:
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
        # TTS current model (using openai but might switch to another lib for cost)
        response_content = completion.choices[0].message.content
        response = client.audio.speech.create(
            model="tts-1",
            voice="fable",
            input=response_content

        )
        # uploading the response to a mp3 file
        response.stream_to_file("output.mp3")
        print(response_content)  # print to terminal yuh
        # playing sound using ffmpeg and pydub
        sound = AudioSegment.from_mp3('output.mp3')
        play(sound)



if __name__ == "__main__":
    brain()  # run yuh
