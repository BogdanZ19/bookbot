def get_book_text(file_path):
    with open(file_path) as path:
        book_text = path.read()
        return book_text

def get_word_count(book_text):
    arr = book_text.split()
    return len(arr)
    
    
def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = get_word_count(text)
    # print(text)
    print(f"Found {word_count} total words")
    
main()
    
    
    