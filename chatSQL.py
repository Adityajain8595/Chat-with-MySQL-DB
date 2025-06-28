import streamlit as st
from utilities import get_sql_db, sql_agent
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
groq_api_key = st.secrets["GROQ_API_KEY"]

st.title("Chat with MySQL DB using LangChain")
st.write("Interact with your database through the chatbot! It is capable of answering any query/question asked in natural language based on data in the database")

with st.sidebar:
    st.header("Enter your MySQL DB credentials")
    host = st.text_input("Enter host", value="localhost")
    port = st.text_input("Enter port", value="3306")
    user = st.text_input("Enter user", value="root")
    password = st.text_input("Enter password", type="password")
    database = st.text_input("Enter database name")
    st.sidebar.write("Click 'Connect' button to ensure that the database is connected after entering credentials or clearing the message history")

if host and port and user and password and database:
    connect_button = st.sidebar.button("Connect")

    if connect_button:
        try:
            sql_db = get_sql_db(user, password, host, port, database)
            agent_executor = sql_agent(sql_db, groq_api_key)
            st.success("✅ Connected to the database!")
            st.session_state['agent'] = agent_executor
        except Exception as e:
            st.error(f"❌ Connection failed: {e}")

if "messages" not in st.session_state or st.sidebar.button("Clear Message History"):
    st.session_state["messages"] = [{"role":"assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask anything from the database")

if user_query and 'agent' in st.session_state:
    with st.spinner("Generating response..."):
        st.session_state.messages.append({"role":"user", "content":user_query})
        st.chat_message("user").write(user_query)

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container())
            result = st.session_state["agent"].run(user_query, callbacks=[st_cb])
            st.session_state.messages.append({"role":"assistant", "content":result})
            st.success("✅ Query executed!")
            st.write("Result:\n")
            st.write(result)
elif user_query:
    st.error("❌ Please connect to the database first.")
        










