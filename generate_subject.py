import os
from dotenv import load_dotenv
from openai import OpenAI

def generate_email_subject():
    load_dotenv()  # Load environment variables from .env file

    api_key = os.getenv("OLLAMA_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set OLLAMA_API_KEY in your .env file.")

    system_prompt = "You are an assistant that reads the content of an email and suggests one short, clear, and professional subject line for it."

    user_prompt = '''
    Hi John,

    I hope you're doing well. I just wanted to follow up on our recent conversation regarding the project updates. I’ve reviewed the points we discussed and wanted to confirm a few next steps moving forward.

    Please let me know if you need any additional information from my side or if there’s anything specific you’d like me to prioritize. I'm happy to assist in any way that helps keep things on track.

    Looking forward to your feedback and continuing our collaboration.

    Best regards,
    Emily
    '''

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    openai = OpenAI(base_url='http://localhost:11434/v1', api_key=api_key)

    response = openai.chat.completions.create(
        model="llama3.2",
        messages=messages
    )

    print("Suggested Subject Line:")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    generate_email_subject()
