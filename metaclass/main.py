import random

class MyMetaClass(type):
    """
    The implementation of a meta class. __init__ and __new__ are minimum set of functions
    """
    def __init__(cls, name, bases, attrib):
        """
        cls: class that is being initialized
        name: name of the class
        bases: Tuples of base class
        attrib: methods or variables associated with the class
        """
        print(f"Initializing the class {cls}, with metaclass: {name}, bases: {bases}, attrib: {attrib}")
        super().__init__(name, bases, attrib)
    

    def __new__(cls, name, bases, attrib):
        """
        Partameters same as above, but must return the object
        """
        print("Creating a new instance")
        return super().__new__(cls, name, bases, attrib)

class Sample(metaclass = MyMetaClass):
    def __init__(self) -> None:
        pass

    def get_me_a_sample(self):
        return random.randint(1, 100)

    pass

s1 = Sample()