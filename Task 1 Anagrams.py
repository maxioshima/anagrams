if __name__ == '__main__':
    cases = [
        'asl1d1fskld asdf34ga'
    ]

    for case in cases:
        list_of_letter = []
        position_of_exceptions = {}  # хранит в себе индексы фиксируемых значение


        def counter_of_words(case):  # функция, которая считает кол-во слов в строке
            if case.find(' ') < 1:
                word = case
                return word_gathering(word)
            else:
                return ' '.join([word_gathering(word) for word in case.split()])


        def word_gathering(word):  # Функция 'собирает' элементы в готовую строку
            list_of_letter.clear()  # Очищает массив и словарь от значений предыдущей строки, если такая была
            position_of_exceptions.clear()
            one_word_remove(word)
            revers_word = list_of_letter[::-1]
            [revers_word.insert(key, position_of_exceptions[key]) for key in position_of_exceptions]
            return ''.join(revers_word)


        def one_word_remove(
                word):  # Функция делает из строки массив, и затем сортирует фиксируемые и нефиксируемые элементы
            list_by_word = list(word)
            for i in range(0, len(list_by_word)):
                if list_by_word[i].isalpha():
                    list_of_letter.append(list_by_word[i])  # добавляет в list нефиксируемые эл.
                else:
                    position_of_exceptions[i] = list_by_word[i]  # добавляет в dict фиксируемые элементы и их индексы


        print(counter_of_words(case))
