import random
# Write your code here
def showMenu():
    user_choice = input('Type "play" to play the game, "exit" to quit: ')
    while user_choice != "play" and user_choice != "exit":
        user_choice = input('Type "play" to play the game, "exit" to quit: ')
    return user_choice

def addCharactersIntoAnswer(answer_chars,char,missing_words):
    words_repeated = answer_chars.count(char)
    for _ in range(words_repeated):
        index = answer_chars.index(char)
        missing_words[index] = char;
        if(words_repeated > 1):
            answer_chars[index] = "-"

def startGame():
    #set variables
    languages = ['python', 'java', 'kotlin', 'javascript']
    answer = random.choice(languages)
    answer_chars = list(answer)
    missing_words = list(len(answer) * "-")
    introduced_chars = list()
    won = False
    attempts = 8
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # print welcome
    print("H A N G M A N")
    # read the input and check it
    while attempts > 0:
        print()
        print("".join(missing_words))
        char = input("Input a letter: ")
        if len(char) != 1:
            print("You should input a single letter")
        elif char not in abc:
            print("Please enter a lowercase English letter")
        elif char in introduced_chars:
            print("You've already guessed this letter")
        elif char in answer:
            addCharactersIntoAnswer(answer_chars,char,missing_words)
            introduced_chars.append(char)
        else:
            print("That letter doesn't appear in the word")
            introduced_chars.append(char)
            attempts -= 1
        if("".join(missing_words) == answer):
            won = True;
            break
    if won == True:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")
        
play_or_exit = showMenu()
while play_or_exit == "play":
    startGame()
    play_or_exit = showMenu()