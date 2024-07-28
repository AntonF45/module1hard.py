# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
# а значением - его средний балл.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_in_alphabetical_order = sorted(list(students))  # Преобразование списка студентов по алфавиту
# print(students_in_alphabetical_order)
average_scores = []
for grade in grades:
    average_score = sum(grade) / len(grade)  # Вычисление среднего балла студентов
    average_scores.append(average_score)  # Добавляем полученные элементы в список average_scores
# print(average_scores)
dictionary_average_score = dict(zip(students_in_alphabetical_order, average_scores))  # Преобразование списка студентов
# и списка со средним балом в словарь dictionary_average_score
print(dictionary_average_score)
