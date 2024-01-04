def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    print(text)
    print(word_count(text))
    print("hello world")

def read_book(book_path):
    with open(book_path) as file1:
        text = file1.read()
    return text

def word_count(text):
    words = text.split()
    return len(words)