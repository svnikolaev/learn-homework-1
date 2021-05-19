"""

Домашнее задание №1

Цикл while: ask_user со словарём

* [x] Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* [x] Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
    'как дела':'Хорошо!',
    'что делаешь':'Программирую',
    'как погода':'Нормальная, процессор греет',
    'пробки':'Нет, электроны просто летят',
    'свободу':'Роботам!',
    'свободен':'Все относительно',
    'кексик':'Экспериментальный центр напоминает вам, что вы торт',
}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    question = input("Пользователь: ")
    question = question.strip('?').lower()
    print("Программа: " + answers_dict[question])
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
