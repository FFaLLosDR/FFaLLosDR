# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    temp=list(secretWord)
    tempguess=lettersGuessed[:]
    count=0
    
    for i in range(len(temp)):
        if temp[i] in tempguess:
            count+=1
        else:
            return False
    
    if count==len(temp):
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
    tempguessed=lettersGuessed[:]
    tempword=list(secretWord)
    ans=str()
    
    for i in range(len(tempword)):
        if tempword[i] in tempguessed:
            ans+=tempword[i]
        else:
            ans+=" _ "
    
    return ans



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    avail=list(string.ascii_lowercase)
    tempavail=lettersGuessed[:]
    
    for i in range(len(tempavail)):
        if tempavail[i] in avail:
            avail.remove(tempavail[i])
    
    avail2=''.join(avail)
    return avail2
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    numchar=len(secretWord)
    print('I am thinking of a word that is ',numchar,'letters long.')
    
    count=8
    lettersGuessed=list()
    print('-------------')
    
    while count>0:    
        print('You have ',count,' guesses left')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        tempinput=input('Please guess a letter : ')
        
        if tempinput in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord,lettersGuessed))
            print('-------------')
        
        else:
            lettersGuessed.append(tempinput)
            
            if tempinput in secretWord:
                print('Good Guess : ', getGuessedWord(secretWord,lettersGuessed))
                print('-------------')
                
                if isWordGuessed(secretWord,lettersGuessed):
                    return print('Congratulations, you won!')
    
            else:
                print('Oops! That letter is not in my word: ', getGuessedWord(secretWord,lettersGuessed))
                count-=1
                print('-------------')

    print("Sorry, you ran out of guesses. The word was ", secretWord)
    


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
