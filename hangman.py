import random
#三个单引号为多行文本
HANGMANPICS = ['''
+---+
|   |
    |
    |
    |
    |
========''', '''
 +---+
 |   |
 O   |
 |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ada ruby python java groovy elixir basic sharp swift rails'.split()

def getRandomWord(wordlist):

    wordIndex = random.randint(0, len(words)-1)
    return wordlist[wordIndex]
#missedLetters:猜错的字母 secretWord：正确的单词 correctLetters:猜中的单词
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):

    print(HANGMANPICS[len(missedLetters)])
    print()
    print("Missed letters:")
    tmp = ''
    for letters in missedLetters:
        tmp = tmp + letters + ' '
    print(tmp + "test")
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[1+i:]
    # tmp = ''
    # for letters in blanks:
    #     tmp = tmp + letters + ' '
    print(' '.join(blanks))
    # print(tmp + "test")
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter:')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    #print(guess)
    print("missedLetters:" + missedLetters)
    print("correctLetters:" + correctLetters)
    print("secretWord:" + secretWord)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +
                str(len(missedLetters)) + ' missed guesses and ' + str(len (correctLetters)) +
                  ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            print('H A N G M A N')
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
