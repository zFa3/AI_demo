#!/usr/bin/env python3

# imports
import asyncio
# pip install google-genai
from google import genai

# pip install rich
from rich.console import Console
from rich.markdown import Markdown

# create an array to hold message history
history = 6
memory = []

# generate a response from google api
async def generate(prompt):

    client = genai.Client(api_key="")

    response = await client.aio.models.generate_content(
        model="gemma-3-27b-it",
        contents=prompt,
    )
    
    return response.text

# format the text
def pretty_print(text):

    console = Console()
    markdown = Markdown(text + "\n")

    console.print(markdown)

# run the program
if __name__ == "__main__":
    
    while prompt := input(">>> "):
        try:
            memory.append(prompt)
            memory = memory[-history:]
            
            response = asyncio.run(
                generate(
                    f"<CURRENT CONVERSATION>:\n{"\n".join(memory)}\n<LATEST USER MESSAGE>:\n{prompt}"
                )
            )
            
            memory.append(response)
            pretty_print(response)

        except Exception as error:
            print(f"An error occured: {error}")