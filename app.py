import os
import google.generativeai as genai 
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

user_input = input("How can I Assist you? ")
response = model.generate_content(user_input)
print(response.text)
input("Press enter to exit...")