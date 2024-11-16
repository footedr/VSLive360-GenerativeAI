from langchain_openai import ChatOpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents import AgentType, create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
import pyodbc
from dotenv import load_dotenv

load_dotenv()

# Choose any MS SQL Server Database or SQL Server Database you have access to.

# myuri = "mssql+pyodbc://@.\SQLEXPRESS/IanResearchDB?driver=SQL+Server+Native+Client+11.0"
myuri = "mssql+pyodbc://@.\SQLEXPRESS/IanResearchDB?driver=ODBC+Driver+17+for+SQL+Server"

db = SQLDatabase.from_uri(myuri)

llm = ChatOpenAI(temperature=0, model="gpt-4o")

sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)

sql_toolkit.get_tools()

sqldb_agent = create_sql_agent(llm=llm, toolkit=sql_toolkit, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

#print(sqldb_agent.invoke("How many tables do we have in the database?"))
#print(sqldb_agent.invoke("How many users do we have in the sf_users table?"))
print(sqldb_agent.invoke("How many libraries are in the sf_libraries table and what are their titles?"))