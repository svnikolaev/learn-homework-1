"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def compare_strings(first_string, second_string):
    # лучше делать return result в конце функции, или return value после каждого if/elif ?
    result = None
    # что лучше возвращать когда конфигурация переданных параметров не описана в спецификации?
    are_strings = type(first_string) == type(second_string) == type(str())
    if not are_strings:
        return 0
    if first_string == second_string:
        result = 1
    elif len(first_string) > len(second_string):
        result = 2
    elif first_string != second_string and second_string == "learn":
        result = 3
    return result

def main():
    print(compare_strings("a", 2)) #=> 0
    print(compare_strings(1, "bb")) #=> 0
    print(compare_strings(1, 2)) #=> 0
    print(compare_strings("aa", "bb")) #=> None
    print(compare_strings("aa", "aa")) #=> 1
    print(compare_strings("aaa", "aa")) #=> 2
    print(compare_strings("aaa", "learn")) #=> 3
    print(compare_strings("learnlearn", "learn")) #=> 2
    print(compare_strings("learn", "learn")) #=> 1
    
if __name__ == "__main__":
    main()
