from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

print("Calling Gemini...")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Say hello in one sentence."
)

print("Gemini response:")
print(response.text)