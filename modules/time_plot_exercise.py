# Program to help the user type faster. Give him a word and ask him to write it five times.
# Check how many seconds it took him to type the word at each round

import time as t
import matplotlib.pyplot as plt

max_attempts = 5
current_attempt = 1
mistakes = 0
attempts = [1, 2, 3, 4, 5]
times = []


def getword(word):
    print(f"The word to test your velocity is '{word}', try to type as fast as you can!")
    return word


def readyToStart():
    return f"Ready to start, press 'y' to continue: "


def countMistakes():
    return f"Number of mistakes: {mistakes}"


def calculateMiliseconds(time_seconds):
    return time_seconds * 1000


def appendTime(time_to_add):
    times.append(time_to_add)


def plotInformation():
    plt.bar(attempts, times)
    plt.ylabel("Time [ms]")
    plt.xlabel("Attempts")
    plt.show()


main_word = getword("iron man")
print(main_word)
enter = input(readyToStart())

if enter.upper() == 'Y':
    while current_attempt <= max_attempts:
        print(f"Attempt {current_attempt}: GO!!!")
        start_time = t.time()
        word = input()
        end_time = t.time()
        appendTime(calculateMiliseconds(end_time - start_time))
        if word.lower() != main_word:
            mistakes += 1
        current_attempt += 1

print(countMistakes())
plotInformation()
