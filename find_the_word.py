import random
# Write your code here
languages = ['python', 'java', 'kotlin', 'javascript']
answer_word = random.choice(languages)
missing_words_length = len(answer_word) - 3
missing_words =  missing_words_length * "-"
words_help = answer_word[0] + answer_word[1] + answer_word[2] + missing_words
attempts = 8

print("H A N G M A N")    
print("Guess the word {}: >".format(words_help))

word = input()

if(word == answer_word):
    print("You survived!")
else:
    print("You lost!")