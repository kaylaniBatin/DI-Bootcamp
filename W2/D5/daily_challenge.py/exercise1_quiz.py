# exercise1_quiz.py

def oop_quiz_answers():
    answers = {
        "What is a class?":
            "A class is a blueprint for creating objects, encapsulating data and behavior into one structure.",
        "What is an instance?":
            "An instance is a specific object created from a class, with its own unique data.",
        "What is encapsulation?":
            "Encapsulation is the concept of restricting direct access to some of an object's components, usually through accessors/mutators.",
        "What is abstraction?":
            "Abstraction means hiding complex implementation details and showing only the necessary features of an object.",
        "What is inheritance?":
            "Inheritance allows one class to inherit attributes and methods from another class.",
        "What is multiple inheritance?":
            "Multiple inheritance allows a class to inherit from more than one parent class.",
        "What is polymorphism?":
            "Polymorphism allows different classes to be treated as instances of the same class through a shared interface.",
        "What is method resolution order or MRO?":
            "MRO is the order in which Python looks for a method in a hierarchy of classes. It's important for determining which method to execute in case of inheritance."
    }

    print("=== OOP Quiz Answers ===")
    for question, answer in answers.items():
        print(f"{question}\n {answer}\n")


if __name__ == "__main__":
    oop_quiz_answers()
