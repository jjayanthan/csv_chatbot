import sys
import os
import pandas as pd
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent

import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY

df = pd.read_csv("./docs/ml_project1_data.csv")

df2 = pd.read_csv("./docs/dictionary.csv")

agent = create_pandas_dataframe_agent(OpenAI(temperature=0), [df,df2], verbose=True)

yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;39m"

persist = True

chat_history = []
print(f"{yellow}---------------------------------------------------------------------------------")
print('Welcome to the CSV Chatbot. You are now ready to start interacting with your CSV file/s')
print('---------------------------------------------------------------------------------')
while persist:
    query = input(f"{green}Query: ")
    if query == "exit" or query == "quit" or query == "q" or query == "f":
        print('Exiting')
        sys.exit()
    else:
        result = agent.run(query)
        chat_history.append((query, result))
 
    

