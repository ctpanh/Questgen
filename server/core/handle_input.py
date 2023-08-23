# from core.Questgen import main
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os
import openai
import sys
import sys
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
sys.path.append('../..')
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY'] 

from generate_questions import get_questions, generate_questions

def load_txt(txt_path):
    f = open(txt_path, "r", encoding="utf8")
    context = f.read()
    return context

def count_words(context):
    words = context.split()
    num_words = len(words)
    return num_words

def get_chunks(context, max_length=500, overlap=50):

    # chunks = [context[i:i+max_length] for i in range(0, len(context), max_length)]
    chunks = [context[i:i+max_length] for i in range(0, len(context), max_length - overlap)]
    return chunks

def get_chunks_2(context, length, overlap):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = length,
        chunk_overlap = overlap,
        length_function = len,
        add_start_index = True
    )
    return text_splitter.create_documents([context])


def getQuestFromText(context, type, easy, med, hard):
    num_words = count_words(context)
    outputs = []
    easy_ques = []
    med_ques = []
    diff_ques = []
    if num_words >= 3000:
        print("more than 3000 words")
        chunks = get_chunks(context)
        for chunk in chunks:
            easy_q, med_q, diff_q = get_questions(chunk, type, easy=easy, med=med, hard=hard)
            easy_ques.append(easy_q)
            med_ques.append(med_q)
            diff_ques.append(diff_q)
    else:
        print("less than 3000 words")
        easy_ques, med_ques, diff_ques = get_questions(context, type, easy=easy, med=med, hard=hard)
    return easy_ques, med_ques, diff_ques

def delete_file():
    import shutil
    chroma_dir = 'server\core\chroma'
    for root, dirs, files in os.walk(chroma_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            os.remove(file_path)
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            shutil.rmtree(dir_path)

def load_file(path = r'C:\Users\User\Desktop\WebAI\Questgen3\Questgen\server\core\cinderella.txt'):
    #delete file
    delete_file()
    #load file
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(find_dotenv())
    from langchain.document_loaders import TextLoader
    loader = TextLoader(file_path=path)
    doc = []
    doc.extend(loader.load())
    persist_directory = 'server\core\chroma'
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding
    )
    vectordb.add_documents(documents=doc)

from prompt import *
def ask_and_answer(question= "generate 5 questions about polymorphysm"):
    question = mcq_template_test.format(easy_num=1, med_num=1,hard_num=1)
    import datetime
    current_date = datetime.datetime.now().date()
    if current_date < datetime.date(2023, 9, 2):
        llm_name = "gpt-3.5-turbo-0301"
    else:
        llm_name = "gpt-3.5-turbo"
    from langchain.vectorstores import Chroma
    from langchain.embeddings.openai import OpenAIEmbeddings
    persist_directory = 'server\core\chroma'
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    llm = ChatOpenAI(model_name=llm_name, temperature=0)
    from langchain.chains import RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectordb.as_retriever()
    )
    result = qa_chain({"query": question})
    print(result["result"])

load_file()
ask_and_answer()
# context = load_txt('server/core/article.txt')
# easy, med, diff = getQuestFromText(context, 'fill in blank', 8, 8, 9)
# print(easy)
# print(med)
# print(diff)