def is_outside_list(letter_list,integer):
    '''
    (list,integer)-->(Boolean value)
    
    It will return boolean value checking if the index is out of the list
    or if it is negative.
    
    >>> is_outside_list(['G','S','J','D'],23)
    True
    >>> is_outside_list(['T','B','S','M'],0)
    False
    >>> is_outside_list(['A','B','C','D'],-2)
    True
    '''
    
#Even though in python we can access indices of negative values, this function
#also considers negative indices as outside of the list.

    if integer >= 0  and integer < len(letter_list):
        return False
    else:
        return True
  
    
def letter_positions(letter_list,character):
    '''
    (list,string)-->(list)
    
    returns the position of given character in the form of list by
    looking all over the given letter list.
    
    >>> letter_positions(['A','B','C','D','G','T','G'],'G')
    [4, 6]
    >>> letter_positions(['A','B','C','D','C','M'],'C')
    [2, 4]
    >>> letter_positions(['A','M','C','D','A','M'],'M')
    [1, 5]
    '''
    
# The function will return an empty list if the character given in not at all
#found in the list
    
    char_index = []
    for i in range (len(letter_list)):
        if character == letter_list[i]:
            char_index.append(i)
    return char_index


def valid_word_pos_direction(letter_list,word,index,direction):
    '''
    (list,string,integer,integer)-->(Boolean value)
    
    first the function will validate the indices by using is_outside_list function
    and returns a boolean vlaue by checking if the given word, in the given direction
    is in the letter list or not 
    
    >>> valid_word_pos_direction(['M','F','C','D','C','M'],'CFM',2,-1)
    True
    >>> valid_word_pos_direction(['T','S','C','K','C','M','G','H'],'MGH',5,1)
    True
    >>> valid_word_pos_direction(['A','B','C','D','C','M'],'CMP',4,1)
    False
    '''
    
    n = 0
    if direction == 1:
        if not (is_outside_list(letter_list,index+len(word)-1)) :
            for i in range (index,index+len(word),direction):
                if letter_list[i] != word[n]:
                    return False
                n = n + 1
            return True
        else:
            return False
    if direction == -1:
        if not (is_outside_list(letter_list,len(word)-1)) :
            for i in range (index,index-len(word),direction):
                if letter_list[i] != word[n]:
                    return False
                n = n + 1
            return True
        else:
            return False
        
        
def direction_word_given_position(letter_list,word,index):
    '''
    (list,string,integer)-->(list)
    
    First the function checks if the given word is in the list or not by using
    direction_word_given_position function and returns the directions in which the
    word is found in the form of list
    
    >>> direction_word_given_position(['J','C','C','H','C','C','J'],'HCCJ',3)
    [-1, 1]
    >>> direction_word_given_position(['A','B','C','D','C','M'],'DC',3)
    [-1, 1]
    >>> direction_word_given_position(['K','B','C','V','O','L'],'VOL',3)
    [1]
    '''
    
    direction = []
    if valid_word_pos_direction(letter_list,word,index,-1):
        direction.append(-1)
    if valid_word_pos_direction(letter_list,word,index,1):
        direction.append(1)
    return direction


def position_direction_word(letter_list,word):
    '''
    (list,string)-->(dictionary)
    
    returns the dictionary of where and in what direction the word is found by using
    the functions letter_positions for indices and direction_word_given_position for
    direction that we need to go in the letter list.
    
    >>> position_direction_word(['A','B','K','D','K','M'],'KDK')
    {2: [1], 4: [-1]}
    >>> position_direction_word(['A','B','K','D','K','M'],'ABK')
    {0: [1]}
    >>> position_direction_word(['A','B','K','D','K','M'],'DK')
    {3: [-1, 1]}
    '''
    
    dictonary = {}
    positions = letter_positions(letter_list,word[0])
    for element in positions:
        dictonary[element] = direction_word_given_position(letter_list,word,element)
    return dictonary


def cross_word_position_direction(letter_list,word,index,direction):
    '''
    (list,string,integer,integer)--> (no output)
    
    updates the given letter list by replacing every character of the word
    found in letter list at given index and direction by '*' 
    
    >>> letter_list = ['A','B','K','D','K','M']
    >>> cross_word_position_direction(letter_list,'ABK',0,1)
    >>> print(letter_list)
    ['*', '*', '*', 'D', 'K', 'M']
    
    >>> letter_list = ['*','*','*','D','K','M']
    >>> cross_word_position_direction(letter_list,'KD',4,-1)
    >>> print(letter_list)
    ['*', '*', '*', '*', '*', 'M']
    
    >>> letter_list = ['A','P','P','L','E']
    >>> cross_word_position_direction(letter_list,'PP',1,1)
    >>> print(letter_list)
    ['A', '*', '*', 'L', 'E']
    
    '''
