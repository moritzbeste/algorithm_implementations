import random
import time
import sys


def read_file(filename = "alphabets.txt", result = []):
    try:
        with open(filename, "r") as file:
            for line in file:
                key, value = line.rstrip("\n").split("|", 1)
                if isinstance(result, list):
                    result.append((key, value))
                elif isinstance(result, dict):
                    result[key] = value
    except FileNotFoundError:
        raise FileNotFoundError(f"The {filename} file was not found. Fatal Error.")
    return result


def practice(alphabet):
    score = 0
    wrong = {}
    start_time = time.time()
    for key in random.sample(list(alphabet.keys()), len(alphabet)):
        guess = input(f"{key} : ").strip().lower()
        if guess == alphabet[key]:
            score += 1
        else:
            wrong[key] = guess
    end_time = time.time()
    return score, wrong, end_time - start_time


def get_alphabet():
    alphabets = read_file()
    choice = -1
    while choice < 0 or choice >= len(alphabets):
        print("please choose which alphabet you want to practice:")
        for i in range(len(alphabets)):
            print(f"{i} : {alphabets[i][0].removesuffix('.txt')}")
        try:
            choice = int(input(""))
        except TypeError: 
            pass
    return read_file(alphabets[choice][0], {}), alphabets[choice][1]


def evaluation(score, wrong, practice_time, leaderboard_file):
    print("\nPractice Completed!")
    print(f"You scored: {score} / {len(alphabet)}, which is {score / len(alphabet) * 100}% accuracy.")
    if len(wrong) > 0:
        print("Here is a list of all mistakes:")
        for key in wrong.keys():
            print(f"{key} : correct: {alphabet[key]} your guess: {wrong[key]}")
    else:
        print(f"Your time was {practice_time} seconds.")

        scores = []
        try:
            with open(leaderboard_file, "r") as leaderboard:
                for line in leaderboard:
                    if line != "\n":
                        score, name = line.rstrip("\n").split("|", 1)
                        scores.append((float(score), name))
        except FileNotFoundError:
            pass

        index = 0
        while index < len(scores) and scores[index][0] < practice_time:
            index += 1

        if index < 10:
            print(f"\nYour attempt made it on the leaderboard! Your rank is {index + 1}!")
            name = input("Please enter your name or leave it blank for anonymous: ")
            if name == "":
                name = "anonymous"
            scores.insert(index, (practice_time, name))
        else:
            print("\nTry again to beat the top 10!")

        print("\nLeaderboard:")
        for i, score in enumerate(scores[:10], start=1):
            print(f"{i}: {score[0]} seconds by {score[1]}")

        with open(leaderboard_file, "w") as leaderboard:
            for score in scores[:10]:
                leaderboard.write(f"{score[0]}|{score[1]}\n")


alphabet, leaderboard_file = get_alphabet()
score, wrong, practice_time = practice(alphabet=alphabet)
evaluation(score=score, wrong=wrong, practice_time=practice_time, leaderboard_file=leaderboard_file)
