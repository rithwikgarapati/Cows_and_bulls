import random
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.


def cows_and_bulls(actual_num, user_input):
    cows = 0
    empty_list = [0] * 10
    nums = 0

    if len(user_input) == 4:
        for i in range(len(user_input)):

            if user_input[i] == actual_num[i]:
                cows += 1
            else:
                empty_list[int(actual_num[i])] += 1
                empty_list[int(user_input[i])] -= 1

        for i in empty_list:
            if i > 0:
                nums += i
        return f"Cows: {cows}, Bulls: {(len(actual_num) - cows - nums)} "
    else:
        return "Please Enter a Valid 4 digit number."


num = str(random.randint(1000, 9999))
x = 1
guess_count = 0

while x > 0:

    input1 = input("Enter a 4 digit number: ")

    if len(input1) == 4 and input1 == num:
        guess_count += 1
        print(f"Hurray you guessed it right in {guess_count} guesses.")
        x = 0
    else:
        print(cows_and_bulls(num, input1))
        guess_count += 1

with open('Cows and Bulls Scores.txt', 'a') as scores:
    scores.write(f"You guessed it in {guess_count} guesses \n")
    scores.close()

print("Game Over.")
