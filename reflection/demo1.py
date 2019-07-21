# encoding:utf-8

# 有时候我们会碰到这样的需求，需要执行对象的某个方法，或是需要对对象的某个字段赋值，
# 而方法名或是字段名在编码代码时并不能确定，需要通过参数传递字符串的形式输入。举个具体的例子：
# 当我们需要实现一个通用的DBM框架时，可能需要对数据对象的字段赋值，但我们无法预知用到这个框架
# 的数据对象都有些什么字段，换言之，我们在写框架的时候需要通过某种机制访问未知的属性


class User:
    __name = None    # 设为私有属性
    __sex = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSex(self, sex):
        self.__sex = sex

    def getSex(self, sex):
        return self.__sex


user = User()


if hasattr(user, "setName"):
    setter = getattr(user, "setName")  # 获取set的方法
    setter("jack")  # 调用set
    print(user.getName())


