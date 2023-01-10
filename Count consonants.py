def consonant_count(s):
    vowels = 'aeiou'
    validchars = 'bcdfghjklmnpqrstvwxyz'
    counter = 0
    answer = []
    sList = list(s.lower())
    for char in sList:
        if char not in vowels:
            if char in validchars:
                counter+=1
    return counter
