# Behavioral Patterns
# Strategy Pattern
# Think about choosing a route on a GPS app. Depending on your preference (fastest, shortest, or scenic), the app changes its behavior.
# The Strategy pattern allows you to switch algorithms dynamically at runtime.

class Strategy:
    def execute(self, data):
        print(f"Strategy execute {data}")
        # pass

class FastestRoute(Strategy):
    def execute(self, data):
        print(f"Calculating the fastest route for {data}")

class ScenicRoute(Strategy):
    def execute(self, data):
        print(f"Calculating the scenic route for {data}")

class Navigator:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def navigate(self, data):
        self._strategy.execute(data)


navigate = Navigator(FastestRoute())
navigate.navigate("Destination")
navigate.set_strategy(ScenicRoute())
navigate.navigate("Destination")
