def get_num_words(text):
    words = []
    num_words = 0
    words = text.split()

    for i in range(0, len(words)):
        num_words += 1

    return num_words 


def get_num_char(text):
    lowercase_text = text.lower()
    char_num = {}
    
    for char in lowercase_text:
        if char in char_num:
            char_num[char] += 1
        else:
            char_num[char] = 1
        
    return char_num
