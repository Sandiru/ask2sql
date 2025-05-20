import os
import re
from dotenv import load_dotenv
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_sql_query_chain
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_core.runnables import RunnableLambda,RunnablePassthrough
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()
os.environ["GOOGLE_API_KEY"]
user=os.environ['USER']
password=os.environ['PASSWORD']
host=os.environ['HOST']
port=os.environ['PORT']
db_name=os.environ['DB_NAME']
model=os.environ['MODEL']

db=SQLDatabase.from_uri(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db_name}")

llm = ChatGoogleGenerativeAI(model=model, temperature=0.0)

query_generate=create_sql_query_chain(llm,db)

query_execute=QuerySQLDatabaseTool(db=db)


def extract_sql(query):
    pattern = r"```sql\s*(.*?)\s*```"
    matches = re.findall(pattern, query,re.DOTALL)
    query = matches[0].strip() if matches else query
    return query

extract_sql_runnable = RunnableLambda(extract_sql)


answer_prompt=PromptTemplate.from_template("""Given a user question, the generated SQL query, and its result, write a clear and natural answer to the question.
                                          
                                          User Question: {question}
                                          SQL Query:{query}
                                          SQL Result:{result}
                                          
                                          Final Answer:""")

final_answer=answer_prompt|llm|StrOutputParser()

chain=(RunnablePassthrough.assign(query=query_generate).assign(result=itemgetter("query")|extract_sql_runnable|query_execute)|final_answer)

def run_quary():
    print("\n📘 Welcome to ASK2SQL!")
    print("Type a natural language question to generate and execute a SQL query.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        question = input("❓ Question: ")
        if question.lower() == "exit":
            print("👋 Exiting ASK2SQL. Goodbye!")
            break

        print("🧠 Thinking...\n")
        try:
            result = chain.invoke({"question": question})
            print("✅ Result:")
            print("----------------------------")
            print(result)
            print("----------------------------\n")
        except Exception as e:
            print("❌ Error:", e)
            print("Please try again.\n")

run_quary()