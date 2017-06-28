import string
import random
WORDLIST_FILENAME = "words.txt"

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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for char in secretWord:
        if char in lettersGuessed:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

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


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

#ABOVE IS PREVIOUSLY WRITTEN CODE PROB 1 - 3 AND HELPER CODE GIVEN FROM PS3_HANGMAN

wordlist = loadWords()

def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' +str(len(secretWord)) + ' letters long.')
    
    game_over = True

   

        #Game text
    guesses = 8
    lettersGuessed = []
    while game_over:
        print('______________')
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
        letter = input('Please guess a letter: ')

        #Logic

        lettersGuessed.append(letter)
        
        if guesses > 0:
            if isWordGuessed(secretWord, lettersGuessed):
                print('Congratulations you won!')

            else:
                if letter in secretWord:
                    print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                else:
                    print('Oops! That letter is not in my word: '+ str(getGuessedWord(secretWord, lettersGuessed)))
                    guesses -=1

                


        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was ' + str(secretWord))
            game_over = False

        














# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)





