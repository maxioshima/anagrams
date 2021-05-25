# if __name__=='__main__':
cases = [
    'asdmasmd',
    'asl1dfskld'
    ]


position_of_exceptions = []     #хранит в себе индексы фиксируемых значение


for case in cases:
        list_by_case = list(case)   #преобразует строку в список

        def counter_of_words(case): #функция, которая считает кол-во слов в строке
            if case.find(' ') < 1:
                return one_word_remove(case)
            else:



        def one_word_remove(case):  #функция для "переворота" строки с одним словом
            if case.isalpha() == True:
                return ''.join(case[::-1])  # "переворачивает" строку если в неё только литералы
            else:
                exception_positions(case)   # вызов функции
                pos = {position: list_by_case[position] for position in position_of_exceptions}     #словарь, хранящий в себе индексы, которые не переставляются и их значения
                for position in position_of_exceptions:     #удаляет элементы, которые не нужно переставлять
                    list_by_case.pop(position)
                return return_fix_values(case, pos)

        def return_fix_values(case, pos):   # функция возвращает на места фиксированные значения
            new_list_case = list_by_case[::-1]
            new_list_case.append('0'*len(pos))
            for key in pos.keys():  #этот цикл перебирает ключи словаря, и "двигает" элементы строки вправо, освобождая место для возвращения фиксированных элементов
                for i in range(len(new_list_case) - 1, key, -1):
                    new_list_case[i] = new_list_case[i - 1]
                new_list_case[key] = pos[key]
            return ''.join(new_list_case)

        def exception_positions(case):  #Эта функция определяет индексы фиксируемых элементов и добавляет их (индексы) в отдельный list
            # list_by_case = list(case)
            for i in range(0, len(list_by_case)):
                if list_by_case[i].isalpha() == False:
                    position_of_exceptions.append(i)



        print(counter_of_words(case))