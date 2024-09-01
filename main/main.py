# main.py
from openai import OpenAI
import os
from wheatleybrain.wheatley import brain
from WheatleyEyes.eyeImageProcessing import eyeBase
import sys

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
MODEL = "gpt-4o-mini"

initChoice = input("Type 'a' for eyes and 'b' for brain.")
if initChoice == "a":
    eyeBase()
elif initChoice == "b":
    brain()
else:
    print("you did not choose a proper value")
    sys.exit(0)

