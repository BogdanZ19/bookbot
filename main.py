from stats import get_word_count, get_letter_dict, get_sorted_letter_arr
import sys

def get_book_text(file_path):
    with open(file_path) as path:
        book_text = path.read()
        return book_text
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        book = sys.argv[1]
        
    text = get_book_text(book)
    word_count = get_word_count(text)
    letter_dict = get_letter_dict(text)
    sorted_letter_list = get_sorted_letter_arr(letter_dict)
    # print(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_letter_list:
        if letter["char"].isalpha() is True:
            print (f"{letter["char"]}: {letter["num"]}")
    
main()
    
    
    