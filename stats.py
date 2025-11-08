def get_word_count(book_text):
    arr = book_text.split()
    return len(arr)

def get_letter_dict(book_text):
    letter_dict = {}
    for letter in book_text:
        letter = letter.lower()
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1            
    return letter_dict 
        