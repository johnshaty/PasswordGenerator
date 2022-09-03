import random

# variables

Letters = 'abcdefghijklmnopqrstuvwxyz'
UpperLetters = Letters.upper()
Numbers = '0123456789'
Symbols = '!@#$%^&*)?'
combo2 = Numbers + Symbols

# input password length

while True:
    try:
        PassLength = int(input("Enter your password length: \n"))
        break
    except:
        print("Error, please enter a valid number. ")

# reads word file in

with open('word_list') as word_file:
    english_words = (word_file.read().split())

# Random word selection from file

def wordIndex():
    word_index = random.randint(0, len(english_words))

    return word_index

def wordSelect():

    condition = False

# Evaluating if word fits user length requirements

    while condition == False:
        word_select = english_words[wordIndex()]

        if(len(word_select) != (PassLength - 3)):
            wordIndex()

            condition = False

# iterate for every new word that does not fit condition

        else:
            print(word_select)
            print("""""""""""""""""""")
            condition = True
            return word_select


# Replacing certain letters with Symbols

def processString(word):
    dictionary = {'a': '@', 'A': '@', 'e': '3', 'E': '3'}
    transTable = word.maketrans(dictionary)
    Utxt = word.translate(transTable)

    return Utxt


# final password generation

GENERATED_PASSWORD = processString(wordSelect()) + "".join(random.sample(combo2, 3))

print(GENERATED_PASSWORD)
print(len(GENERATED_PASSWORD))

