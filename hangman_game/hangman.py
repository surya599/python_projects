import random
import hangman_words
from hangman_art import stages
from hangman_art import logo

correctletters = []
lives = 7
print(logo)


choosen_word = random.choice(hangman_words.word_list)

length = len(choosen_word)
placeholder = ""
while length > 0:
    placeholder  = placeholder+ "_ "
    length = length-1 
print(placeholder)

gameover = False
while not gameover :
    print(f"*********************************you have {lives} left************************************")
    guess = input("guess a letter : ").lower()
    if guess in correctletters:
        print(f"you've already guessed  {guess}")

    display = ""
    for letter in choosen_word:
        if letter == guess:
            display = display + letter
            correctletters.append(guess)
        elif letter in correctletters:
            display += letter
        else:
            display = display + ' _ '
    if guess not in choosen_word:
        lives = lives-1
        print(f"you've guessed {guess} that's not in the word you lost a life")
        if lives == 0:
            gameover = True
            print(f"*****************************it was {choosen_word} You Loose******************************************")
    
    print(display)
    if "_" not in display:
        gameover = True
        print("***********************************You Win*******************************************")
    print(stages[lives])

