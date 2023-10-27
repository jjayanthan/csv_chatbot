# CSV Chatbot

This is a Python based chatbot project, which allows the user to interact with the AI agent (provided by OpenAI), to query multiple different files from a directory, here I have used a .csv file and have converted the provided .png to a .pdf file, as Langchain Document Loader does not currently have a document loader which works with .png files.

While this initially seemed like a good solution, the chatbot didn't seem to be reading the entire CSV file as seen in the screenshot below. 

After researching online, it seems that this is a common issue with Langchain Document Loader, where the results are only correct some of the time. This apparently is because the OpenAI token limit is 4096 tokens and so only 6-7 chunks of text can be sent from the Vector DB used, thus the CSV file provided is too large. This however, is a good solution to query smaller documents of various types.


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
When started up, you should see something like below show in terminal. You can type your questions regarding the CSV file where it says Query: in green. Also, when running this script, it may work better in a virtual environment.
