# 5. quiz_data.py

def get_quiz_data():
    return {
        1: {
            "question": "What is the output of print(2**3)?",
            "options": ["a) 6", "b) 8", "c) 9", "d) 4"],
            "answer": "b",
        },
        2: {
            "question": "Which of these is a mutable data type in Python?",
            "options": ["a) Tuple", "b) String", "c) List", "d) Integer"],
            "answer": "c",
        },
        3: {
            "question": "What keyword is used to define a function in Python?",
            "options": ["a) define", "b) func", "c) def", "d) lambda"],
            "answer": "c",
        
        },
        4: {
            "question": "What is the purpose of the `pass` statement in Python?",
            "options": ["a) To skip an iteration in a loop", "b) To exit a loop", "c) To do nothing and avoid syntax errors", "d) To raise an exception"],
            "answer": "c",
        },
        5: {
            "question": "Which method is used to add an element to a set?",
            "options": ["a) append()", "b) add()", "c) insert()", "d) extend()"],
            "answer": "b",
        },
        6: {
            "question": "What is the output of the following code?\nx = [1, 2, 3]\nprint(x[1])",
            "options": ["a) 1", "b) 2", "c) 3", "d) IndexError"],
            "answer": "b",
        },
        7: {
            "question": "Which of the following is **not** a keyword in Python?",
            "options": ["a) class", "b) try", "c) catch", "d) finally"],
            "answer": "c",
        },
        8: {
            "question": "What will be the output of the following code?\nprint(\"Hello, World!\".replace(\"World\", \"Python\"))",
            "options": ["a) Hello, World!", "b) Hello, Python!", "c) Hello, Python", "d) Error"],
            "answer": "b",
        },
        9: {
            "question": "What is the result of the following expression?\n5 // 2",
            "options": ["a) 2", "b) 2.5", "c) 3", "d) Error"],
            "answer": "a",
        },
        10: {
            "question": "Which of the following is true about Python functions?",
            "options": ["a) A function can return multiple values.", "b) A function must always return a value.", "c) A function can take unlimited arguments.", "d) Both a and c"],
            "answer": "d",
        }

    }

def get_total_questions():
    return len(get_quiz_data())  #total numbers in quiz
