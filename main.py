from stats import get_num_words, get_num_char, get_sorted

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_num = get_num_char(text)
    sorted_char = get_sorted(char_num)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char:
        character = entry["char"]
        num = entry["num"]
        if character.isalpha():
            print(f"{character}: {num}")
    print("============= END ===============")


def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        file_contents = f.read()
        return file_contents

main()