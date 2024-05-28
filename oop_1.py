import pylint
import pytest


class Employee:
    """Common base class for all employees"""

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.__private = 'private variable'
        Employee.empCount += 1

    @classmethod
    def show_count(cls):
        return f"empCount: {cls.empCount}"


def test_oop():
    e1 = Employee("Sana", 200)
    e2 = Employee("Sana", 200)
    assert e1.empCount == 2
    assert e2.empCount == 2
    assert Employee.empCount == 2
    assert Employee.show_count() == "empCount: 2"
    assert e2._Employee__private == "private variable"
