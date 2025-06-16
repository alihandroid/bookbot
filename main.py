import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    path = sys.argv[1]
    print(f"Analyzing book found at {path}")
    book_str = get_book_text(path)
    
    print("----------- Word Count ----------")
    num_words = get_num_words(book_str)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    char_counts = get_char_counts(book_str)
    char_counts = sort_char_counts(char_counts)
    for c in char_counts:
        if c.isalpha():
            print(f"{c}: {char_counts[c]}")

main()