import sys
from stats import get_num_words
from stats import count_character
from stats import sorted_list

def get_book_text(file):

    with open(file) as f:
        return f.read()
    
def main():
    final_count = {"a": 0}
    sorted_count = []
    book = "books/frankenstein.txt"

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]

    book_text = get_book_text(book)
    word_count = get_num_words(book_text)
    #print(f"Found {word_count} total words")

    final_count = count_character (book_text)

    sorted_count = sorted_list(final_count)

   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for sc in sorted_count:
        print(f"{sc["letter"]}: {sc["count"]}")
    print("============= END ===============")
    

main()
