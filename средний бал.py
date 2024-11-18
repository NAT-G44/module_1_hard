

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)

average_grade = [sum(group) / len(group) for group in grades]
average_grade_dict = dict(zip(sorted_students, average_grade))
print(average_grade_dict)

