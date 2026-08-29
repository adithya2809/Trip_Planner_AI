from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

print("Calling Gemini...")

trip={
    "destination":"Bangkok",
    "Days":4,
    "Budget":70000,
    "Interests":['temples','streets','water paragliding']   
}

prompt = f"""
You are an AI travel planner.

Plan a {trip["Days"]}-day trip to {trip["destination"]}.

The traveler's budget is ₹{trip["Budget"]}.
Their interests are: {", ".join(trip["Interests"])}.

Organize the itinerary by day, with morning,
afternoon, and evening activities.

Keep the itinerary realistic and concise.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print("\nGemini response:")
print(response.text)