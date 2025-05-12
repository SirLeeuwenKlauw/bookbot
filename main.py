def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        file_contents = f.read()
    return file_contents

def main():

    text = get_book_text("books/frankenstein.txt")
    words = []
    num_words = 0
    words = text.split()

    for i in range(0, len(words)):
        num_words += 1

    print(num_words,"words found in the document")            

main()