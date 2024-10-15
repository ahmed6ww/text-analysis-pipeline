import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
os.environ["GEMENI_API_KEY"] = os.getenv('GEMENI_API_KEY')

# Configure the LLM (OpenAI ChatGPT)
llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
         api_key=os.getenv('GEMENI_API_KEY')
    )