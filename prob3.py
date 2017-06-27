import string

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alph = list(string.ascii_lowercase)
    for x in lettersGuessed:
        if x in alph:
            alph.remove(x)
    return ''.join(alph)

print(getAvailableLetters(lettersGuessed))
