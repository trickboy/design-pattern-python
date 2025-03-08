# Creational Patterns
# Factory Pattern
# Imagine you’re running a bakery. Depending on the order, you might create a cake, a muffin, or a loaf of bread.
# The Factory pattern works the same way: it provides a single interface to create objects, but the actual object created depends on the input.

class Notification:
    def notify(self):
        pass

class EmailNotification(Notification):
    def notify(self):
        print("Sending email notification")

class SMSNotification(Notification):
    def notify(self):
        print("Sending sms notification")

class NotificationFactory:
    @staticmethod
    def get_notification(method):
        if method == "email":
            return EmailNotification()
        elif method == "sms":
            return SMSNotification()
        else:
            return Notification()

notification_factory = NotificationFactory.get_notification("email")
notification_factory.notify()
notification_factory = NotificationFactory.get_notification("sms")
notification_factory.notify()
notification_factory = NotificationFactory.get_notification("")
notification_factory.notify()
