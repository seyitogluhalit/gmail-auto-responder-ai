from openai import OpenAI 

client = OpenAI(API) 

def generate_reply(email_text: str) -> str:
    lowered = email_text.lower()

    if "meeting" in lowered or "schedule" in lowered:
        prompt = f"""
You received a meeting request:
\"\"\"{email_text}\"\"\"
Reply by confirming the meeting time and offering alternatives if needed.
"""
    elif "complaint" in lowered or "not working" in lowered or "issue" in lowered:
        prompt = f"""
A customer complaint was received:
\"\"\"{email_text}\"\"\"
Reply with an apology and suggest a resolution.
"""
    else:
        prompt = f"""
Write a professional reply to the following email:
\"\"\"{email_text}\"\"\"
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
