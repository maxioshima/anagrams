def remove_word(word):  # Функция "переворачивает" слово, оставляя на месте отличные цифры и иные символы
    list_of_letter = [c for c in word if c.isalpha()]
    position_of_exceptions = {i: c for (i, c) in enumerate(word) if not c.isalpha()}
    revers_word = list_of_letter[::-1]
    [revers_word.insert(key, position_of_exceptions[key]) for key in position_of_exceptions]
    return ''.join(revers_word)


case = 'ed12adfgv qwet'
print(' '.join([remove_word(word) for word in case.split(' ')]))
