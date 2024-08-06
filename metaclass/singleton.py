"""
################################### Output of this code #########################
Got new request for <class '__main__.SomethingImportant'>
No instance exist, hence creating one!
Got new request for <class '__main__.SomethingImportant'>
True
"""
class SingletonMeta(type):
    __instance__ = {}

    def __call__(cls, *args, **kwargs):
        """
        This is different from __new__ method, which is used to create new class, __call__ method is used to create new instance
        cls will be __main__.SomethingImportant
        """
        print(f"Got new request for {cls}")
        if cls not in cls.__instance__:
            print("No instance exist, hence creating one!")
            # be careful not to use cls in __call__
            cls.__instance__[cls] = super().__call__(*args, **kwargs)
        return cls.__instance__[cls]

class SomethingImportant(metaclass = SingletonMeta):
    pass


s1 = SomethingImportant()
s2 = SomethingImportant()

print (s1 == s2)


        

    