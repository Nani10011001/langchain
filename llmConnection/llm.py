from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import os

groq_api_key = os.environ["GROQ_API_KEY"]

llm = ChatGroq(model="llama-3.1-8b-instant",api_key=groq_api_key)

result = llm.invoke(
    "i have the craving to eat biriyani"
)
print(result.content)