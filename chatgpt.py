import openai

openai.api_key = "TU_API_KEY creada en https://platform.openai.com"

while True:

    prompt = input("\nIntroduce una pregunta: ")

    if prompt == "exit":
    	break

    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens=2048)
    
    print(completion.choices[0].text)

