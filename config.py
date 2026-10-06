
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

groq_api=os.getenv("GROQ_API_KEY")


if not groq_api:
    raise ValueError("GROQ_API_KEY is not set in .env")
llm=ChatGroq(
    groq_api_key=groq_api,
    model_name="qwen/qwen3.8-27b",
    temperature=0
)