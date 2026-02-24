#!/usr/bin/env python3

# imports
import asyncio
from google import genai

from rich.console import Console
from rich.markdown import Markdown

# create an array to hold message history
history = 6
memory = []

async def generate(prompt):

    client = genai.Client(api_key=)

    response = await client.aio.models.generate_content(
        model="gemma-3-27b-it",
        contents=prompt,
    )
    
    return response.text

def pretty_print(text):

    console = Console()
    markdown = Markdown(text + "\n")

    console.print(markdown)

if __name__ == "__main__":
    
    while prompt := input(">>> "):
        
        memory.append(prompt)
        memory = memory[-history:]
        
        response = asyncio.run(generate(f"<SYSTEM MESSAGE>\nKeep responses brief, use markdown formatting\n<CURRENT CONVERSATION>:\n{"\n".join(memory)}\n<LATEST USER MESSAGE>:\n{prompt}"))
        
        memory.append(response)

        pretty_print(response)
