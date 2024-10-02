from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method(self):
        """ Interface method """


class Person(IPerson):

    def person_method(self):
        print("I am the person")


class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy person")
        self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()