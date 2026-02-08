# 1. main.py
from question_handler import get_all_questions
from user_interaction import display_question, get_user_answer
from scoring import check_answer, calculate_score

def start_quiz():
    questions = get_all_questions()
    score = 0

    for q_no, q_data in questions.items():
        display_question(q_data)
        user_answer = get_user_answer()   
        
        if check_answer(user_answer, q_data["answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q_data['answer']}.")

    print("\nQuiz Complete!")
    print(calculate_score(score, len(questions)))

def main():
    print("Welcome to the Python Quiz!")
    print("Answer the following questions by typing a, b, c, or d.")
    start_quiz()

if __name__ == "__main__":
    main()  
