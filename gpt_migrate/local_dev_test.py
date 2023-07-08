### File for testing locally

import os
from dotenv import load_dotenv
from ai import AI
import openai

load_dotenv()

OPENAI_API_TYPE = os.getenv('OPENAI_API_TYPE')
OPENAI_API_VERSION = os.getenv('OPENAI_API_VERSION')
OPENAI_API_BASE = os.getenv('OPENAI_API_BASE')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

print(os.environ["OPENAI_API_TYPE"])

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_base = os.getenv("OPENAI_API_BASE")  # Your Azure OpenAI resource's endpoint value.
openai.api_key = os.getenv("OPENAI_API_KEY")

ai = AI(
    model="gpt-35-turbo",
    temperature=0.1,
)

print(ai.model_name)

print(ai.write_code("hi, how are you"))

message=[{"role": "user", "content": str("hi, how are you")}] 
response = openai.ChatCompletion.create(
    engine=ai.model_name,
    messages = message)

print(response)