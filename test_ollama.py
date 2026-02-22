import ollama

response = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': 'Talk to me like a friend.'}]
)

print(response['message']['content'])