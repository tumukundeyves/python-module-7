# Creature Battle System

## Overview

This project is a Python implementation of several Object-Oriented Programming (OOP) design patterns. It simulates a small creature battle game where creatures are created by factories, gain special capabilities, and fight using different battle strategies.

The project is divided into three exercises, each introducing a new design pattern.

---

## Project Structure

```
.
├── battle.py
├── capacitor.py
├── tournament.py
├── ex0
├── ex1
└── ex2
```

---

## Exercise 0 – Abstract Factory

Implements the **Abstract Factory** design pattern.

Features:
- Abstract `Creature` class
- Fire and Water creature families
- `FlameFactory` and `AquaFactory`
- Base and evolved creature creation

Run:

```bash
python3 battle.py
```

---

## Exercise 1 – Capabilities

Builds on Exercise 0 by adding reusable capabilities.

Features:
- `HealCapability`
- `TransformCapability`
- Healing creatures
- Transforming creatures
- Multiple inheritance

Run:

```bash
python3 capacitor.py
```

---

## Exercise 2 – Strategy

Builds on Exercises 0 and 1 by implementing the **Strategy** design pattern.

Features:
- `NormalStrategy`
- `DefensiveStrategy`
- `AggressiveStrategy`
- Tournament simulation
- Custom exception for invalid strategy combinations

Run:

```bash
python3 tournament.py
```

---

## Design Patterns Used

- Abstract Factory
- Strategy
- Abstraction
- Inheritance
- Polymorphism
- Multiple Inheritance

---

## Requirements

- Python 3.10+
- Only standard Python libraries
- Type hints
- Compatible with `mypy`

Check types:

```bash
mypy .
```

---

## Learning Objectives

This project demonstrates how to:

- Create objects using factories.
- Reuse code through inheritance.
- Separate behaviors using capabilities.
- Change object behavior using the Strategy pattern.
- Organize a Python project using packages and `__init__.py`.

---

## Author

Yves Tumukunde
