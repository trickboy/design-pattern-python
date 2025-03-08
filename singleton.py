# Singleton Pattern
# Think of a Singleton as the VIP pass to a club. Only one person—or instance—can hold the pass at a time.
# The Singleton pattern ensures that a class has only one instance and provides a global access point to it.

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized: return
        self.__initialized = True
        print('Singleton instance created')


singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)
