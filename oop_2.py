class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

    @voltage.setter
    def voltage(self, val):
        self._voltage = val


#
# p = Parrot()
# print(p.voltage)
# p.voltage = 100
# print(p.voltage)
#

class Parent:  # define parent class
    def __init__(self):
        self.attr = 100
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def set_attr(self, attr):
        self.attr = attr

    def get_attr(self):
        print("Parent attribute :", self.attr)


class Child(Parent):  # define child class
    def __init__(self):
        super().__init__()
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
# c.set_attr(200)  # again call parent's method
# c.get_attr()  # again call parent's method
print(c.attr)
print(Child.mro())
