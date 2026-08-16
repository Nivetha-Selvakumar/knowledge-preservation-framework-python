# import json
# import os

# from dotenv import load_dotenv
# from google import genai


# class KnowledgeAnalyzer:

#     def __init__(self):

#         api_key = os.getenv("GEMINI_API_KEY")

#         if not api_key:
#             raise Exception("GEMINI_API_KEY not found in .env")

#         self.client = genai.Client(api_key=api_key)

#         self.model = "gemini-2.5-flash"

#     def analyze(self, prompt):

#         response = self.client.models.generate_content(
#             model=self.model, contents=prompt
#         )

#         if response is None:
#             raise Exception("No response received from Gemini")

#         text = response.text.strip()

#         # Remove markdown fences if Gemini returns them
#         if text.startswith("```json"):
#             text = text.replace("```json", "", 1)

#         if text.endswith("```"):
#             text = text[:-3]

#         text = text.strip()

#         return text


# class KnowledgeAnalyzer:

#     def __init__(self):

#         api_key = os.getenv("GEMINI_API_KEY")

#         self.client = genai.Client(api_key=api_key)

#         self.model = "gemini-3.5-flash"

#     def analyze(self, prompt):

#         print(f"Using model: {self.model}")

#         response = self.client.models.generate_content(
#             model=self.model, contents=prompt
#         )

#         return response.text

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class KnowledgeAnalyzer:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise Exception("GROQ_API_KEY not found")

        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def analyze(self, prompt):

        response = self.client.chat.completions.create(
            model=self.model, messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content


print(__file__)
