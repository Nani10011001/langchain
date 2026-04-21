from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_core.messages import SystemMessage,HumanMessage

load_dotenv()
groq_api_key = os.environ["GROQ_API_KEY"]

#initilaze the llm model
llm = ChatGroq(model = "llama-3.1-8b-instant",api_key=groq_api_key)
promt_message = SystemMessage(content="""
Explore three different potential solutions for the user's problem. 
    For each, provide a 'Pros' and 'Cons' list. 
    Finally, determine which branch is the most logical
""")
prompt = ChatPromptTemplate.from_messages([
    (promt_message),(HumanMessage(content="what is best course a person can get in the trending market of it"))
])
#chaing runnable chainign the flow of the architeture 
chain = prompt | llm | StrOutputParser()
result = chain.invoke({})
print(result)