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

def main(first_line,second_line):
    if type(first_line) != str and type(second_line) != str:
        return "0"
    elif first_line == second_line:
        return "1"
    elif first_line != second_line and len(first_line) > len(second_line):
        return "2"
    elif first_line != second_line and second_line == "learn":
        return "3"
print(main(3, 3))
print(main("line", "line"))
print(main("hello", "hey"))
print(main("teach", "learn"))
    