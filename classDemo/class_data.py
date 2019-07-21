# encoding:utf-8

a = 1
class Student:

    __name = None
    __age = None

    def set_name(self, name):
        self.__name = name

    def get_name(self, name):
        return self.get_name()

    def set_age(self, age):
        self.__age = age

    def get_age(self, age):
        return self.__age

    def __str__(self) -> str:
        return "{" + "name:{},age:{}".format(self.__name, self.__age) + "}"

    def __repr__(self):
        return "{" + "name:{},age:{}".format(self.__name, self.__age) + "}"




