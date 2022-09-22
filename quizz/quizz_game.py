from Question import Question

question_prompt = [
    "What collor are apples? \n(a) red/green\n(b)purple\n(c)orange",
    "What collor are bananas? \n(a) red/green\n(b)yellow\n(c)orange",
    "What collor are strawberries? \n(a) red/green\n(b)purple\n(c)orange"
]
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You gott " +str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)