'''Simple CLI Worlde Clone. For project-based learning purposes.'''

from random import choice
import sys

TURNS = 5
CORRECT_LETTER_POSITION = '\33[102m'
CORRECT_POSITION = '\33[103m'
WRONG = '\33[101m'
END = '\x1b[0m'
WORD_LENGTH = 5

def get_word_list():
    '''Gets the all possible five-letter words for the game's answer.
    Word list taken from:
    https://github.com/powerlanguage/word-lists (1000 most common English words),
    then I filtered all the 5-letter words into words/words.txt'''

    with open('words/words.txt', 'r', encoding='utf-8') as words:
        from_file = words.read()
    words_list = from_file.split("\n")

    return words_list

def get_random_word(word_list):
    correct_word = choice(word_list)

    return correct_word
            
def get_hint(answer, guess):
    correct_answer_list = answer
    guess_list = guess
    hint = ''
            
    for i in range(WORD_LENGTH):
        if correct_answer_list[i] == guess_list[i]:
            #green
            hint += f'{CORRECT_LETTER_POSITION} {guess_list[i]} {END}'
        elif correct_answer_list[i] != guess_list[i] and guess_list[i] in correct_answer_list:
            #yellow
            hint += f'{CORRECT_POSITION} {guess_list[i]} {END}'
        else:
            #red
            hint += f'{WRONG} {guess_list[i]} {END}'

    return hint

def start_game():
    word_list = get_word_list()
    goal = get_random_word(word_list)

    for _ in range(TURNS):
        guess = input("Input your five-letter guess separated by spaces: ")
        hint = get_hint(goal, guess)
        print(hint)

def start_menu():
    print("Welcome to my simple CLI Wordle Clone!")
            
    menu = {
        '1': 'Start Game',
        '2': 'Exit'
    }

    while True:
        print("-----------------------------")
        for number, option in menu.items():
            print(f"{number}\t{option}")
        user_choice = input("Enter your choice: ")
        if user_choice not in menu:
            print("Invalid Input")
            continue
        break
            
    if user_choice == '1':
        start_game()
    if user_choice == '2':
        sys.exit()

def main():
    start_menu()


if __name__ == '__main__':
    main()
