
def count_letters(word):
    word = word.upper()
    dictionary = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    
    for letter in word:
        if letter not in dictionary and letter in alphabet:
            dictionary[letter] = 1
        elif letter in alphabet and letter in dictionary:
            dictionary[letter] += 1
    return dictionary

print(count_letters('sSUOPERrcalafragili555555555sticexpealidoshus'))
