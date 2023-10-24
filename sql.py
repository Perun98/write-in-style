from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
import streamlit as st

llm = ChatOpenAI(temperature=0)

db = SQLDatabase.from_uri(
    f"mssql+pyodbc://@DJORDJE-E15\SQLEXPRESS01/sqltest?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes&charset=utf8"
)

toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

st.subheader("Upit u SQL bazu")
st.caption("Ver. 24.10.23")
pitanje = st.text_input("Unesi upit u SQL bazu")
if pitanje:
    odgovor = agent_executor.run(pitanje)
    st.write(odgovor)
