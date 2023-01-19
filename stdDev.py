def std_deviation(list_of_people):
    ages = []
    for person in list_of_people:
        ages.append(person.get_age())
    list_sum = sum(ages)
    total = len(ages)
    list_ave = list_sum/total
    variances = []
    for num in ages:
        variances.append((num-list_ave)**2)
    variance = sum(variances)/len(list_of_people)
    deviation = variance ** 0.5
    return deviation

class Person:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

p1 = Person("Kyoungmin", 100)
p2 = Person("Mercedes", 20)
p3 = Person("Beatrice", 5)
plist = [p1,p2,p3]
answer = std_deviation(plist)
print(answer)