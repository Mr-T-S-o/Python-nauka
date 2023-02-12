import json

points = 0

with open("quiz.json") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        print(questions[i])