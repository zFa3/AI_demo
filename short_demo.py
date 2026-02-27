#!/usr/bin/env python3

# imports
import asyncio

# pip install google-genai
from google import genai

# run the program
if __name__ == "__main__":

    client = genai.Client(api_key="")
    
    while prompt := input(">>> "):
        
        response = asyncio.run(
            client.aio.models.generate_content(
                model="gemma-3-27b-it",
                contents=prompt,
            )
        )
        
        print(response.text)