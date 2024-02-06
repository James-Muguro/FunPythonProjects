class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_prompts = [
    "What is the capital of Kenya?\n(a) Nairobi\n(b) Mombasa\n(c) Kisumu\n\n",
    "Which language is Python?\n(a) Scripting\n(b) Programming\n(c) Markup\n\n",
    "What is the largest planet?\n(a) Earth\n(b) Mars\n(c) Jupiter\n\n",
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "c"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct")

run_quiz(questions)