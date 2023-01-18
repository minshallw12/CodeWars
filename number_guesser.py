def number_guess(num):
    guesses = 0
    guess = input('What is your guess')
    the_integer = int(guess)
    while the_integer != num:
        guesses += 1
        if the_integer > num:
            guess = input('Too high. Guess again ')
        elif the_integer < num:
            guess = input('Too low. Guess again ')
        else:
            return "It took you " + guesses + " guesses"

print(number_guess(50))