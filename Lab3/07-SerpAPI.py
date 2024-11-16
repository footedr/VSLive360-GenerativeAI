from langchain_openai import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain.chains import LLMMathChain
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.agent_toolkits.load_tools import load_tools
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0.9, model="gpt-4o") 
prompt = "Where was the latest Summer Olympics that just took place? and what is the population of that country ?"
llm_math_chain = LLMMathChain.from_llm(llm, verbose=True)   
search = SerpAPIWrapper()
wikipedia = WikipediaAPIWrapper()
tools= load_tools(["serpapi", "wikipedia"])

model = ChatOpenAI(temperature=0)
planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)

agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

agent.invoke(prompt)
