from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def info(self):
        print(f"I am {self.name}")

class Dog(Animal):

    def make_sound(self):
        print("Bark!")

def main():
    dog = Dog("Buddy")
    dog.make_sound()

if __name__ == "__main__":
    main()