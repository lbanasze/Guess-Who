from computer_tasks import find_question, create_statement, get_data, create_question, interpret_answer, answer_user
from load import initialize_db
from input_tasks import get_data_lists, parser
import random
import pygame
import time
import sys

# Global variables

# Databases 
TABLE1 = "professor_table"
TABLE2 = "computer_table"
DB = "data.db"
columns = ["department", "location", "glasses", "hair_color", "hat", "sex", "facial_hair"]

# Computer information
COMPUTER_CHARACTER = ""
prof = []

# Display information
user_character = [()]
user_character_display = False

# GUI Turns
PLAYER_TURN, AI_TURN, CLICK_CONT, INTRO, GAME_OVER, CHAR_DETAILS = 0, 1, 2, 3, 4, 5
global state
state = PLAYER_TURN


def initialize_game():
    global COMPUTER_CHARACTER

    char_list = get_data_lists("dictionary")
    # Randomly choose a character
    rand = random.randint(0, len(char_list) - 1)
    COMPUTER_CHARACTER = char_list[rand]
    # Initialize database
    initialize_db()
    return COMPUTER_CHARACTER


def computer_turn(answer, field, value):
    global guess_text
    global state
    global prof

    if field == 'professor':
        if answer:
            guess_text = "Computer has won!"

            state = GAME_OVER
            return True
        else:
            guess_text = "Whoops, looks like you answered a question wrong."
            state = GAME_OVER
            return False

    # print(field)
    # print(value)
    # print(answer)
    prof = interpret_answer(answer, TABLE1, TABLE2, field, value, DB)
    print(prof)

    if len(prof) == 0:
        state = GAME_OVER
        guess_text = "Whoops, looks like you answered a question wrong."
        return True

    return False


def user_turn(query):
    global guess_text
    global state

    target, value, query = parser(query)
    print(target)
    print(value)
    print(query)

    if target == "professor":
        if value == COMPUTER_CHARACTER:
            guess_text = "You've guessed correctly!"
            return True
        else:
            guess_text = "You've guessed incorrectly."

        state = GAME_OVER

    else:
        answer = answer_user(target, value, TABLE1, COMPUTER_CHARACTER, DB)
        guess_text = answer
        return False


def main():
    pygame_main() #chunking in my main here


class card():
    def __init__(self, loc, size, color, surface, flipped, button):
        self.loc = loc
        self.size = size
        self.color = color
        self.surface = surface
        self.flipped = flipped
        self.button = button
    def draw(self):
        pygame.draw.rect(screen, (0,0,0), loc, size, 0)
    def overlap(self, pos):
        if (pos[0] > self.loc[0]) and (pos[0] < self.loc[0] + self.size[0]):
            if pos[1] > self.loc[1] and pos[1] < self.loc[1] + self.size[1]:
                return True
        return False



