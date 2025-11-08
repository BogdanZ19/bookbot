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


def sort_on(item):
    return item["num"]


def get_sorted_letter_arr(letter_dict):
    dict_list = []
    
    for letter in letter_dict:
        dict_list.append({"char": letter, "num": letter_dict[letter]})
    dict_list.sort(reverse = True, key=sort_on)   
    return dict_list
