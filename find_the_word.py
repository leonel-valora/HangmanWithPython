import random
# Write your code here
languages = ['python', 'java', 'kotlin', 'javascript']
answer_word = random.choice(languages)
missing_words = len(answer_word) * "-"
words = list(missing_words)
chars_answer = list(answer_word)

print("H A N G M A N")
print()

for _ in range(8):
    print("".join(words))
    char = input("Input a letter: ")
    if char in answer_word:
        words_repeated = words.count(char)
        for _ in range(words_repeated):
            index = chars_answer.index(char)
            words[index] = char;
            if(words_repeated > 1):
                chars_answer[index] = "-"
                
    else:
        print("That letter doesn't appear in the word")
    print()

print("Thanks for playing!")
print("We'll see how well you did in the next stage")