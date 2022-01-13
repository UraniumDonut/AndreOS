import openai
import json

stop = "\n"
with open("keys.json", "r") as f:
    keys = json.load(f)
openai.api_key = keys["openai"]
prompt = """Q:Lieblings Steam Spiel?
A:"""

response = openai.Completion.create(engine="davinci", prompt=prompt, stop=stop, temperature=0.6)

print(response)