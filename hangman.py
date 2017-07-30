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
    wordIndex = random.randint(0,len(words)-1)
    return wordlist[wordIndex]

print (getRandomWord())
