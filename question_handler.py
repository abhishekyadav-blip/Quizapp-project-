# 2. question_handler.py
from quiz_data import get_quiz_data

def get_question(q_no):
    quiz_data = get_quiz_data()
    return quiz_data.get(q_no)

def get_all_questions():
    return get_quiz_data()
