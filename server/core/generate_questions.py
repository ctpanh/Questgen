#main
import os
# from dotenv import load_dotenv
# load_dotenv()
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from core.prompt import tfq_template, mcq_template, fill_in_blank_template 
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

def generate_questions(context, type, easy_num, med_num, hard_num):
    chat = ChatOpenAI(temperature=0, openai_api_key="")
    
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
            num_questions=10, type=type, easy_num=easy_num, med_num=med_num, hard_num=hard_num, context=context
        ).to_messages()
    )
    # question = process(res, easy_num, med_num, hard_num)
    return res


def get_questions(context, type, easy, med, hard):
    output = generate_questions(context=context, type=type, easy_num=easy, med_num=med, hard_num=hard)
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
def load_txt(txt_path):
    f = open(txt_path, "r", encoding="utf8")
    context = f.read()
    return context

context = """ Cinderella is a Disney romantic and fantasy film produced in 2015, a screenplay authored by Chris Weitz and directed by Branagh Kenneth. The film’s co-producers consist of Walt Disney Pictures, Beagle Plug Films, Allison Shearmur Productions, and Kinberg Genre. Cinderella bases its storyline on a folktale hence a live-action conceptualization of the animated film that bore the same name that Walt Disney produced in the 1950s. I chose Cinderella,2015 because it portrays how the main character exhibits great values of generosity and kindness and is unwilling to abdicate these values even in the face of adversity even though she is surrounded by cruel people (Walt Disney Studios,2015). The film features the story of a kind and courageous girl whose life as a slave girl in her stepmother’s care is transformed by a bit of glass shoe.
The main character in the story is referred to as Ella. After her mother’s unexpected and unanticipated death, her rich father remarries and travels abroad; hence, she is forced to live with her cruel stepmother, Lady Tremaine, and her naughty stepsisters Drisella and Anastasia, who treat her like a slave. However, her status is transformed when she cannot attend the royal ball where the prince seeks a wife. She is visited by a fairy godmother who transforms her into a princess with glass shoes, which will change her life forever after it falls off while she was leaving the ball. Ella is meant to be an exhibition of humility, courage and kindness, and inner beauty. Cinderella kicks off with Ella as a small girl who, from a very tender age, is taught by her mother to believe that magic exists and that all that is needed to survive is kindness and courage (Walt Disney Studios,2015). Representation in terms of gender portrays women as demeaned by society in numerous aspects. Women are denied the liberty of choice and believe that in life, marriage is the ultimate goal.
Male dominance is exhibited by the royal family when they hold a royal ball, requiring all women to attend to enable Prince Kit to select his well-desired bride. The man is considered stereotypical who is only troubled with finding a beautiful bride. The prince exhibits that in society, a man is only recognized by his wealth which guarantees him independence and a listening ear. Prince Kit was thus desirable by women because he assured security in terms of provision (Walt Disney Studios,2015).
Cinderella is a folktale that speaks of oppression and yields that are triumphant. Women, who are usually belittled by society, are seen to have transformative gains since they end up in powerful positions, in this case, a princess. Cinderella has been described in terms of numerous setups, but the first and most outstanding variant is that of Rhodopids retrieved by a geographer from Greece known as Strabo between 7Bc and AD23. The story demonstrates how a Greek slave gets married to an Egyptian king. However, it is necessary to note that Disney based its report on a tale written by Charles Perrault, whose story revolves around a girl with a cruel stepmother and evil stepsisters force to serve them.
 """

# easy, medium, hard = get_questions(context=context, type="boolean", easy=0, med=0, hard=0)
# print(easy)
# print(medium)
# print(hard)
# tf = contains_character("1. true option ne ne", "true option")
# print(tf)