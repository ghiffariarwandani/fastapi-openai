import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv(key="OPENROUTER_API_KEY"),base_url="https://openrouter.ai/api/v1")

res = client.chat.completions.create(
    model="z-ai/glm-4.5-air:free",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

result = res.choices[0].message.content
print(result)
