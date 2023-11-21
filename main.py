import random

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
code_length = 4
max_attempts = 10

code = random.choices(colors, k=code_length)
attempts = 0

print(f"Avaiable colors: {','.join(colors)}")
print(f"Code length: {code_length}, Max attempts: {max_attempts}")

while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ").strip().split()

    if len(guess)!= code_length or not all(color in colors for color in guess):
        print("Invalid guess. Make sure you use only four colors.")
        continue

    correct_position = sum(g == c for g, c in zip(guess, code))
    correct_color = sum(min(guess.count(c), code.count(c)) for c in set(code))
    correct_color -= correct_position

    print(f"{correct_position} colors placed correctly")
    print(f"{correct_color} correct colors placed in the wrong positions")

    if correct_position == code_length:
        print("You won")
        exit()

    attempts += 1

print("You lost") 

