def count_words_starting_with_e(text):
    words = text.split()
    count = sum(1 for word in words if word.lower().startswith('е'))
    return count

if __name__ == "__main__":
    text = input("Введите строку: ")
    result = count_words_starting_with_e(text)
    print(f"Количество слов, начинающихся с буквы 'е': {result}")
