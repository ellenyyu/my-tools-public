'''
FAISS.add_texts() has a bug and so I am

Adding notes as a multi-line string to a list in a .txt file 

and ingesting all notes 

until the bug is fixed 
'''
import re
import json
import streamlit as st 
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(layout="wide")

NOTES_FILEPATH = 'my-notes.json'
EMBEDDING_MODEL = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
HEIGHT = 800

# Helper functions
def add_string_to_dict_in_json_file(new_string):   
    try:
        with open(NOTES_FILEPATH, 'r') as file:
            data = json.load(file)
    except:
        data = {}  # Initialize as an empty list if file does not exist

    count = len(data)
    # Add the new entry to the JSON data
    data.update({count: new_string})

    # Write the updated JSON data back to the file
    with open(NOTES_FILEPATH, 'w') as file:
        json.dump(data, file, indent=4)

def return_to_empty():
    return None

def add_line_breaks(text):
    # Add a line break before exactly ###
    text = re.sub(r'(?<!\n)(###)', '\n###', text)  # Add a newline before ####
    # Add a line break before exactly ####
    text = re.sub(r'(?<!\n)(####)', '\n####', text)  # Add a newline before ###
    # Add a line break before numbered lists (1. 2. 3. etc.)
    text = re.sub(r'(?<!\n)(?=\d+\.)', '\n', text)
    # Add a line break before ```
    text = re.sub(r'(?<!\n)(?=```)', '\n', text)
    # Add a line break before -
    text = re.sub(r'(?<!\n)(?=-)', '\n', text)

    # Add a line break after "python" within triple backticks
    text = re.sub(r'(```python)(?!\n)', r'\1\n', text)
    # Add a line break before import
    text = re.sub(r'(?<!\n)(?=import)', '\n', text)
    # Add a line break before async def
    text = re.sub(r'(?<!\n)(?=async def)', '\n', text)
    # Add a line break after `):` within the code block
    text = re.sub(r'\):', '):\n', text)  # Match `):` followed by optional whitespace
    # Add a line break after ) followed by more than four whitespaces
    text = re.sub(r'\)(?=\s{4,})', ')\n', text)  # Match ) followed by 4 or more whitespaces

    return text



with st.sidebar:
    new_note = st.text_area('Enter new note', height=HEIGHT, on_change=return_to_empty())
    
if len(new_note) > 1:
    add_string_to_dict_in_json_file(new_note)
try:
    with open(NOTES_FILEPATH, 'r') as file:
        my_notes = json.load(file)
except:
    st.warning("""You don't have any notes in your database!""")

try: 
    vector_store = FAISS.from_texts(my_notes.values(), EMBEDDING_MODEL)
except: 
    pass


query, result = st.columns(2)
with query:
    query = st.text_input('Query notes',on_change=return_to_empty())

    col1, col2 = st.columns(2)
    with col1: 
        as_is = st.checkbox('Return notes as is', help='This feature is currently being developed')
    with col2: 
        context = st.checkbox('Return notes as context', help='This feature is currently being developed')



with result:
    retriever = vector_store.as_retriever()

    st.markdown(add_line_breaks(retriever.invoke(query)[0].page_content))


