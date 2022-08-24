import random

#variables
Letters = 'abcdefghijklmnopqrstuvwxyz'
UpperLetters = Letters.upper()
Numbers = '0123456789'
Symbols = '!@#$%^&*)?'

with open('word_list') as word_file:
    english_words = (word_file.read().split())

#Random word selection from file

def wordIndex():
#    with open('word_list') as word_file:
#        english_words = (word_file.read().split())
        word_index = random.randint(0, len(english_words))

        return word_index

def wordSelect():
#    with open('word_list') as word_file:
#        english_words = (word_file.read().split())
#        word_index = random.randint(0, len(english_words))
    word_select = english_words[wordIndex()]
    if len(word_select)-3 >= PassLength:
        wordIndex()
    else:
        print(word_select)
        print("""""""""""""""""")
    return word_select





#Replacing certain letters with Symbols
def processString(word):
  dictionary = {'a': '@', 'A': '@', 'e': '3', 'E': '3'}
  transTable = word.maketrans(dictionary)
  Utxt = word.translate(transTable)

  return Utxt








#input password length
PassLength = int(input("Enter your password length: "))

#combo = Letters + UpperLetters + Numbers + Symbols
combo2 = Numbers + Symbols



#GENERATED_PASSWORD = "".join(random.sample(combo, PassLength))


GENERATED_PASSWORD = processString(wordSelect()) + "".join(random.sample(combo2, 3))

#print(processString(wordSelect()))
print(GENERATED_PASSWORD)