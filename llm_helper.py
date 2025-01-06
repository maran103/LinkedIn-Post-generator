
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()
llm = ChatGroq(groq_api_key = os.getenv("GROQ_API_KEY"),model="llama-3.2-90b-vision-preview")

if __name__=="__main__":
    response = llm.invoke("who is the gratest football player of all time")
    print(response)