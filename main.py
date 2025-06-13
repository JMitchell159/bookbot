import sys
from stats import num_words
from stats import num_char_sorted

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    
    return contents

def main():
    books = "book_directory.txt"
    with open(books) as b:
        book_list = b.read().split()
    for i in range(len(book_list)):
        book_list[i] = f"books/{book_list[i]}"
    
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>. Warning: All other arguments will be ignored")
    file = sys.argv[1]
    if file not in book_list:
        print("You must enter a valid book path")
        sys.exit(1)
    
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