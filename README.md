# Questgen

## 📌  Introduction
Questgen creates questions and answers based on your document.

**Type of questions:**
✅ True/False question <br>
✅ Multiple choice question <br>
✅ Fill in blank question <br>

**Level of questions:**
✅ Easy <br>
✅ Medium <br>
✅ Hard <br>

## 📌  Demo
** True/False question
- Easy
- Medium
- Hard
** Multiple choice question
- Easy:
  Question: What is Object Oriented Programming?
  Options:
    A programming pattern where programs are structured around objects
    A programming pattern where programs are structured around functions
    A programming pattern where programs are structured around logic
    A programming pattern where programs are structured around data
  True option: A programming pattern where programs are structured around objects
- Medium:
  Question: What does Abstraction help in?
  Options:
    Data hiding process
    Displaying essential features without showing details
    Avoiding unnecessary information or irrelevant details
    All of the above
  True option: All of the above
- Hard:
  
** Fill in blank question
- Easy
  Question: OOPs stands for Object Oriented __________ C++., 
  Options:
      a) Programming
      b) Polymorphism
      c) Inheritance
      d) Abstraction 
  True option: a) Programming
- Medium:
  Question: Abstraction allows hiding __________ implementation details and exposing a simplified interface to the user.
  Options:
      a) complex
      b) unnecessary
      c) irrelevant
      d) essential
  True option: a) complex
- Hard:
  Question: Inheritance establishes a __________ relationship among classes, reflecting real-world or conceptual hierarchies.
  Options':
      a) hierarchical
      b) polymorphic
      c) encapsulated
      d) abstract
  True option: a) hierarchical

## 🚀  Quickstart
```bash
# clone project
git clone https://github.com/ctpanh/Questgen.git
cd Questgen

# [OPTIONAL] create conda environment
conda create -n myenv python=3.9
conda activate myenv

# install requirements
pip install -r requirements.txt
```


## Main Technologies
- Frontend:
- Backend:
- AI: OpenAI

## Project Structure

The directory structure of new project looks like this:

```

├── client                   <- Frontend
│   ├── .vscode                  <- vscode file
│   ├── public                   <- Bo cai nay di
│   └──  src                     <- Source code
|         ├── assets                 <- 
│         ├── components             <- 
│         ├── router                 <- 
│         ├── store                  <- 
│         ├── view                   <- 
│         ├── App.vue                <- 
│         └── main.js                <- 
├── server                   <- Backend
    ├── core                      <- Core part to generate questions
    |    ├── article.txt             <- Document to generate questions
    |    ├── generate_questions.py   <- Generate questions
    |    ├── handle_input.py         <- Handle long input file
    |    └── prompt.py               <- Prompt to ask OpenAI
    ├── questgen                     <-
    └── server                       <-

```
