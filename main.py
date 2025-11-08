from stats import get_word_count, get_letter_dict


def get_book_text(file_path):
    with open(file_path) as path:
        book_text = path.read()
        return book_text
    
def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = get_word_count(text)
    letters_dict = get_letter_dict(text)
    # print(text)
    print(f"Found {word_count} total words")
    print(letters_dict)
main()
    
    
    