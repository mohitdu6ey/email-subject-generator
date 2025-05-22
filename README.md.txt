# Email Subject Line Generator

This project uses a local LLaMA 3.2 model (via Ollama) to generate short, clear, and professional subject lines based on email content.

## How to Use

1. Make sure your local LLaMA 3.2 model is running and the Ollama API is accessible.
2. Set your API key securely (do **not** hardcode in the script).
3. Run the Python script to generate subject line suggestions from email content.

## Example Usage

```python
from openai import OpenAI

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

openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

response = openai.chat.completions.create(
    model="llama3.2",
    messages=messages
)

print(response.choices[0].message.content)
