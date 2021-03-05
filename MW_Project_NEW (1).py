from random import shuffle
from random import randint

def main():

    

    wordlist = []
    scrambledword = []
    guessedword = []
    letter = 0
    newletter = ""
    guesses = 0
    gameover = False

    

    file = open("wordlist.txt")

    
    
    line = file.readline()

    while len(line) > 0:
        
        line = line.strip()
        wordlist.append(line)
        line = file.readline()

    

    file.close()

    
        
    word = getNextWord(wordlist)

    
    
    scrambledword = scrambleWord(word)

    

    print("Welcome to CRYPTO-LOGIC!\nTry to guess the scrambled word, one letter at a time!")

    

    while (not gameover):

        

        print("\nIncorrect Guesses: " + str(guesses))

        

        printWord(scrambledword)
        printWord(guessedword)

        

        newletter = input("Your Guess? ").lower()

        if ( word[letter] == newletter ):

            

            guessedword.append(newletter)
            letter += 1

        else:

            

            guesses += 1

        

        if ( len(guessedword) == len(word) ):

            gameover = True

    

    printWord(guessedword)

    print("\nCongratulations!  You guessed the word after only " + str(guesses) + " incorrect guess(es)!")

    

    input("Press ENTER to exit: ")

def getNextWord (wordlist) :







    return list ( wordlist.pop ( randint(1,len(wordlist)) - 1 ))

def scrambleWord (word) :






    shuffledword = list(word)
    shuffle (shuffledword)
    return shuffledword

def printWord (word) :









    print( "".join(word).upper() )
main()


