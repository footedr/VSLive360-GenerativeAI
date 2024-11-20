from langchain_openai import ChatOpenAI
from langchain_community.utilities.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from dotenv import load_dotenv

load_dotenv()

# Choose any MS SQL Server Database or SQL Server Database you have access to.

# myuri = "mssql+pyodbc://@.\SQLEXPRESS/IanResearchDB?driver=SQL+Server+Native+Client+11.0"
# myuri = "mssql+pyodbc://@.\SQLEXPRESS/IanResearchDB?driver=ODBC+Driver+17+for+SQL+Server"
myuri = "mssql+pyodbc://threepladmin:4acb7531-9210-4f5e-b398-a9564b3c4080@threepl.database.windows.net/threepl-prod?driver=ODBC+Driver+17+for+SQL+Server"

db = SQLDatabase.from_uri(myuri)

llm = ChatOpenAI(temperature=0, model="gpt-4o")
#llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)

sql_toolkit.get_tools()

# sqldb_agent = create_sql_agent(llm=llm, toolkit=sql_toolkit, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
sqldb_agent = create_sql_agent(llm=llm, toolkit=sql_toolkit, agent_type=AgentType.OPENAI_FUNCTIONS, verbose=True)

#print(sqldb_agent.invoke("How many tables do we have in the database?"))
#print(sqldb_agent.invoke("How many users do we have in the sf_users table?"))
#print(sqldb_agent.invoke("How many libraries are in the sf_libraries table and what are their titles?"))

#print(sqldb_agent.invoke("How many orders were created last week with a mode of LTL?"));
print(sqldb_agent.invoke("Could you please provide me with a list of orders entered last week by each broker for each order mode?"));
#print(sqldb_agent.invoke("Could you please tell me the percentage of orders that have PO numbers attached to them?"));