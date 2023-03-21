import openai

openai.api_key = "OPENAI_API_KEY"

while True:
    prompt= input("\nRealiza una pregunta: ")
    prompt = prompt.lower()
    
    if prompt == "exit" or prompt == "exit()":
        break
    
    chat = openai.Completion.create(engine="text-davinci-003",
                                    prompt=prompt,
                                    max_tokens=2048)
    print(chat)
    print(chat.choices[0].text)