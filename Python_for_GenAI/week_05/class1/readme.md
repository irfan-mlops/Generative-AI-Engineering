# Functional Programming in Python

Functional Programming (FP) is a programming paradigm that focuses on using functions to process data and build reusable, predictable code.

## Core Concepts

* **First-Class Functions** — Functions can be assigned to variables, passed as arguments, and returned from other functions.
* **Higher-Order Functions** — Functions that accept or return other functions.
* **Lambda Functions** — Small anonymous functions for simple operations.
* **map()** — Applies a function to every item in an iterable.
* **filter()** — Selects items based on a condition.
* **reduce()** — Combines iterable elements into a single result.
* **Pure Functions** — Functions that produce the same output for the same input without side effects.
* **Immutability** — Avoiding unnecessary modification of existing data.

## Example

```python
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

## Key Takeaway

Functional programming helps write Python code that is modular, reusable, and easier to reason about. For Generative AI engineering, understanding the practical concepts of FP is sufficient.
