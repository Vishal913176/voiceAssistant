import os

from openai import OpenAI
import openai

# Set your OpenAI API key
api_key = 'sk-...OfMw'

# Initialize OpenAI client with API key
#openai.api_key = api_key

client = OpenAI( api_key = os.environ.get("OPENAI_API_KEY"))

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write a gmail to friend for wishing happy anniversary",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)