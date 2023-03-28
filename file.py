import string

def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Видаляємо зайві пробіли з початку та кінця тексту
        content = content.strip()
        # Рахуємо кількість слів
        words = content.split()
        word_count = len(words)
        return word_count