#!/usr/bin/env python3

from gpt4all import GPT4All

llm_path = "/Users/georgian/Library/Application Support/nomic.ai/GPT4All/Meta-Llama-3-8B-Instruct.Q4_0.gguf"
llm = GPT4All(llm_path)


with llm.chat_session():
    try:
        print("Press Ctrl+C to exit this program.")
        while True:
            question = input("Enter your question: ")
            print("Generating response...")

            prompt = f"Question: {question}\nAnswer:"
            response = llm.generate(prompt, max_tokens=2048)
            print(response)
    except KeyboardInterrupt:
        print("\nGood bye!")