def pygame_main():

    # boilerplate pygame stuff
    pygame.init()
    screen_size = (1400, 800)
    screen = pygame.display.set_mode(screen_size)

    width = screen.get_width()
    height = screen.get_height()

    white = (255, 255, 255)
    red = (162, 34, 5)
    blue = (9, 3, 138)

    pygame.display.set_caption("Guess Who! UVM")
    clock = pygame.time.Clock()
    running = True

    bg = pygame.image.load('FullBoardFinal.png')
    bg = pygame.transform.scale(bg, (800,800))
    start_screen = pygame.image.load('TitleCard.png')
    start_screen = pygame.transform.scale(start_screen, (1400, 800))

    font = pygame.font.SysFont(pygame.font.get_fonts()[0], 24)
    prompt_font = pygame.font.SysFont(pygame.font.get_fonts()[0], 46)
    fontSmall = pygame.font.SysFont(pygame.font.get_fonts()[0], 14)

    pygame.mixer.music.load("gameMusocSMALL.wav")
    pygame.mixer.music.play(-1)

    # Buttons
    start_button = font.render("START GAME", True, white)
    quit_button = font.render("QUIT GAME", True, white)

    # Start menu
    start_menu = True
    while start_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                # quit button pressed
                if (width / 3) * 1.75 <= mouse[0] <= (width / 3) * 1.75 + 180 and (height / 5) * 4 <= mouse[1] <= (height / 5) * 4 + 40:
                    pygame.mixer.music.load("./sfx/evil.wav")
                    pygame.mixer.music.play(-1)
                    time.sleep(1)
                    pygame.quit()
                # quit button pressed
                if (width / 3) * 1.25 <= mouse[0] <= (width / 3) * 1.75 + 180 and (height / 5) * 4 <= mouse[1] <= (height / 5) * 4 + 40:
                    # some sort of help menu
                    pass
                # start button pressed
                if (width / 3) * .75 <= mouse[0] <= (width / 3) * .75 + 180 and (height / 5) * 4 <= mouse[1] <= (height / 5) * 4 + 40:
                    my_char = initialize_game()
                    pygame.mixer.music.load("./sfx/deedlee.wav")
                    pygame.mixer.music.play(-1)
                    time.sleep(.75)
                    pygame.mixer.music.load("gameMusocSMALL.wav")
                    pygame.mixer.music.play(-1)
                    start_menu = False

            # Volume control
            elif event.type == pygame.KEYDOWN:
                if event.key == ord('.'):
                    vol = pygame.mixer.music.get_volume()
                    if vol < 1:
                        pygame.mixer.music.set_volume(vol+0.1)
                elif event.key == ord(','):
                    vol = pygame.mixer.music.get_volume()
                    if vol >= 0:
                        pygame.mixer.music.set_volume(vol - 0.1)
                elif event.key == ord(';'):
                    pygame.mixer.music.set_volume(0)

        screen.fill(white)
        screen.blit(start_screen, (0, 0))

        mouse = pygame.mouse.get_pos()

        # start button

        if (width / 3) * .75 <= mouse[0] <= (width / 3) * .75 + 180 and (height / 5) * 4 <= mouse[1] <= (
                height / 5) * 4 + 40:
            pygame.draw.rect(screen, red, [(width / 3) * .75, (height / 5) * 4, 180, 40])
        else:
            pygame.draw.rect(screen, blue, [(width / 3) * .75, (height / 5) * 4, 180, 40])

        # help button

        if (width / 3) * 1.25 <= mouse[0] <= (width / 3) * 1.25 + 180 and (height / 5) * 4 <= mouse[1] <= (height / 5) * 4 + 40:
            pass
            #pygame.draw.rect(screen, blue, [(width / 3) * 1.25, (height / 5) * 4, 180, 40])
        else:
            pass
            #pygame.draw.rect(screen, red, [(width / 3) * 1.25, (height / 5) * 4, 180, 40])

        # quit button
        if (width / 3) * 1.75 <= mouse[0] <= (width / 3) * 1.75 + 180 and (height / 5) * 4 <= mouse[1] <= (height / 5) * 4 + 40:
            pygame.draw.rect(screen, red, [(width / 3) * 1.75, (height / 5) * 4, 180, 40])
        else:
            pygame.draw.rect(screen, blue, [(width / 3) * 1.75, (height / 5) * 4, 180, 40])

        screen.blit(start_button, ((width / 3) * .75 + 5, (height / 5) * 4 + 5))
        #screen.blit(help_button, ((width / 3) * 1.25 + 55, (height / 5) * 4 + 5))
        screen.blit(quit_button, ((width / 3) * 1.75 + 15, (height / 5) * 4 + 5))

        pygame.display.update()

    # Main game loop

    global question_field
    global question_value

    # boilerplate and functions for player/AI turns
    global state
    state = INTRO
    global guess_text
    global question_text
    guessed = False
    question_text = ""
    guess_text = ""
    result = None
    default_text = "TYPE HERE"
    default_img = font.render(default_text, True, (255,255,255))
    guess_img = font.render(guess_text, True, (255,255,255))
    global user_char_img0
    global user_char_img1
    user_char_img0 = font.render("", True, (255, 255, 255))
    user_char_img1 = font.render("", True, (255, 255, 255))


    #initialize
    # my_char = initialize_game()
    char_text = "opponent's char: " + COMPUTER_CHARACTER
    char_img = font.render(char_text, True, (255,255,255))
    professor_list, department_list, location_list, glasses_list, hair_color_list, hat_list, sex_list, facial_hair_list = get_data_lists("options")
    # choose_character(professor_list)


    # make prompt text
    prompt_text = "Example prompt text"
    prompt_img = font.render(prompt_text, True, (255,255,255))

    # make input text
    input_text = ""
    input_img = font.render(input_text, True, (255,255,255))

    # making card covers and all that
    card_covers = []
    for i in range(6):
        for j in range(4):
            card_size = (120, 185)
            card_loc = (i * 132 + 8, j * 195 + 10)
            card_color = (200, i*30, j*40, 0)
            s = pygame.Surface(card_size)
            c = card(card_loc, card_size, card_color, s, False, False)
            s.set_alpha(50)
            s.fill(card_color)
            card_covers.append(c)
            #screen.blit(s, card_loc)



    # main game loop
    while running:
        screen.fill([90, 90, 90])
        screen.blit(bg, (0, 0))
        for s in card_covers:
            if s.overlap(pygame.mouse.get_pos()) or s.flipped == True:
                s.surface.set_alpha(200)
            else:
                s.surface.set_alpha(0)
            screen.blit(s.surface, s.loc)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_exit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame_main()
                    pygame.quit()
                    sys.exit(-1)
                if event.key == pygame.K_BACKSPACE:
                    if len(input_text) > 0:
                        input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if state == PLAYER_TURN:
                        if parser(input_text) == False:
                            # need to prompt for good question
                            question_text = "Please enter a valid question. "
                            input_text = ""
                        else:
                            guessed = user_turn(input_text)
                            if guessed:
                                state = GAME_OVER
                                input_text = ""
                            else:
                                state = AI_TURN
                                input_text = ""

                                if len(prof) == 1:
                                    question = "Are you "
                                    question += prof[0][0]
                                    question += " ?"
                                    question_text = question
                                    question_field = "professor"
                                    question_value = prof[0][0]

                                else:
                                    question, field, value = find_question(columns, TABLE2, DB)
                                    question_field = field
                                    question_text = question
                                    question_value = value
                            
                    elif state == AI_TURN:
                        if input_text != 'y' and input_text != 'n':
                            input_text = ""
                            state = AI_TURN
                        else:
                            if input_text == 'y':
                                answer = True
                            else:
                                answer = False
                            guessed = computer_turn(answer, question_field, question_value)
                            if guessed:
                                state = GAME_OVER
                                input_text = ""
                            else:
                                question_text = "Ask a question"
                                state = PLAYER_TURN
                                input_text = ""
                                guess_text = ""

                    elif state == INTRO:
                        if input_text.lower() not in professor_list:
                            question_text = "Please enter a valid character."
                        else:
                            user_character = input_text.lower()
                            state = CHAR_DETAILS
                        input_text = ""
                    elif state == CHAR_DETAILS:
                        if input_text != 'y' and input_text != 'n':
                            question_text = " Please enter y or n. "
                            input_text = ""
                        else:
                            char = user_character
                            command = create_statement("*", TABLE1, "professor", char)
                            char_details = get_data(command, DB)[0]
                            global user_character_display
                            user_character_display = True
                            print(input_text)
                            if input_text == 'n':
                                user_character_display = False
                            question_text = "Ask a question"
                            state = PLAYER_TURN
                            char_detail_string1 = ""
                            char_detail_string0 = "Professor | department | college | loc | glasses | hair color | hat | sex | facial hair"
                            for x in range(1, len(char_details)):
                                char_detail_string1 = char_detail_string1 + char_details[x] + ", "
                            user_char_img0 = fontSmall.render(char_detail_string0, True, (255,255,255))
                            user_char_img1 = fontSmall.render(char_detail_string1, True, (255,255,255))
                            input_text = ""
                            guess_text = ""
                elif event.key == ord('.'):
                    vol = pygame.mixer.music.get_volume()
                    if vol < 1:
                        pygame.mixer.music.set_volume(vol+0.1)
                elif event.key == ord(','):
                    vol = pygame.mixer.music.get_volume()
                    if vol >= 0:
                        pygame.mixer.music.set_volume(vol-0.1)
                elif event.key == ord(';'):
                    pygame.mixer.music.set_volume(0)
                else:
                    if state != GAME_OVER:
                        input_text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                for s in card_covers:
                    if s.overlap(event.pos) and s.flipped == False:
                        s.flipped = True
                    elif s.overlap(event.pos) and s.flipped == True:
                        s.flipped = False
        if state == PLAYER_TURN:
            prompt_text = "  Your turn  "
        elif state == AI_TURN:
            prompt_text = "  AI turn  "
        elif state == CLICK_CONT:
            prompt_text = " Press enter to continue "
        elif state == INTRO:
            prompt_text = " Please pick a character. "
        elif state == CHAR_DETAILS:
            prompt_text = " Display character info (y/n)? "
        elif state == GAME_OVER:
            prompt_text = " Thanks for playing! "
            question_text = ""


        #for thread in threading.enumerate():
        #    print(thread.name)
        #print(state)
        #print(prompt_text)
        input_img = font.render(input_text, True, (255,255,255))
        prompt_img = prompt_font.render(prompt_text, True, (255,0,0), (255,255,255))
        question_img = font.render(question_text, True, (255,255,255))
        label_img = font.render("Computer response: ", True, (255,255,255))
        guess_img = font.render(guess_text, True, (255,255,255))
        
        if user_character_display == True:
            screen.blit(user_char_img0, (850, 740))
            screen.blit(user_char_img1, (850, 765))
        screen.blit(question_img, (850, 295))
        screen.blit(guess_img, (850, 495))
        screen.blit(prompt_img, (850, 200))
        screen.blit(label_img, (850, 450))
        if (input_text == ""):
            screen.blit(default_img, (850, 350))
        else:
            screen.blit(input_img, (850,350)) # for displaying your input text

        # screen.blit(char_img, (850, 700)) # for displaying who your prof is
        pygame.display.update()


        # update display
        clock.tick(30)
        pygame.display.flip()


main()
