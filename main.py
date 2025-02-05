def main():
    book_path = "books/frankenstein.txt" # шлях до файлу з книжкою
    text = book_txt(book_path) # зчитує текст книги
    new_words = get_num_words(text)
    chars_dict = get_chars_dict(text) # Отримуємо словник з кількістю символів
    sort_chars = sort_chars_dict(chars_dict)

    print(F"--- Begin report of {book_path} ---")
    print(f"{new_words} words fount in the document\n")

    for char_data in sort_chars:
        print(f"The '{char_data['char']}' character was found {char_data['num']} times")
    print("---End report ---")

def get_num_words(text):
    words = text.split()   # Лічимо кількість слів у тексті
    return len(words)


def book_txt(path):
    with open("books/frankenstein.txt") as f:
        return f.read() # зчитуємо весь файл як текст
    

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower() # зменшуємо регіст символу
        if lowered in chars:
            chars[lowered] += 1 # збільшуємо значення для цього символу
        else:
            chars[lowered] = 1 # додаємо новий ключ для символу
    return chars

def sort_chars_dict(chars_dict):
    char_list = []
    for char, count in chars_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_by_count)
    return char_list

def sort_by_count(char_dict):
    return char_dict["num"]

main()    