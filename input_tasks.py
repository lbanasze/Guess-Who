def parser(query):
    # call get_data to populate lists
    professor_list, department_list, location_list, glasses_list, hair_color_list, hat_list, sex_list, facial_hair_list = get_data_lists('options')
    query = query.strip("?")
    query_lower = query.lower()

    if query_lower == "quit":
        try:
            # need to close connection
            pass
        except:
            return query

    # Check to see if query contains a professors name, this would be the equivalent of the user 
    # guessing the computer's professor
    for professor in professor_list:
        if professor in query_lower:
            # check to see if correct professor
            trait = 'professor'
            value = professor
            return trait, value, query

    # Check to see if user asked about a specific department
    for department in department_list:
        if department in query_lower:
            # check to see if correct department 
            trait = 'department'
            value = department
            return trait, value, query

    # Check to see if user asked about a specific location
    for location in location_list:
        if location in query_lower:
            # Check to see if correct location
            trait = 'location'
            value = location
            return trait, value, query
        elif 'ball' in query_lower or 'bus' in query_lower:
            trait = 'location'
            value = 'school bus ball'
            return trait, value, query
        elif 'stadium' in query_lower or 'arena' in query_lower or 'sports' in query_lower:
            trait = 'location'
            value = '95 million dollar sports arena'
            return trait, value, query

    # Check to see if user asked about glasses
    if 'glass' in query_lower or 'glasses' in query_lower:
        trait = 'glasses'
        value = 'yes'
        return trait, value, query

    # Check to see if user asked about hair color
    for color in hair_color_list:
        if color in query_lower:
            # Check to see if correct hair color
            trait = 'hair_color'
            value = color
            return trait, value, query

    # Check to see if user asked about a hat
    if ' hat'in query_lower or query_lower == 'hat':
        trait = 'hat'
        value = 'yes'
        return trait, value, query

    for q in query_lower.split(' '):
        print(q)
        if q == 'man' or q == 'male':
            trait = 'sex'
            value = 'male'
            return trait, value, query
        elif q == 'female' or q == 'woman':
            trait = 'sex'
            value = 'female'
            return trait, value, query

    """
    # Check to see if user asked about sex
    for sex in sex_list:
        if sex in query_lower:
            # Check to see if correct sex
            trait = 'sex'
            value = sex
            return trait, value, query
        if 'man' in query_lower:
            trait = 'sex'
            value = 'male'
            return trait, value, query
        if 'woman' in query_lower:
            trait = 'sex'
            value = 'female'
            return trait, value, query
            
    """
     
    # Check to see if user asked about facial hair
    if 'facial' in query_lower:
        trait = "facial_hair"
        value = 'yes'
        return trait, value, query

    return False


def get_data_lists(conditional):

    # Open up csv containing Guess Who Data
    try:
        guess_who_data = open('GuessWhoData.csv', 'r')
    except IOError:
        print("Error loading Data")
    else:
        # Create Lists for each category
        professor_list = []
        department_list = []
        location_list = []
        glasses_list = []
        hair_color_list = []
        hat_list = []
        sex_list = []
        facial_hair_list = []

        # create an index
        i = 0

        # create a list to hold data for each line
        data = []
        char_list = []
        
        for line in guess_who_data:
            # split the line by comma and set data equal to
            data = line.split(',')
            
            # using the index to ignore the headers
            if i > 0:
                # if name is not contained in professor list, add it
                if data[1] not in professor_list: 
                    professor_list.append(data[1].lower())

                # if department is not contained in department list, add it    
                if data[2] not in department_list:
                    department_list.append(data[2].lower())

                # if location is not contained in location list, add it    
                if data[4] not in location_list:
                    location_list.append(data[4].lower())

                # if glasses not in glasses list, add it
                if data[5] not in glasses_list:
                    glasses_list.append(data[5].lower())

                # if hair color is not contained in hair color list, add it    
                if data[6] not in hair_color_list:
                    hair_color_list.append(data[6].lower())

                # if hat not in hat list, add it
                if data[7] not in hat_list:
                    hat_list.append(data[7].lower())

                # if sex is not contained in sex list, add it    
                if data[8] not in sex_list:
                    sex_list.append(data[8].lower())

                # if facial hair not in facial hair list, add it
                if data[9] not in facial_hair_list:
                    facial_hair_list.append(data[9].lower())

                # create new entry into the character list
                last_value = data[9].rstrip()
                new_entry = {"professor": data[1],
                                          "department": data[2],
                                          "location": data[4],
                                          "glasses": data[5],
                                          "hair_color": data[6],
                                          "hat": data[7],
                                          "sex": data[8],
                                          "facial_hair": last_value}


            # if header, increment index
            else:
                i += 1





        # close guess who data
        guess_who_data.close()

        if conditional == 'options':
            # return the lists back to parser
            return professor_list, department_list, location_list, glasses_list, hair_color_list, hat_list, sex_list, facial_hair_list
        if conditional == 'dictionary':
            return professor_list
