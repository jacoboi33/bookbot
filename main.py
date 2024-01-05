def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    character_dict = character_count(text)
    print(f"{word_count(text)} words found in the document\n\n")
    print_character_report(character_dict)

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
        if char in character_dict and char.isalpha():
            character_dict[char] += 1
        elif char.isalpha():
            character_dict[char] = 1
    return character_dict

def print_character_report(character_dict):
    character_list = []
    for key in character_dict:
        character_list.append((key, character_dict[key]))
    character_list.sort(key=lambda tup: tup[1], reverse=True)

    for char in character_list:
        print(f"The {char[0]} character was found {char[1]} times")
    
    print("--- End report ---")


main()