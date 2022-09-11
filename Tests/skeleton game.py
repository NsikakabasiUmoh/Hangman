chosen_word = 'wood'

guess = input('Guess an alphabet: ')  # problem that can happen, two alphabets or a digit inputted

if len(guess) > 1 or guess.isdigit():  # this will solve the above issues
    exit()

if guess not in chosen_word:
    exit()

guess_index = [index for index, alphabet in enumerate(chosen_word) if alphabet is guess]

print(f'Continue. Index: {guess_index}')
