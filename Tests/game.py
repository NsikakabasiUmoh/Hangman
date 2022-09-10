chosen_word = 'wood'

display = list(len(chosen_word)*'-')
print(display)

if 'w' in chosen_word:
    display[chosen_word.index('w')] = 'w'
    print(display)
