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
