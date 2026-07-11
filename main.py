import os
import json
import argparse
from prompts import system_prompt
from call_function import available_functions
from call_function import call_function
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
        tools=available_functions,
        temperature=0)
    message = response.choices[0].message

    if response == None:
        raise RuntimeError("Response not available - None Tokens left mayhaps?")
    
    if message.tool_calls:
        for call in message.tool_calls:
            result_message = call_function(call)
            if result_message['content'] == '':
                raise Exception('Error: No content received from the tool call')
            if args.verbose:
                print(f"-> {result_message['content']}")
            else:
                print(f"{result_message['content']}")
    
if __name__ == "__main__":
    main()


