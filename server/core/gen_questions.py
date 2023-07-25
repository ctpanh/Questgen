from pprint import pprint
from pprint import pprint
import nltk
# nltk.download('stopwords')
from Questgen import main

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

def get_questions(context, max_ques=4, type='mcq'):
    # qg = main.QGen()
    payload = {
        "input_text": context,
        "max_questions": max_ques
    }
    # output = qg.predict_mcq(payload)
    if type == "boolean":
        bg = main.BoolQGen() 
        output = bg.predict_boolq(payload)
    if type == "mcq":
        qg = main.QGen()
        output = qg.predict_mcq(payload)
    return output

def run():
    txt_path = 'txt_file/article.txt'
    context = load_txt(txt_path)
    num_words = count_words(context)
    # print(num_words)
    outputs = []
    if num_words >= 3000:
        chunks = get_chunks(context)
        for chunk in chunks:
            output = get_questions(chunk)
    else:
        output = get_questions(context)
        
    pprint (output)
run()