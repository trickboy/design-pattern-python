# Observer / PubSub Pattern
# Picture a social media app. You follow your favorite influencer, and every time they post, you get notified.
# The Observer pattern works similarly: objects (observers) subscribe to another object (subject) and get updates when the subject changes.

class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)
            observer.update()


class Observer:
    def notify(self, subject, *args, **kwargs):
        print(f"{type(self).__name__}:: Got {args} from {subject}")

    def update(self):
        pass

class BuildConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self):
        print('BuildObserver:: Updated')
        print(f"{self.name} received notification")


subject = Subject()
subscriber1 = BuildConcreteObserver('subscriber1')
subscriber2 = BuildConcreteObserver('subscriber2')

subject.subscribe(subscriber1)
subject.subscribe(subscriber2)
subject.unsubscribe(subscriber1)
subject.notify_all()