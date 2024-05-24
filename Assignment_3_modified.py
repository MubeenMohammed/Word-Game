def is_outside_list(letter_list,integer):
    if integer > -len(letter_list) and integer < len(letter_list):
        return False
    else:
        return True
def letter_positions(letter_list,character):
    char_index = []
    for i in range (len(letter_list)):
        if character == letter_list[i]:
            char_index.append(i)
    return char_index
def valid_word_pos_direction(letter_list,word,index,direction):
    n = 0
    if direction == 1:
        if is_outside_list(letter_list,index+len(word)) == False:
            for i in range (index,index+len(word),direction):
                if letter_list[i] != word[n]:
                    return False
                n = n + 1
            return True
        else:
            return False
    if direction == -1:
        if is_outside_list(letter_list,len(word)) == False:
            for i in range (index,index-len(word),direction):
                if letter_list[i] != word[n]:
                    return False
                n = n + 1
            return True
        else:
            return False
def direction_word_given_position(letter_list,word,index):
    direction = []
    if valid_word_pos_direction(letter_list,word,index,-1) == True:
        direction.append(-1)
    if valid_word_pos_direction(letter_list,word,index,1) == True:
        direction.append(1)
    return direction
def position_direction_word(letter_list,word):
    dictonary = {}
    positions = letter_positions(letter_list,word[0])
    for element in positions:
        dictonary[element] = direction_word_given_position(letter_list,word,element)
    return dictonary
def cross_word_position_direction(letter_list,word,index,direction):
    if direction == 1:
        for i in range(index,index+len(word),direction):
            letter_list[i] = '*'
    if direction == -1:
        for i in range(index,index-len(word),direction):
            letter_list[i] = '*'
def cross_word_all_position_direction(letter_list,word,dict_position_direction):
    for key in dict_position_direction:
        directions = dict_position_direction[key]
        for i in range(len(directions)):
            cross_word_position_direction(letter_list,word,key,dict_position_direction[key][i])
def find_magic_word(letter_list):
    new_letter_list = []
    for i in letter_list:
        if i != '*' :
            new_letter_list.append(i)
    word = ''.join(new_letter_list)
    return word
def word_search(letter_list,word_list):
    new_list = []
    for element in word_list:
        word_position = position_direction_word(letter_list,element)
        cross_word_all_position_direction(letter_list,element,word_position)
    new_list = find_magic_word(letter_list)
    word = ''.join(new_list)
    return word
def word_search_main(filepath):
    file_list = []
    letter_list = []
    word_list = []
    file = open(filepath,'r')
    for line in file:
        file_list.append(line)
    first_line = file_list[0]
    for char in first_line:
        char.capitalize()
        letter_list.append(char)
    letter_list.remove('\n')
    for word in file_list[1:]:
        word.strip()
        word.upper()
        word_list.append(word)
    return letter_list
print(word_search_main('word_search_text.txt'))


