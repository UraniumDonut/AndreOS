import openai
import json

stop = "\n"
with open("keys.json", "r") as f:
    keys = json.load(f)
openai.api_key = keys["openai"]
prompt = """Q:We are having chicken for dinner. Should we have corn or buckwheat as a side?
A:"""

response = openai.Completion.create(engine="davinci", prompt=prompt, stop=stop, temperature=0.6)

print(response)