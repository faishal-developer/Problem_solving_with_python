# purpose: defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically
# use case: often used in event-driven programming, such as GUIS, or notifying subscribers when a change occurs.

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self,observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class observer:
    def update(self):
        raise NotImplementedError

class ConcreteObserver(observer):
    def update(self):
        print("observer has benn notified")


subject= Subject()
observer=ConcreteObserver()
subject.attach(observer)
subject.notify()