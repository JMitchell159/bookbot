from stats import num_words

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    
    return contents

def main():
    print(f"{num_words(get_book_text("books/frankenstein.txt"))} words found in the document")

main()