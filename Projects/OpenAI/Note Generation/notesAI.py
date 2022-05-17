import os
import openai

openai.api_key = "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"

response = lambda prompt : openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  temperature=0.3,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

def main ():
    prompt = "What are 5 key points I should know when studying Shostakovich?"
    print(prompt)
    print("="*len(prompt))
    print(response(prompt)['choices'][0]['text'])

if __name__ == "__main__":
    main()