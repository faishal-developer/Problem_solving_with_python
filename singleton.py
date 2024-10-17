# a class has only one instance and provides a global point of access it
# used for managing resources like database connections, logging, etc
class Singleton:
    _instance=None

    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)
        
        return self._instance
    
s1=Singleton()
s2=Singleton()

print(s1 == s2)