text_position_quantity = input('Введите текст, позицию, количество слов: ')

def string(text, i, quantity_words):
    words = text.split(' ')
    if (quantity_words <= 0):
        return text
    word = selected_word(text, i)
    last_words = words[:word] + words[word + quantity_words:]
    return str.join(' ', last_words)

def selected_word(text, position):
    text_position = text[:position]
    left_words = len(text_position.split(' '))
    if len(text) >= position:
        return left_words
    return left_words - 1

doc = text_position_quantity.split(',')
print(string(doc[0], int(doc[1].strip(),0), int(doc[2].strip(),0)))
