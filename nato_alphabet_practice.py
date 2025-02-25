import random
import time

nato_alphabet = {"A" : "alfa", 
    "B" : "bravo", 
    "C" : "charlie", 
    "D" : "delta", 
    "E" : "echo", 
    "F" : "foxtrot", 
    "G" : "golf", 
    "H" : "hotel", 
    "I" : "india", 
    "J" : "juliett", 
    "K" : "kilo", 
    "L" : "lima", 
    "M" : "mike", 
    "N" : "november", 
    "O" : "oscar", 
    "P" : "papa", 
    "Q" : "quebec", 
    "R" : "romeo", 
    "S" : "sierra", 
    "T" : "tango", 
    "U" : "uniform", 
    "V" : "victor", 
    "W" : "whiskey", 
    "X" : "xray", 
    "Y" : "yankee", 
    "Z" : "zulu"}

score = 0
wrong = {}

start_time = time.time()
for key in random.sample(list(nato_alphabet.keys()), len(nato_alphabet)):
    guess = input(f"{key} : ").strip().lower()
    if guess == nato_alphabet[key]:
        score += 1
    else:
        wrong[key] = guess
end_time = time.time()

practice_time = end_time - start_time

print("\nPractice Completed!")
print(f"You scored: {score} / {len(nato_alphabet)}, which is {score / len(nato_alphabet) * 100}% accuracy.")
if len(wrong) > 0:
    print("Here is a list of all mistakes:")
    for key in wrong.keys():
        print(f"{key} : correct: {nato_alphabet[key]} your guess: {wrong[key]}")
else:
    print(f"Your time was {practice_time} seconds.")

    leaderboard_file = "nato_alphabet_leaderboard.txt"
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