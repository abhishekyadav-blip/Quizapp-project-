# 3. user_interaction.py

def display_question(q_data):
    print(f"\n{q_data['question']}")
    for option in q_data["options"]:
        print(option)

def get_user_answer():
    return input("Your answer: ").lower()
