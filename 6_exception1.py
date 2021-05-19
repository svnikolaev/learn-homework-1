"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* [x] Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    user_input_fine = False
    while not user_input_fine:
        try:
            user_input = input("Как дела?\n")
            if user_input.lower() == "хорошо":
                user_input_fine = True
                print('Ну пока')
        except KeyboardInterrupt:
            print()
            print("Пока!")
            break
            
    
if __name__ == "__main__":
    hello_user()
