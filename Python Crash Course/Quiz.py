from Questions import Question

question_prompts = [
    "How many sequences are present in AC - Unity?\n(a) 11\n(b) 3\n(c) 8\n(d) 17\n\n",
    "What was the name of Barny Stinson's best friend in 'How I Met Your Mother'?\n(a) Matthew Perry\n(b) Marshall "
    "White\n(c) Ted Mosby\n(d) Rachel McDawes \n\n",
    "What is the antonym for perseverance? \n(a) Persistence \n(b) Spunk \n(c) Cowardice\n(d) Idleness\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)