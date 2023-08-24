#main
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from server.core.prompt import tfq_template, mcq_template, fill_in_blank_template 
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import re

def contains_character(input_string, character):
    return input_string.find(character) != -1

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
            # print("check: " + item)
            key, value = item.split(': ', 1)
            if (key.find("Question") != -1):
                current_question = {}
                current_question['question'] = value
                current_question['options'] = []  # Initialize 'option' as an empty list
                current_question['true option'] = []  # Initialize 'true option' as an empty list
            elif (key.find("Option") != -1): 
                current_question['options'].append(value)
            elif (key.find("True option") != -1):
                current_question['true option'].append(value)
                questions[current_difficulty].append(current_question)
            else:
                continue

    return questions['easy'], questions['medium'], questions['hard']

def generate_questions(language, context, type, easy_num, med_num, hard_num):
    chat = ChatOpenAI(temperature=0, openai_api_key=os.getenv('OPENAI_API_KEY'))
    
    template = ""
    if type == "boolean":
        template = tfq_template
    if type == "multiple choice":
        template = mcq_template
    if type == "fill in blank":
        template = fill_in_blank_template

    human_message_prompt = HumanMessagePromptTemplate.from_template(template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [human_message_prompt]
    )

    res = chat(
        chat_prompt.format_prompt(
            language=language, num_questions=10, type=type, easy_num=easy_num, med_num=med_num, hard_num=hard_num, context=context
        ).to_messages()
    )
    # print(res)
    return res


def get_questions(language, context, type, easy, med, hard):
    output = generate_questions(language = language, context=context, type=type, easy_num=easy, med_num=med, hard_num=hard)
    # print(output)
    questions_list = output.to_json()['kwargs']['content']
    questions_list = questions_list.split("\n")
    questions_list = [item for item in questions_list if item != ""]
    easy_q = []
    medium_q = []
    hard_q = []
    
    if type == "boolean":
        easy_q, medium_q, hard_q = extract_tfq(questions_list)
    else:
        easy_q, medium_q, hard_q = extract_mcq(questions_list)

    return easy_q, medium_q, hard_q
def load_txt(txt_path):
    f = open(txt_path, "r", encoding="utf8")
    context = f.read()
    return context