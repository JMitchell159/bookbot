from stats import num_words
from stats import num_char_sorted

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    
    return contents

def main():
    file = "books/frankenstein.txt"
    sorted_chars = num_char_sorted(get_book_text(file))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words(get_book_text(file))} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()