from stats import get_word_count, get_letter_dict, get_sorted_letter_arr


def get_book_text(file_path):
    with open(file_path) as path:
        book_text = path.read()
        return book_text
    
def main():
    book = "books/frankenstein.txt"
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
    
    
    