### File for testing locally

import os
from dotenv import load_dotenv
from ai import AI

load_dotenv()

OPENAI_API_TYPE = os.getenv('OPENAI_API_TYPE')
OPENAI_API_VERSION = os.getenv('OPENAI_API_VERSION')
OPENAI_API_BASE = os.getenv('OPENAI_API_BASE')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

print(os.environ["OPENAI_API_TYPE"])

ai = AI(
    model="gpt-35-turbo",
    temperature=0.1,
)

print(ai.model_name)