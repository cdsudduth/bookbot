def __main__():
    book_path = "Books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in document")

def get_num_words(text):
    words = text.split( )
    return len(words)

def get_book_text(path):
    with open(path) as book:
        book_content = book.read()
        return book_content
__main__()