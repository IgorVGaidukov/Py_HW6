"""
5. Реализовать формирование списка, используя функцию range()
и возможности LC.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""

print(reduce(lambda x, y: x * y, my_list))
