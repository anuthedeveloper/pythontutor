
class Person():

    def __init__(self, name, age, gender):
        # private
        self.__name = name 
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def static():
        print("Call to a static method")


Person.static()

p1 = Person('Joseph', 23, 'male')
print(p1.Name)

# when you have setter to reference the props
p1.Name = "Michael"
print(p1.Name)