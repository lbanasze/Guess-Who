# CS 205 Final: Guess Who
### Laura Banaszewski, Scotti Day, James Putnam

### NOTE: Original project used GitLab

## Late Work Changes

While implementing states into our program for our GUI, we ran into a bug that we were unable to fix by 11:59pm on May 2nd. Ultimately, we found that the issue was how the user input was handled in the GUI, as it was not being properly stored and sent into the function that handles user answers. Because of this, records were being wrongly deleted from the table and causing the program to crash when it found that the table it was using was empty. To fix this, we made two changes:

1. Set game state to GAME_OVER when the table is empty and display an error message. This also accounts for if the user answers questions untruthfully and the computer is unable to locate a professor that has all of the features communicated.

2. Introduct a new variable called "answer" that stores the user input immediately after a question has been asked. This prevents input that does not correspond with the question from being sent into the function that handles user answers to computer questions.

## Overview
Our team decided that the game we are most interested in replicating is Guess Who. Guess Who
is a game in which two players have a set of character cards. Each user is assigned a character present in
the other user’s character set. The objective of the game is to figure out what character has been assigned
to the opposing user. We determined that Python is the language we are most comfortable with using, as
the sqlite3 and pygame modules would be very beneficial towards achieving our vision for the game.

To add a creative spin to Guess Who, we decided to use a professor character set. We will include features that are not physical, such as the courses taught and department. The student set, on the other hand, will account for solely physical characteristics. The
professor set requires background knowledge on the characters for the most efficient gameplay, so the
user will have access to the table entry for their assigned character.

## CLI Version
CLI_main is a command line version that does not have an interactive board. Instead, the user is provided with an image containing the board. 

NOTE: Please open the image from this repo independent of the program. We began to write the code to have it open itself, but assembling proved to be complicated and we ran out of time.

Using the image of the board provided, the user will select a professor to be their character. To make a selection, they will type out the full name of the professor into the command line. 

## GUI Version

GUI_main is the version of the game that uses a GUI rather than a CLI. This implementation is more elaborate, as it has a start menu and an interactive board.

This version also includes the use of some special key presses. the key bindings are as follows:
 * [,] to decrease the volume
 * [.] to increase the volume
 * [;] to mute the volume
 * [ESC] to return to the main menu and reset the game

Due to issues with pygame, flipping a card over may not work on some versions of MacOS.

## Testing Instructions

After selecting your character, you will ask the computer a yes or no question regarding their character. You may ask about the following characteristics:

- **Department:** You can ask whether the computer's character works in the following departments:
    - Computer Science
    - Mathematics
    - Statistics
    - Dean
    - Asst. Dean

- **Location:** You can ask whether the computer's character in at the following locations:
    - School bus ball
    - Catamount statue
    - 95 million dollar sports arena
    - Delehanty hall

- **Glasses:** You can ask if the computer's character is wearing glasses

- **Hair Color:** You can ask if the computer's character has the following hair color:
    - Black
    - Grey
    - Brown
    - Blonde

- **Hat:** You can ask whether the computer's character is wearing a hat

- **Sex:** You can ask whether the computer's character is male or female

- **Facial Hair:** You can ask whether the computer's character has facial hair





