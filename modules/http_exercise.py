import json
import requests
import html
import random

url = "https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple"
print(f"Welcome to the trivia Games, let's start.")


def get_question(data):
    return data['results'][0]['question']


def get_incorrect_answers(data):
    return data['results'][0]['incorrect_answers']


def get_correct_answer(data):
    return data['results'][0]['correct_answer']


def show_question_answers(question, answers):
    print(f"Question: {html.unescape(question)}")
    position_answer = 0
    answer_number = 1
    for answer in answers:
        if answer == correct_answer:
            position_answer = answer_number
        print(f"{str(answer_number)} - {answer}")
        answer_number += 1

    answer_user = input("Answer: ")

    message = "CORRECT!" if answer_user == str(position_answer) else "INCORRECT!"
    print(message)


while True:
    data = json.loads(requests.get(url).text)
    # print(html.unescape(json.dumps(data, indent=4, sort_keys=True)))

    question = get_question(data)
    answers = get_incorrect_answers(data)
    correct_answer = get_correct_answer(data)
    answers.append(correct_answer)
    random.shuffle(answers)
    show_question_answers(question, answers)
    exit_game = input(f"\nPlease type 'q' to finish or 'c' to continue: ")
    if exit_game.lower() == 'q':
        break
