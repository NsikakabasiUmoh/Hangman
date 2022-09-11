chosen_word = 'wood'

guess = input('Guess an alphabet: ')  # problem that can happen, two alphabets or a digit inputted

# Validation
if len(guess) > 1 or guess.isdigit():  # this will solve the above issues
    exit()

if guess not in chosen_word:
    exit()

# Assigning & Changing
guess_index = [index for index, alphabet in enumerate(chosen_word) if alphabet is guess]

placeholder = list(len(chosen_word)*'-')  # Placeholder variable

for i in guess_index:
    placeholder[i] = guess

print(*placeholder, sep=', ')
