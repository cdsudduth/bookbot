def __main__():
    book_path = "Books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    list_of_dicts = dict_conversion(letter_count)
    sorted_letter_count = sort_dict(list_of_dicts)
    print(f"---Begin report of {book_path}---")
    print(f"{num_words} words found in document\n")
    for x in sorted_letter_count:
        print(f"The '{x[0]}' character was found {x[1]} times")


def get_letter_count(text):
    letter_dict = {
        'a': 0,
        'b': 0, 
        'c': 0, 
        'd': 0, 
        'e': 0, 
        'f': 0, 
        'g': 0, 
        'h': 0, 
        'i': 0,
        'j': 0, 
        'k': 0, 
        'l': 0, 
        'm': 0, 
        'n': 0, 
        'o': 0, 
        'p': 0, 
        'q': 0, 
        'r': 0, 
        's': 0, 
        't': 0, 
        'u': 0, 
        'v': 0, 
        'w': 0, 
        'x': 0, 
        'y': 0, 
        'z': 0
        }

    words = text.split( )
    
    for word in words:
        word = word.lower()
        for character in word:
            check_letter=False
            if character in letter_dict:
                check_letter = True
            if check_letter:
                letter_dict[character] += 1
    return letter_dict


def get_num_words(text):
    words = text.split( )
    return len(words)


def get_book_text(path):
    with open(path) as book:
        book_content = book.read()
        return book_content

def dict_conversion(dict):
    keys = dict.keys()
    counts = dict.values()
    merged_list = list(zip(keys,counts))
    #print(merged_list)
    return merged_list
def sort_dict(list):
    new_list = sorted(list, key = lambda x: int(x[1]), reverse=True)

    return new_list
__main__()