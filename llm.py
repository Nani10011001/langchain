from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()# loads the .env (where the secret values present in it)

llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=os.environ["GROQ_API_KEY"])
result = llm.invoke("what are the metro paltone city in india") # using the invoke function to pass the query of it
print(result.content)# to print the result of the 