#Here we will assume that the word is accurately located at the given index and direction
#we won't be needing to validate the index using valid_word_pos_direction     


    if direction == 1:
        for i in range(index,index+len(word),direction):
            letter_list[i] = '*'
    if direction == -1:
        for i in range(index,index-len(word),direction):
            letter_list[i] = '*'
            
            
def cross_word_all_position_direction(letter_list,word,dict_position_direction):
    '''
    (list,string,dictionary)-->(no output)
    
    The function will call cross_word_position_direction and updates the letter list
    by replacing the letters of the word by ’*’ at the different positions and
    directions where the word is found.
    
    >>> letter_list = ['A','B','C','D','C','B','A']
    >>> cross_word_all_position_direction(letter_list,'ABC',{0:[1],6:[-1]})
    >>> print(letter_list)
    ['*', '*', '*', 'D', '*', '*', '*']
    >>> letter_list = ['S','B','Q','D','H','B','G']
    >>> cross_word_all_position_direction(letter_list,'HBG',{4:[1]})
    >>> print(letter_list)
    ['S', 'B', 'Q', 'D', '*', '*', '*']
    >>> letter_list = ['S','B','H','D','H','B','G']
    >>> cross_word_all_position_direction(letter_list,'DH',{3:[1,-1]})
    >>> print(letter_list)
    ['S', 'B', '*', '*', '*', 'B', 'G']
    '''
    
    for key in dict_position_direction:
        directions = dict_position_direction[key]
        for i in range(len(directions)):
            cross_word_position_direction(letter_list,word,key,dict_position_direction[key][i])

#Here and in the above function there is no return statement because these function just update the letter list
#we know that the list are mutable
            
def find_magic_word(letter_list):
    '''
    (list)-->(string)
    
    The function will return the word that is formed by combing the letters
    that are found in the given letter list that are not crossed out '*'
    
    >>> find_magic_word(['S','A','*','*','*','V','E'])
    'SAVE'
    >>> find_magic_word(['C','A','*','*','M','P'])
    'CAMP'
    >>> find_magic_word(['S','A','*','*','D'])
    'SAD'
    '''
    
    new_letter_list = []
    for i in letter_list:
        if i != '*' :
            new_letter_list.append(i)
    word = ''.join(new_letter_list)
    return word
    
    
def word_search(letter_list,word_list):
    '''
    (list,list)-->(string)
    
    function will first get the positions and directions of the words given using
    position_direction_word function and cross out the letters of the words that
    are in the letter list using cross_word_all_positio_direction function
    and will return the word that is formed by the combining the letters remaning
    that are not crossed out
    
    
    >>> word_search(['H','E','L','L','O','W','O','R','L','D'],['HELLO'])
    'WORLD'
    >>> word_search(['H','E','L','L','O','B','E','A','U','T','I','F','U','L','W','O','R','L','D'],['HELLO','WORLD'])
    'BEAUTIFUL'
    >>> word_search(['H','E','Y','M','U','B','E','E','N'],['MUBEEN'])
    'HEY'
    '''
    
    new_list = []
    for element in word_list:
        word_position = position_direction_word(letter_list,element)
        cross_word_all_position_direction(letter_list,element,word_position)
    new_list = find_magic_word(letter_list)
    word = ''.join(new_list)
    return word


def word_search_main(filepath):
    '''
    (string)-->(string)
    
    This function will read the given input file where it has in its first line a
    list of letters. It will read that first line and converts it into a list of characters. The
    function will then read the following lines where each line will contain a specific word
    and it will build the word list using each word listed in the file starting from the
    second line. Then the function will return the magic word by calling word_search function.
    
    >>> word_search_main('word_search_text.txt')
    'PYTHON'
    
    >>> f = open('my_file.txt','r')
    >>> file = f.read()
    >>> print(file)
    HelloEveryOneMyNameisMubeen
    Hello
    Everyone
    my
    Name
    is
    >>> word_search_main('my_file.txt','r')
    'MUBEEN'
    
    >>> f = open('your_file.txt','r')
    >>> file = f.read()
    >>> print(file)
    MybirthDayistomOrrow
    My
    Birthday
    is
    >>> word_search_main('your_file.txt')
    'TOMORROW'
    '''
    
    file_list = []
    letter_list = []
    word_list = []
    file = open(filepath,'r')
    for line in file:
        file_list.append(line)
    file.close()
    first_line = file_list[0]
    for char in first_line:
        letter_list.append(char.capitalize())
    letter_list.remove('\n')
    for word in file_list[1:]:
        word_list.append((word.strip()).upper())
    return word_search(letter_list,word_list)


