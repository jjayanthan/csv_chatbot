# CSV Chatbot

This is a Python based chatbot project, which allows the user to interact with the AI agent (provided by OpenAI), to query multiple datasets from a CSV file which has already been provided. 

Langchain Pandas Dataframe Agent has been used here as it provides a convenient implementation for the AI agent to interact with more then one CSV file. 

While the initial dictionary was given as a .png file, the data was converted into a .csv file for ease of implementation. (Please note, I have tried to do another implementation on the doc-loader-chatbot branch with multiple file types, however this had some limitations).


## Environment Variables

To run this project, you will need to create a constants.py file. Please see constants.py.default to use as a template. 
The OpenAI API Key should be added to the constants.py file, as below, but replace the "sk-..." with your own OpenAI API Key.

`APIKEY = "sk-..."`


## Installation

Python will be required to run this project. Langchain is used in this project which requires a Python version of 3.8.1 or higher. I have used Python 3.10. Once cloned locally, please navigate into the /csv_chatbot folder and use the following commands in terminal.

```bash
  pip install -r requirements.txt
  python chatbot.py
```
When started up, you should see something like below show in terminal. You can type your questions regarding the CSV file where it says Query: in green. 

<img width="921" alt="Screenshot 2023-10-27 at 01 40 31" src="https://github.com/jjayanthan/csv_chatbot/assets/142901385/0abce7cc-62c8-481d-a8bf-989f4b05994b">


