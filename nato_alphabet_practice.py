import random

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
wrong = []
for key in random.sample(list(nato_alphabet.keys()), len(nato_alphabet)):
    guess = input(f"{key} : ").strip().lower()
    if guess == nato_alphabet[key]:
        score += 1
    else:
        wrong.append(key)

print("\nPractice Completed!")
print(f"You scored: {score} / {len(nato_alphabet)}, which is {score / len(nato_alphabet) * 100}% accuracy.")
if len(wrong) > 0:
    print("Here is a list of all mistakes:")
    for key in wrong:
        print(f"{key} : {nato_alphabet[key]}")
    