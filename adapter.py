# Adapter Pattern
# Ever used a travel adapter to plug your devices into a foreign socket?
# The Adapter pattern bridges the gap between two incompatible interfaces, allowing them to work together seamlessly.

class Legacy:
    def __init__(self):
        self.data = "legacy data"
        print("Access Legacy System")

    def get_data(self):
        return "Fetch Legacy System Data"

class  NewSystem:
    def __init__(self):
        self.data = "new data"
        print("Access New System")


    def get_data(self):
        return "Fetch New System Data"

class Adapter:
    def __init__(self, system):
        self.system = system

    def get_data(self):
        return self.system.get_data()


# Usage
legacy = Legacy()
adapter1 = Adapter(legacy)
print(adapter1.get_data())
newSystem = NewSystem()
adapter2 = Adapter(newSystem)
print(adapter2.get_data())