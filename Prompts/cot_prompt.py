from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_core.prompts import PromptTemplate

groq_api_key = os.environ["GROQ_API_KEY"]


prompt = PromptTemplate(template="""You are a logical assistant. Always think step-by-step before giving a final answer. \n userQuery:{query}""",
input_variables=["query"])

llm = ChatGroq(model="llama-3.1-8b-instant",api_key=groq_api_key)
chain = prompt | llm
result = chain.invoke({
    "query":"i have the craving to eat bir"
})
print(result.content)