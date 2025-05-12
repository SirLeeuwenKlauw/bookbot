def get_num_words():
    from main import get_book_text
    text = get_book_text("books/frankenstein.txt")
    words = []
    num_words = 0
    words = text.split()

    for i in range(0, len(words)):
        num_words += 1

    print(num_words,"words found in the document") 

get_num_words()

def get_num_char():
    from main import get_book_text
    text = get_book_text("books/frankenstein.txt")
    lowercase_text = text.lower()
    print(lowercase_text)
    char_num = {}
    
    for char in lowercase_text:
        if char in char_num:
            char_num[char] += 1
        else:
            char_num[char] = 1
        

    print(char_num)


get_num_char()