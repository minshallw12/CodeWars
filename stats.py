import statistics

class Student:

    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        return self._grade
    def get_name(self):
        return self._name

def basic_stats(list_of_objects):
    grades = []
    for grade in list_of_objects:
        grades.append(grade.get_grade())
        ave = statistics.mean(grades)
        med = statistics.median(grades)
        mod = statistics.mode(grades)
    return (ave, med, mod)


s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))