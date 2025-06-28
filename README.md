# 💬 Chat With MySQL Database

A Streamlit web app that allows users to chat with a MySQL database using natural language! This app utilizes LangChain, Groq's LLaMA3, and SQLDatabaseToolkit to dynamically convert user queries into SQL commands and return relevant results.

--- 

## 🚀 Demo

https://github.com/user-attachments/assets/9a972d98-b860-48ac-b7a8-1cd17c4965ba

---

## 🚀 Features

🔗 Connect to any MySQL database with your credentials

🤖 Use natural language to query the database

🚀 Powered by LangChain's SQL agent and Groq's LLaMA3-70B

🧠 Explore the thoughts of the agent, i.e. intermediate steps in generating results 

🗂️ Clear chat history and reconnect seamlessly

🖥️ Intuitive Streamlit UI

---

## 📦 Installation

> git clone https://github.com/Adityajain8595/Chat-with-MySQL-DB.git

> cd Chat-with-MySQL-DB

> pip install -r requirements.txt

> streamlit run chatSQL.py

---

## 🔐 Environment setup:

Create a .streamlit/secrets.toml file and write in it:

GROQ_API_KEY = "your-groq-api-key"

LANGCHAIN_API_KEY = "your-langchain-api-key"

---

### 📸 Example Use Case

User: What are the top 5 customers by total order value?

Agent: Executes SQL like "SELECT customer_id, SUM(order_total) FROM orders GROUP BY customer_id ORDER BY SUM(order_total) DESC LIMIT 5;" to retrieve results. 

---

## 🛠️ Developer Info

Key functions in utilities.py:

1. def get_sql_db(...)         # Builds connection from user credentials
2. def sql_agent(...)          # Sets up LangChain SQL Agent with Groq model

Main logic in 'chatSQL.py':

1. UI for user inputs via Streamlit
2. Connect/disconnect DB
3. Show chat messages and results
4. Handle chat interaction state

---

## 📌 Notes

1. Ensure your MySQL DB is accessible (host/port open).
2. Secure your .env and .streamlit/secrets.toml (do not commit to GitHub).
3. This app uses LLaMA3-70B via Groq, ensure your API quota allows inference.

---

## 🤝 Author

Made by Aditya Jain

Feel free to fork this repo and submit pull requests! Bug reports and feature suggestions are welcome.

Connect with me:

LinkedIn: [LinkedIn URL](https://www.linkedin.com/in/adityajain8595/) 

