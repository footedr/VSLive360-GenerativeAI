from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature": 0.9, "max_length": 64})

prompt = "What is a good name for a workshop on Generative AI at a technical conference in Columbus, OH?"

print(llm.invoke(prompt))