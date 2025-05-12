def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        file_contents = f.read()
    return file_contents

def main():

    from stats import get_num_words

    from stats import get_num_char

main()