def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    print(word_count(text))
    print(character_count(text))
    print("hello world")

def read_book(book_path):
    with open(book_path) as file1:
        text = file1.read()
    return text

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = text.lower()
    character_dict = {}
    for char in characters:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

main()