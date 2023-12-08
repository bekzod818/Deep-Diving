## 1. Single-Responsibility Principle (SRP)

The single-responsibility principle (SRP) comes from Robert C. Martin, more commonly known by his nickname Uncle Bob, who’s a well-respected figure in the software engineering world and one of the original signatories of the Agile Manifesto. In fact, he coined the term SOLID.

The single-responsibility principle states that:

> A class should have only one reason to change.

This means that a class should have only one responsibility, as expressed through its methods. If a class takes care of more than one task, then you should separate those tasks into separate classes.

## 2. Open-Closed Principle (OCP)

The open-closed principle (OCP) for object-oriented design was originally introduced by Bertrand Meyer in 1988 and means that:

> Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

## 3. Liskov Substitution Principle (LSP)

The Liskov substitution principle (LSP) was introduced by Barbara Liskov at an OOPSLA conference in 1987. Since then, this principle has been a fundamental part of object-oriented programming. The principle states that:

> Subtypes must be substitutable for their base types.

For example, if you have a piece of code that works with a Shape class, then you should be able to substitute that class with any of its subclasses, such as Circle or Rectangle, without breaking the code.

## 4. Interface Segregation Principle (ISP)

The interface segregation principle (ISP) comes from the same mind as the single-responsibility principle. Yes, it’s another feather in Uncle Bob’s cap. The principle’s main idea is that:

> Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.

In this case, clients are classes and subclasses, and interfaces consist of methods and attributes. In other words, if a class doesn’t use particular methods or attributes, then those methods and attributes should be segregated into more specific classes.

## 5. Dependency Inversion Principle (DIP)

The dependency inversion principle (DIP) is the last principle in the SOLID set. This principle states that:

> Abstractions should not depend upon details. Details should depend upon abstractions.

## Conclusion \#

You’ve learned a lot about the five **SOLID principles**, including how to identify code that violates them and how to refactor the code in adherence to best design practices. You saw good and bad examples related to each principle and learned that applying the SOLID principles can help you improve your **object-oriented design** in Python.

**In this tutorial, you’ve learned how to:**

* Understand the **meaning** and **purpose** of each **SOLID principle**
* Identify class designs that **violate** some of the SOLID principles in Python
* Use the SOLID principles to help you **refactor** Python code and improve its OOD

With this knowledge, you have a strong foundation of well-established best practices that you should apply when designing your classes and their relationships in Python. By applying these principles, you can create code that’s more maintainable, extensible, scalable, and testable.
