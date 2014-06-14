'''
Pig latin converter
@param word: the word to convert into pig latin
'''

def pig_latin(word):
    return word[1:] + word[0] + "ay"

while(1):
    word = raw_input("Enter a word to convert into Pig Latin! ")
    print pig_latin(word)
    print
    print
