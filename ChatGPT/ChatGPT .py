
import openai

openai.api_key = "OPENAPI KEY"

def chat(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
    {"role": "user", "content": prompt}]
        
    )
    reply = completion.choices[0]
    print(reply["message"]["content"])
    return reply

print("Hello! I am your chatbot. You can ask me any question!")
print("Type 'exit' to end the conversation.")

while True:
    prompt = input("You: ")
    if prompt.lower() == 'exit':
        break
    chat(prompt)
