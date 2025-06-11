Java Proficiency Test
=====================

This two-part coding challenge will help you review your understanding of basic Java concepts including classes, objects, methods, variables, and logic.

Part 1: Pet Simulator (OOP Practice)
------------------------------------

**Goal:** Practice using classes, constructors, methods, and objects.

Create a Java program with two classes: ``Dog`` and ``Cat``.

Each class should have:
- At least one **instance variable** (for example: ``name``, ``age``, or ``isHungry``).
- A **constructor** that initializes the instance variable(s).
- A **method**:
  
  - ``Dog``: Implement a method called ``bark()`` that prints a message like::
  
      Rex says: Woof!
  
  - ``Cat``: Implement a method called ``meow()`` that prints a message like::
  
      Mittens says: Meow!

In a separate ``Main`` class (with a ``main`` method):
- Create one ``Dog`` object and one ``Cat`` object.
- Call each of their methods.

**What this tests:**
- Creating classes and methods
- Constructors and instance variables
- Creating and using objects
- Calling methods

Part 2: Pet Feeding System (Logic and Control Flow)
---------------------------------------------------

**Goal:** Practice using variables, if-statements, and logic.

Expand your existing ``Dog`` and ``Cat`` classes to include:

- A boolean instance variable: ``isHungry``.
- A method called ``feed()``:
  
  - If the pet *is hungry*, print a message like::
  
      Feeding Rex...
  
    Then update ``isHungry`` to ``false``.

  - If the pet *is not hungry*, print a message like::
  
      Rex is not hungry.

In your ``Main`` method:
- Create a pet that is hungry.
- Call ``feed()`` on it **twice**, and observe the output.

**What this tests:**
- Use of boolean variables
- If-statements and conditionals
- Updating and checking object state

Optional Bonus Challenge
------------------------

If you're feeling confident, try the following:

- Create a shared interface or abstract class called ``Pet`` with a method ``speak()``.
- Implement and override ``speak()`` in both ``Dog`` and ``Cat``.

This will give you practice with **inheritance** and **polymorphism**.

Completed
----------

- Justin Hollister
- Vincent Schelstreate
- Ivan Kirigan
- Akash Seetheraman
- Mihai Popescu