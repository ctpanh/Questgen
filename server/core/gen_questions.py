from pprint import pprint
# nltk.download('stopwords')
from core.Questgen import main
from langchain.text_splitter import RecursiveCharacterTextSplitter

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

def getQuestFromFile(file_path):
    # context = load_txt(file_path)
    # num_words = count_words(context)
    # outputs = []
    # if num_words >= 3000:
    #     chunks = get_chunks(context)
    #     for chunk in chunks:
    #         output = get_questions(chunk)
    # else:
    #     output = get_questions(context)
    # return output
    context = load_txt(file_path)
    chunks = get_chunks_2(context=context, length=500, overlap=50)
    outputs = []
    for i in range(0, len(chunks) -1):
        chunk_output = get_questions(chunks[i].page_content)
        outputs.append(chunk_output)
    print(outputs)
    return outputs


def getQuestFromText(context):
    num_words = count_words(context)
    outputs = []
    if num_words >= 3000:
        chunks = get_chunks(context)
        for chunk in chunks:
            output = get_questions(chunk)
    else:
        output = get_questions(context)
        
    return output

# pprint(getQuest('core/article.txt'))

context = load_txt(r"C:\Users\User\Desktop\New folder\Questgen\server\core\article.txt")
# print("CHUNK1: ")
print(get_chunks_2(context=context, length=500, overlap=50)[0].page_content)

# print("CHUNK2:")
# print(get_chunks(context=context, max_length=500, overlap=50)[0])
# print(getQuestFromFile(r"C:\Users\User\Desktop\New folder\Questgen\server\core\article.txt"))