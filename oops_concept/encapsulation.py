class Student:
    name = "rohan";
    marks = 24;

s1 = Student()
print(s1.name)
print(s1.marks)
    # print(name,marks);


class Car:
    # This is a class attribute, shared among all instances of Car
    available_models = ["Mercedes", "Ferrari", "Bugatti"]

    def __init__(self, model):
        # This is an instance attribute
        self.model = model
        for j in self.model:
            print(f"New Car Model is {j}")
        self.model = model
        for i in self.available_models:  # Loop through the list of models
            print(f"- {i}")  # Print each model
        print(f"Car model '{self.model}' has started.")
        for i in self.available_models:
            print(f"Car Model Name is {i}")


# Creating an instance of the Car class
car = Car(["Ferrari","Hundai"])


