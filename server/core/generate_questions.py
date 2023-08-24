#main
import os
from langchain.chat_models import ChatOpenAI
from core.prompt import *
from core.handle_input import *

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
            # current_question = {}
        elif (item.find("Medium question") != -1):
            current_difficulty = 'medium'
            # current_question = {}
        elif (item.find("Difficult question") != -1):
            current_difficulty = 'hard'
            # current_question = {}
        elif current_difficulty:
            # print(item.split(': ', 1))
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
                # print("go here")
                questions[current_difficulty].append(current_question)
                # print(current_question)
            else:
                continue

    return questions['easy'], questions['medium'], questions['hard']

def extract_mcq(question_list):
    print(question_list)
    questions = {
        'easy': [],
        'medium': [],
        'hard': []
    }
    current_difficulty = None
    current_question = None

    for item in question_list:
        if "Easy question" in item:
            current_difficulty = 'easy'
        elif "Medium question" in item:
            current_difficulty = 'medium'
        elif "Difficult question" in item:
            current_difficulty = 'hard'
        elif current_difficulty and ': ' in item:
            key, value = item.split(': ', 1)
            if key == 'Question':
                current_question = {}
                current_question['question'] = value
                current_question['options'] = []  # Initialize 'options' as an empty list
                current_question['true option'] = []  # Initialize 'true option' as an empty list
            elif key.startswith('Option'):
                current_question['options'].append(value)
            elif key == 'True option':
                current_question['true option'].append(value)
                questions[current_difficulty].append(current_question)

    # Remove empty lists for 0 questions
    questions['easy'] = [q for q in questions['easy'] if q['question']]
    questions['medium'] = [q for q in questions['medium'] if q['question']]
    questions['hard'] = [q for q in questions['hard'] if q['question']]

    return questions['easy'], questions['medium'], questions['hard']

# def generate_questions(context, type, easy_num, med_num, hard_num):
#     chat = ChatOpenAI(temperature=0, openai_api_key="")
    
#     template = ""
#     if type == "boolean":
#         template = tfq_template
#     if type == "multiple choice":
#         template = mcq_template
#     if type == "fill in blank":
#         template = fill_in_blank_template

#     human_message_prompt = HumanMessagePromptTemplate.from_template(template)

#     chat_prompt = ChatPromptTemplate.from_messages(
#         [human_message_prompt]
#     )

#     res = chat(
#         chat_prompt.format_prompt(
#             num_questions=10, type=type, easy_num=easy_num, med_num=med_num, hard_num=hard_num, context=context
#         ).to_messages()
#     )
#     # question = process(res, easy_num, med_num, hard_num)
#     return res


def get_questions(type, easy, med, hard):
    output = genquests(type=type, e=easy, m=med, h=hard)
    # print(output)
    questions_list = output.to_json()['kwargs']['content']
    questions_list = questions_list.split("\n")
    questions_list = [item for item in questions_list if item != ""]
    # print(questions_list)
    easy_q = []
    medium_q = []
    hard_q = []
    if type == "boolean":
        easy_q, medium_q, hard_q = extract_tfq(questions_list)
        # print(easy)
    else:
        easy_q, medium_q, hard_q = extract_mcq(questions_list)
    # print(easy)
    # print(medium)
    # print(hard)
    return easy_q, medium_q, hard_q
# def load_txt(txt_path):
#     f = open(txt_path, "r", encoding="utf8")
#     context = f.read()
#     return context
