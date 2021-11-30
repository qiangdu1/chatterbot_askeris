# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 13:32:50 2021

"""

from flask import Flask, render_template
from flask import request

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Flash app, used for link to internet browser.
app = Flask(__name__)

# chatbot = ChatBot("L")
chatbot = ChatBot("L", read_only=True)

greetings_openings = open(r"Greetings.txt", "rb").read()
greetings_openings_list = eval(greetings_openings)

#greetings_openings = open("Greetings.txt", "rb").read()
#greetings_openings_list = eval(greetings_openings)

likely_questions = open(r"Likely_questions.txt", "rb").read()
# likely_questions_list = eval(r"likely_questions")
likely_questions_l = likely_questions.decode("utf-8","ignore")
likely_questions_list =eval(likely_questions_l)

print(likely_questions_list)

trainer = ListTrainer(chatbot)

trainer.train(likely_questions_list)




@app.route("/")
def index():
    question = request.args.get("question", "")
    if question:
        answer = get_chatbot_answer(question)
    else:
        answer = ""
    return (
        """<form action="" method="get">
                Question: <input type="text" name="question">
                <input type="submit" value="Get Chatbot's answer">
            </form>"""
        + "Chatbot: "
        + answer
    )

@app.route("/<string:question>")
def get_chatbot_answer(question):
    answer = chatbot.get_response(question)
    print(answer)
    return str(answer)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    
    
    
# # start of the trial part: html 
# # web page structure
# posts = [
#         {
#             'author': 'Corey Schafer',
#             'title': 'Bolg post 1',
#             'content': 'First post content',
#             'date_posted': 'Apriil 20, 2018'
#             }
#         ]


# @app.route("/about")
# def about():
#     return render_template('about.html',posts=posts)
# # end of the trial part: html


# @app.route('/crawl')
# def crawl():
#     return render_template('crawl.html', myfunction=get_chatbot_answer)