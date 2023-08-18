tfq_template = (
    """Create true or false statements and their answers and their explanations (all statements, answers and explanations are in {language}) with {easy_num} easy questions, {med_num} medium questions, {hard_num} difficult questions to help users learn about the following context: {context}.
    Translate all statements, answers and explantions into {language}
    Please give the response strictly follow below format and don't add or change character/word.
    ###
    Desired format:
    Easy question: 
    statement: -||- 
    answer: -||-
    explanation: -||-
    (all the easy question)
    ...
    Medium question:
    (all the medium question)
    ...
    Difficult question:
    (all the difficult question)
    ...
    ###
    """
)
mcq_template = (
    """You are a helpful assistant that create multiple choice questions and their answers with {easy_num} easy questions, {med_num} medium questions, {hard_num} difficult questions about the following context: {context}.
    Please give the response strictly follow below format and don't add or change character/word.
    
    ###
    Desired format:
    Easy question:
    Question: Who directed the Disney film Cinderella in 2015?
    Option: Branagh Kenneth
    Option: Walt Disney
    Option: Charles Perrault
    Option: Chris Weitz
    True option: Branagh Kenneth
    (all the easy question)
    ...
    Medium question:
    Question: -||-
    Option: -||-
    Option: -||-
    Option: -||-
    Option: -||-
    True option: -||-
    (all the medium question)
    ...
    Difficult question:
    Question: -||-
    Option: -||-
    Option: -||-
    Option: -||-
    Option: -||-
    True option: -||-
    (all the difficult question)
    ...
    ###
    """
)
fill_in_blank_template = (
    """You are a helpful assistant that create fill in blank questions and their answers with {easy_num} easy questions, {med_num} medium questions, {hard_num} difficult questions about the following context: {context}.
    Please give the response strictly follow below format and don't add or change character/word:
    
    ###
    Desired format:
    Easy question:
    Question: (question with blank)
    Option: -||-
    Option: -||-
    Option: -||-
    Option: -||-
    True option: -||-
    (all the easy question)
    ...
    Medium question:
    (all the medium question)
    ...
    Difficult question:
    (all the difficult question)
    ...
    ###
    """
)