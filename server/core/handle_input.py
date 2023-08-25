# from core.Questgen import main
from langchain.text_splitter import RecursiveCharacterTextSplitter

from server.core.generate_questions import get_questions

def load_txt(txt_path):
    f = open(txt_path, "r", encoding="utf8")
    context = f.read()
    return context

def count_words(context):
    words = context.split()
    num_words = len(words)
    return num_words

def get_chunks(context, max_length=3000, overlap=50):

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
    max_words = 3000
    if num_words >= max_words:
        print("more than 3000 words")
        chunks = get_chunks(context)
        
        easy = easy / len(chunks) + 1
        med = med / len(chunks) + 1 
        hard = hard / len(chunks) + 1
        for chunk in chunks:
            easy_q, med_q, diff_q = get_questions(language=language, context=chunk, type=type, easy=easy, med=med, hard=hard)
            easy_ques.append(easy_q)
            med_ques.append(med_q)
            diff_ques.append(diff_q)
            
            # easy_ques.flatten()
            # med_ques.flatten()
            # diff_ques.flatten()
        easy_ques = [item for sublist in easy_ques for item in sublist]
        med_ques = [item for sublist in med_ques for item in sublist]
        diff_ques = [item for sublist in diff_ques for item in sublist]
            

    else:
        print("less than 3000 words")
        easy_ques, med_ques, diff_ques = get_questions(language=language, context=context, type=type, easy=easy, med=med, hard=hard)
    return easy_ques, med_ques, diff_ques

context = load_txt('/mnt/banana/k66/thuy/Questgen/server/core/his_geo.txt')
easy, med, diff = getQuestFromText("Vietnamese", context, 'fill in blank', 5, 5, 5)
print(easy)
print('----------------------')
print(med)
print('----------------------')
print(diff)