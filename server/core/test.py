# from core.pipelines import pipeline
from core import pipelines

text = """Lyly is a student of University of Engineering and Technology, her major is Information Technology. She loves coding but hates learning Calculus.
She plans to learn Japanese this summer."""

text2 = "Gravity (from Latin gravitas, meaning 'weight'), or gravitation, is a natural phenomenon by which all \
things with mass or energy—including planets, stars, galaxies, and even light—are brought toward (or gravitate toward) \
one another. On Earth, gravity gives weight to physical objects, and the Moon's gravity causes the ocean tides. \
The gravitational attraction of the original gaseous matter present in the Universe caused it to begin coalescing \
and forming stars and caused the stars to group together into galaxies, so gravity is responsible for many of \
the large-scale structures in the Universe. Gravity has an infinite range, although its effects become increasingly \
weaker as objects get further away"

text3 = "42 is the answer to life, universe and everything."

text4 = "Forrest Gump is a 1994 American comedy-drama film directed by Robert Zemeckis and written by Eric Roth. \
It is based on the 1986 novel of the same name by Winston Groom and stars Tom Hanks, Robin Wright, Gary Sinise, \
Mykelti Williamson and Sally Field. The story depicts several decades in the life of Forrest Gump (Hanks), \
a slow-witted but kind-hearted man from Alabama who witnesses and unwittingly influences several defining \
historical events in the 20th century United States. The film differs substantially from the novel."



from transformers import pipeline
# # from rake_nltk import Rake
# import nltk
# from Questgen import main
# from pprint import pprint

def summarize(article_path):
    # Open and read the article
    f = open(article_path, "r", encoding="utf8")
    # f = open("/mnt/bk66/thuy/ask-multiple-pdfs/Questgen.ai/article.txt", "r", encoding="utf8")
    to_tokenize = f.read()

    # Initialize the HuggingFace summarization pipeline
    summarizer = pipeline("summarization")
    summarized = summarizer(to_tokenize, min_length=75, max_length=300)
    summary = summarized[0]['summary_text']
    # Print summarized text
    print(summary)
    return summary

def genQuest(input_txt):
    nlp = pipelines.pipeline("question-generation", model="valhalla/t5-base-qg-hl")
    # print(nlp(input_txt))
    output = nlp(input_txt)
    return output

def getQuest(file):
    # article_path = "article.txt"
    # summarized = summarize(file)
    return genQuest("""A young girl named Lily was known for her kind heart and adventurous spirit . She had always dreamt of embarking on an exciting journey beyond the borders of her village . One day, while climbing a steep mountain, she came across a hidden cave and discovered a sparkling crystal . As she touched the crystal, a surge of energy coursed through her veins, granting her incredible powers . She became known as 
the Guardian of Imagination .""")

if __name__ == '__main__':
    article_path = "article.txt"
    summarized = summarize(article_path)
    result = genQuest(summarized)