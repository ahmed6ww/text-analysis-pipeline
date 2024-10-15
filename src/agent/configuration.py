import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

# Configure the LLM (OpenAI ChatGPT)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
