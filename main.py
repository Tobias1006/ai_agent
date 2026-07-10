import os
import argparse
from prompts import system_prompt
from dotenv import load_dotenv
from openai import OpenAI
 

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type = str, help = "User prompt")
parser.add_argument("--verbose", action="store_true", help = "Enable verbose output")
args = parser.parse_args()

messages=[
            {"role": "system","content": system_prompt},
            {"role": "user","content": args.user_prompt}
        ]
def main():
    print("Hello from ai-agent!")
    if api_key == None:
        raise RuntimeError("No API-Key was found in .env")
    response = client.chat.completions.create(
        model = "openrouter/free", 
        messages=messages,
        temperature=0)
    
    if response == None:
            raise RuntimeError("Response not available - None Tokens left mayhaps?")
    
    if args.verbose:
        print(f'User prompt: {args.user_prompt}') 
        print(f'Prompt tokens: {response.usage.prompt_tokens}')
        print(f'Response tokens: {response.usage.completion_tokens}')
        print(response.choices[0].message.content)
    else: 
        print(response.choices[0].message.content)
        
if __name__ == "__main__":
    main()
