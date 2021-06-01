from computer_tasks import find_question, create_statement, get_data, create_question, interpret_answer, answer_user
from load import initialize_db
from input_tasks import get_data_lists, parser
import random

# Global variables
TABLE1 = "professor_table"
TABLE2 = "computer_table"
DB = "data.db"
COMPUTER_CHARACTER = ""
user_character = [()]
user_character_display = False
columns = ["professor", "department", "location", "glasses", "hair_color", "hat", "sex", "facial_hair"]


def initialize_game():
    global COMPUTER_CHARACTER

    char_list = get_data_lists("dictionary")
    # Randomly choose a character
    rand = random.randint(0, len(char_list) - 1)
    COMPUTER_CHARACTER = char_list[rand]

    # Initialize database
    initialize_db()


def computer_turn():
    global user_character
    global user_character_display
    global char_list
    global columns

    if user_character_display:
        print(user_character)

    # Get the best question
    question, field, value = find_question(columns, TABLE2, DB)

    answer = input(question)
    while answer != 'y' and answer != 'n':
        answer = input(question)

    if answer == 'y':
        if field == "professor":
            return True
        answer = True

    else:
        answer = False

    interpret_answer(answer, TABLE1, TABLE2, field, value, DB)

    return False


def user_turn():
    query = input(">")
    get_question = parser(query)
    while get_question == False:
        print("Please enter a valid question")
        query = input(">")
        get_question = parser(query)

    target = get_question[0]
    value = get_question[1]

    if target == "professor":
        if value == COMPUTER_CHARACTER:
            print("Yes!")
            return True
        else:
            print("No.")
    else:
        answer = answer_user(target, value, TABLE1, COMPUTER_CHARACTER, DB)
        print(answer)
        return False


def print_menu():
    print("Welcome to Guess Who: UVM Professor Edition")
    print("In this game, you will play against the computer.")
    print("Your objective is to figure out what character the computer has.")
    print("The computer will try to figure out your character first.")


def choose_character(professor_list):
    global user_character
    global user_character_display

    char = input("Please choose a character:")
    while char not in professor_list:
        char = input("Please choose a valid character:")

    command = create_statement("*", TABLE1, "professor", char)
    user_character = get_data(command, DB)

    display = input("Would you like the information about your character to be displayed? (y/n)")
    while display != 'y' and display != 'n':
        display = input("Would you like the information about your character to be displayed? (y/n)")

    if display == 'y':
        user_character_display = True


def main():
    initialize_game()
    print_menu()
    professor_list, department_list, location_list, glasses_list, hair_color_list, hat_list, sex_list, facial_hair_list = get_data_lists("options")
    choose_character(professor_list)
    play = True

    while play:
        print("Your turn.")
        user_win = user_turn()
        if user_win:
            print("You won!")
            play = False
            break

        print("Computer's turn.")
        computer_win = computer_turn()
        if computer_win:
            print("You lost.")
            play = False

        if play == False:
            again = input("Play again? (y/n)")
            while again != "y" and again != "n":
                again = input("Play again? (y/n)")

            if input == "n":
                again = False


main()
