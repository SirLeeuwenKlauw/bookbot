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