"""Run this model in Python

> pip install openai
"""
import os
from openai import OpenAI

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings. 
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key="",
)


response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "你对比chatgpt4有什么优势？",
        }
    ],
    model="o1-mini"
)

print(response.choices[0].message.content)
