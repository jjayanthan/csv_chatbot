# csv_chatbot

This is a Python based chatbot project, which allows the user to interact with the AI agent (provided by OpenAI), to query multiple datasets from a CSV file which has already been provided. 

The script uses several imports, including, pandas to import the CSV file and also data manipulation, os to gain access to environment variables stored in the .env file. Langchain has also been used here as it provides a convenient implementation for the AI agent to interact with the CSV file. 

Unfortunately, while developing this project, I ran into some issues and so the implementation here is not complete and cannot run successfully. While developing the solution, there were several issues that arose in the development environment where the root cause was due to different Python versions already installed on the machine, causing an import conflict that I was regrettably unable to fix within the given timeframe. Due to time taken fixing these issues, I was also unable to incorporate the Dictionary data contained on the .png file into this project.





## Environment Variables

To run this project, you will need to add the following environment variables to a new .env file. These can be obtained from an OPEN AI account.

`OPENAI_API_KEY=`


## Installation

Python will be required to run this project. Langchain is used in this project which requires a Python version of 3.8.1 or higher. Once cloned locally, please navigate into the /AI_CSV_Chatbot folder and use the following commands in terminal.

```bash
  pip install -r requirements.txt
  streamlit run main.py
```