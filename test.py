def word_search_main(filepath):
    file_list = []
    letter_list = []
    word_list = []
    new_word = ''
    new_word_list = []
    file = open(filepath,'r')
    for line in file:
        file_list.append(line)
    first_line = file_list[0]
    for char in first_line:
        letter_list.append(char.capitalize())
    letter_list.remove('\n')
    for word in file_list[1:]:
        word_list.append((word.strip()).upper())
    word_search(letter_list,word_list)
    
print(word_search_main('word_search_text.txt'))
    
    
    