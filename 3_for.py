"""

Домашнее задание №1

Цикл for: Оценки

* [x] Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* [x] Посчитать и вывести средний балл по всей школе.
* [x] Посчитать и вывести средний балл по каждому классу.
"""

SCHOOL_CLASSES = [ 
    {
        'school_class': '1a',
        'scores': [3,3,5,3]
    },  
    {
        'school_class': '1b',
        'scores': [3,2,3,3,5,2]
    },  
    {
        'school_class': '2a',
        'scores': [3,5,4,4,3,5,5,2]
    },  
    {
        'school_class': '3a',
        'scores': [3,4,4,5]
    }, 
    {
        'school_class': '4a',
        'scores': [3,4,4,5,2]
    }, 
    {
        'school_class': '4b',
        'scores': [5,4,3,3,4,4,2]
    },  
]

def school_average_score(classes_list):
    scores = []
    for school_class in classes_list:
        scores.extend(school_class['scores'])
    return sum(scores)/len(scores)

def class_average_score(scores_list):
    return sum(scores_list)/len(scores_list)
    
    
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print("Средний балл по всей школе: " + str(school_average_score(SCHOOL_CLASSES))[:4])
    for school_class in SCHOOL_CLASSES:
        print("Класс: " + school_class['school_class'] + ", средний балл: " + str(class_average_score(school_class['scores']))[:4])

if __name__ == "__main__":
    main()
