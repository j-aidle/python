number_names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
"Eight", "Nine"]

dict_string = {
"A":"Alpha", "B":"Bravo", "C": "Charlie", "D":"Delta", "E":"Echo",
"F":"Foxtrot", "G":"Golf", "H":"Hotel", "I":"India", "J":"Juliett", "K":"Kilo",
"L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", "Q":"Quebec",
"R":"Romeo", " S":"Sierra", "T":"Tango", "U":"Uniform", "V":"Victor",
"W":"Whiskey", "X":"X-ray", "Y":"Yankee", "Z":"Zulu",
".": "Decimal",
}

character_list = []
while True:
    input_data = input()
    if input_data == "#":
        break
    for s in input_data.split():
        found = False
        for key in dict_string.keys():
            if dict_string[key] == s:
                for k in list(s):
                    character_list.append(k)
                    found = True
        if found: character_list.append(" ")
        if not found:
            for i in list(s):
                from_key = False
                if i.isdigit():
                    character_list.append(number_names[int(i)])
                    from_key = True
                elif i in dict_string.keys():
                    character_list.append(dict_string[i])
                    from_key = True
                else:
                    character_list.append(i)
                if character_list != [] and from_key:
                    c = character_list.pop()
                    character_list.append(c)
                    if c != " ":
                        character_list.append(" ")
            c = character_list.pop()
            character_list.append(c)
            if c != " ":
                character_list.append(" ")
    character_list.append('\n')
limit = len(character_list)
iteration = 1
concat = ""
for i in character_list:
    if i != '\n':
        concat = concat + i
    else:
        print(concat)
        concat = ""     

