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
    
def count_sentences(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Видаляємо зайві пробіли з початку та кінця тексту
        content = content.strip()
        # Рахуємо кількість речень
        sentence_count = 0
        for char in content:
            if char in [".", "!", "?"]:
                sentence_count += 1
        return sentence_count
    
def count_words_and_sentences(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Видаляємо зайві пробіли з початку та кінця тексту
        content = content.strip()
        # Рахуємо кількість слів
        words = content.split()
        word_count = len(words)
        # Рахуємо кількість речень
        sentence_count = 0
        for char in content:
            if char in [".", "!", "?"]:
                sentence_count += 1
        return "Кількість слів " , word_count, "Кількість речень ",sentence_count