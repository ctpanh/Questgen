# from core.Questgen import main
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import AIMessage, HumanMessage, SystemMessage

from server.core.generate_questions import get_questions

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


def getQuestFromText(language, context, type, easy, med, hard):
    num_words = count_words(context)
    outputs = []
    easy_ques = []
    med_ques = []
    diff_ques = []
    if num_words >= 3000:
        print("more than 3000 words")
        chunks = get_chunks(context)
        for chunk in chunks:
            easy_q, med_q, diff_q = get_questions(language=language, context=chunk, type=type, easy=easy, med=med, hard=hard)
            easy_ques.append(easy_q)
            med_ques.append(med_q)
            diff_ques.append(diff_q)
    else:
        print("less than 3000 words")
        easy_ques, med_ques, diff_ques = get_questions(language=language, context=context, type=type, easy=easy, med=med, hard=hard)
    return easy_ques, med_ques, diff_ques

context = load_txt('server/core/article.txt')
easy, med, diff = getQuestFromText("Vietnamese", context, 'boolean', 3, 3, 3)
print(easy)
# print(med)
# print(diff)