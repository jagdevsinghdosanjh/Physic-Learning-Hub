def get_quiz(topic):
    return [
        {
            "question": "What is the SI unit of displacement?",
            "options": ["Meter", "Second", "Kilogram", "Newton"],
            "answer": "Meter"
        },
        {
            "question": "Which equation gives final velocity?",
            "options": ["v = u + at", "s = ut + ½at²", "v² = u² + 2as", "None of these"],
            "answer": "v = u + at"
        },
        {
            "question": "Acceleration is defined as:",
            "options": [
                "Rate of change of velocity",
                "Rate of change of displacement",
                "Rate of change of speed",
                "None of these"
            ],
            "answer": "Rate of change of velocity"
        }
    ]

# def get_quiz(topic):
#     quiz_data = quizzes.find_one({"chapter": topic})
#     return quiz_data["questions"]
