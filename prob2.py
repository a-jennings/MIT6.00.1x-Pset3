secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
test = ['x','y']



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    word = []
    result = []
    under = '_ '
    #converts secretWord into list of individual characters
    for char in secretWord:
        word.append(char)

    
    for x in word:
        if x in lettersGuessed:
            result.append(x)
        elif x not in lettersGuessed:
            result.append(under)
    return ''.join(result)


print(getGuessedWord(secretWord, test))

