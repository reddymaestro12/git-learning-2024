from datetime import date


class Person:
    def __init__(self, name, age,sal):
        self.name = name
        self.age = age
        self.sal = sal

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year,sal):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21,1000)
person2 = Person.fromBirthYear('mayank', 1996,2000)

print(person1.age)
print(person2.age)
print("git diff test")
# print the result
print(Person.isAdult(22))