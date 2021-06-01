import sqlite3

# Functions authored by Laura Banaszewski
# The following functions handle the computer player


# Function to determine best question to ask user
def find_question(columns, table, db):

    value = ""
    field = ""
    count = 0

    # Find the best question
    for col in columns:

        command = "SELECT "
        command += col
        command += ", COUNT("
        command += col
        command += ") AS `count`"
        command += " FROM "
        command += table
        command += " GROUP BY "
        command += col
        command += " ORDER BY `count` DESC LIMIT 1"
        data = get_data(command, db)

        if len(data) > 0:
            v = data[0][0]
            c = data[0][1]

            if c > count:
                count = c
                value = v
                field = col


    # update the table
    if value == 'yes' or value == 'no':
        command = "UPDATE "
        command += table
        command += " SET "
        command += field
        command += " = NULL"
        update_data(command, db)
    else:
        command = "UPDATE "
        command += table
        command += " SET "
        command += field
        command += " = NULL WHERE "
        command += field
        command += " = \""
        command += value
        command += "\""
        update_data(command, db)


    return create_question(field, value), field, value


# Function to create SQL statement
def create_statement(target, table, field, value):
    command = "SELECT "
    command += target
    command += " FROM "
    command += table
    command += " WHERE "
    command += field
    command += " = "
    command += "\""
    command += value
    command += "\""
    return command


# Function to run SQL statement
def get_data(command, db):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    try:
        c.execute(command)
        results = c.fetchall()

        if results == None:
            return "Invalid question"

        return results

    except BaseException as be:
        print(command)
        print(be)
        return be


def update_data(command, db):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    try:
        c.execute(command)
        conn.commit()
        return True

    except BaseException as be:
        print(command)
        print(be)
        return be


# Function to ask user a question
def create_question(field, value):
    # There are various types of questions
    binary = ["glasses", "hat", "facial_hair"]
    adj = ["hair_color"]

    if field == "location":
        return "Are you at the " + value + "? (y/n)"
    elif field == "department":
        return "Are you in the " + value + " department? (y/n)"
    elif field == "sex":
        return "Are you " + value + "? (y/n)"
    elif field in binary:
        if field == 'facial_hair':
            return "Do you have facial hair? (y/n)"
        elif field == 'hat':
            return "Do you have a hat? (y/n)"
        else:
            return "Do you have " + field + "? (y/n)"
    elif field in adj:
        return "Do you have " + value + " hair? (y/n)"
    elif field == "professor":
        return "Are you " + value + " ? (y/n)"

# Function to eliminate candidates based on user answer
def interpret_answer(answer, table1, table2, field, value, db):
    if field == "" or value == "":
        print("Field or value is empty.")
        return []

    # account for the fact there is only one form of binary question
    if value == 'no':
        value = 'yes'

    if answer:
        command = "UPDATE "
        command += table2
        command += " SET "
        command += field
        command += " = NULL "
        command += " WHERE "
        command += field
        command += " NOT LIKE \""
        command += value
        command += "\""
        update_data(command, db)

        # Get the character keys that the question applies to
        command = "SELECT professor FROM "
        command += table1
        command += " WHERE "
        command += field
        command += " NOT LIKE \""
        command += value
        command += "\""
        character_keys = get_data(command, db)

        # Remove them from the dict
        for key in character_keys:
            command = "DELETE FROM "
            command += table2
            command += " WHERE professor = \""
            command += key[0]
            command += "\""
            update_data(command, db)

    # If the user answered no, remove the candidates that are eliminated
    if not answer:
        command = "UPDATE "
        command += table2
        command += " SET "
        command += field
        command += " = NULL "
        command += " WHERE "
        command += field
        command += " = \""
        command += value
        command += "\""
        update_data(command, db)

        # Get the character keys that the question applies to
        command = create_statement("professor", table1, field, value)
        character_keys = get_data(command, db)

        # Remove them from the dict
        for key in character_keys:
            command = "DELETE FROM "
            command += table2
            command += " WHERE professor = \""
            command += key[0]
            command += "\""
            update_data(command, db)

    data = get_data("SELECT professor FROM " + table2, db)
    #if type(data) != list:
     #   return [data]
    return data

# Function to answer user question
def answer_user(target, value, table, character, db):
    command = create_statement(target, table, "professor", character)
    results = get_data(command, db)
    result = results[0][0]

    if result == value:
        return "Yes!"
    else:
        return "No."
