from langchain_community.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq

def get_sql_db(user, password, host, port, database):
    uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(uri)

def sql_agent(sql_db, groq_api_key):
    llm = ChatGroq(model="llama3-70b-8192", groq_api_key=groq_api_key)
    toolkit = SQLDatabaseToolkit(db=sql_db,llm=llm)

    sql_agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
    )
    
    return sql_agent