
import os
import openai
import sys
import sys
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
sys.path.append('../..')
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY'] 

def extract_tfq(question_list):
    questions = {
        'easy': [],
        'medium': [],
        'hard': []
    }
    current_difficulty = None
    current_question = None

    for item in question_list:
        if (item.find("Easy question") != -1):
            current_difficulty = 'easy'
        elif (item.find("Medium question") != -1):
            current_difficulty = 'medium'
        elif (item.find("Difficult question") != -1):
            current_difficulty = 'hard'
        elif current_difficulty:
            key, value = item.split(': ', 1)
            if key.find('Statement') != -1:
                current_question = {}
                current_question['question'] = value
                current_question['answer'] = []  # Initialize 'option' as an empty list
                current_question['explanation'] = []  # Initialize 'true option' as an empty list
            elif key.find('Answer') != -1:
                current_question['answer'] = value
            elif key.find('Explanation') != -1:
                current_question['explanation'] = value
                questions[current_difficulty].append(current_question)
            else:
                continue

    return questions['easy'], questions['medium'], questions['hard']

def extract_mcq(question_list):
    questions = []

    current_question = {}

    for item in question_list.split('\n'):
        if "Easy question" in item:
            current_question['difficulty'] = 'easy'
        elif "Medium question" in item:
            current_question['difficulty'] = 'medium'
        elif "Difficult question" in item:
            current_question['difficulty'] = 'hard'
        elif ': ' in item:
            key, value = item.split(': ', 1)
            if key == 'Question':
                current_question['question'] = value
                current_question['options'] = []
                current_question['true option'] = []
            elif key.startswith('Option'):
                current_question['options'].append(value)
            elif key == 'True option':
                current_question['true option'].append(value)

                # When we have collected all information for the current question, add it to the list
                questions.append(current_question)
                current_question = {}

    return questions
def delete_file():
    import shutil
    chroma_dir = 'server\server\core\chroma'
    for root, dirs, files in os.walk(chroma_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            os.remove(file_path)
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            shutil.rmtree(dir_path)

def load_file(path = r'C:\Users\User\Desktop\WebAI\Questgen\server\core\cinderella.txt'):
    #delete file
    delete_file()
    #load file
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(find_dotenv())
    from langchain.document_loaders import TextLoader
    loader = TextLoader(file_path=path)
    doc = []
    doc.extend(loader.load())
    persist_directory = 'server\server\core\chroma'
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding
    )
    vectordb.add_documents(documents=doc)

from core.prompt import *
def genquests(type, e, m, h):
    template = ""
    if type == "boolean":
        template = tfq_template
    if type == "multiple choice":
        template = mcq_template
    if type == "fill in blank":
        template = fill_in_blank_template
    question = template.format(easy_num=e, med_num=m,hard_num=h)
    import datetime
    current_date = datetime.datetime.now().date()
    if current_date < datetime.date(2023, 9, 2):
        llm_name = "gpt-3.5-turbo-0301"
    else:
        llm_name = "gpt-3.5-turbo"
    from langchain.vectorstores import Chroma
    from langchain.embeddings.openai import OpenAIEmbeddings
    persist_directory = 'server\server\core\chroma'
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    llm = ChatOpenAI(model_name=llm_name, temperature=0)
    from langchain.chains import RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever(search_kwargs={"k": 1})
    )
    result = qa_chain({"query": question})
    # print(result["result"])
    return result["result"]

# load_file()
str = genquests("multiple choice", 1, 1, 1)
print(type(str))
# # print(str)
# a = extract_mcq(str)
# print(a)