"""

Домашнее задание №1

Цикл while: hello_user

* [x] Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def hello_user():
    user_input_fine = False
    # где-то слышал, что while True - не очень хорошо использовать, почему?
    while not user_input_fine:
        user_input = input("Как дела?\n")
        if user_input.lower() == "хорошо":
            user_input_fine = True
            print('Ну пока')
            # break
    print()

if __name__ == "__main__":
    hello_user()
