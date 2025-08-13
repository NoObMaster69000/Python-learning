# 🐍 Python Learning Roadmap: From Basics to Advanced (Beginner → Pro)

Organized in **logical progression** — each topic builds on the previous one. Includes **what to learn**, **why it matters**, and **real-world use cases**.

---

## 🟢 Level 1: Python Basics (Beginner)
*Goal: Write simple scripts and understand syntax.*

### 1. **Getting Started**
- Installing Python (via Anaconda or official installer)
- Running Python: IDLE, Jupyter, VS Code, terminal
- `print()`, `input()`, comments

> 💡 *Use Case: Hello World, user interaction*

---

### 2. **Variables & Data Types**
- Variables (no declaration needed)
- Basic types: `int`, `float`, `str`, `bool`, `None`
- Type checking: `type()`
- Type conversion: `int("5")`, `str(3.14)`

> 💡 *Use Case: Storing user input, calculations*

---

### 3. **Operators**
- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `>`, `<`
- Logical: `and`, `or`, `not`
- Assignment: `=`, `+=`, `-=`

> 💡 *Use Case: Conditions, math operations*

---

### 4. **Control Flow**
- `if`, `elif`, `else`
- Nested conditions
- Ternary operator: `x = "even" if num % 2 == 0 else "odd"`

> 💡 *Use Case: Decision-making in programs*

---

### 5. **Loops**
- `for` loop: `for i in range(5):`
- `while` loop: `while x < 10:`
- `break`, `continue`, `pass`
- Looping through strings, lists

> 💡 *Use Case: Processing lists, repeating tasks*

---

### 6. **Strings**
- String creation, quotes (`'`, `"`, `'''`)
- Indexing & slicing: `s[0]`, `s[1:4]`
- Methods: `.upper()`, `.lower()`, `.split()`, `.join()`, `.strip()`
- f-strings: `f"Hello {name}!"`

> 💡 *Use Case: Text processing, formatting output*

---

### 7. **Data Structures: List, Tuple, Set, Dict**

| Structure | Mutability | Ordered | Syntax | Use Case |
|-----------|---|---|---|---|
| **List** `[]` | ✅ Yes | ✅ | `[1,2,3]` | General-purpose collection |
| **Tuple** `()` | ❌ No | ✅ | `(1,2)` | Fixed data (e.g., coordinates) |
| **Set** `{}` | ✅ | ❌ | `{1,2,3}` | Unique items, fast lookup |
| **Dictionary** `{}` | ✅ | ✅ (Python 3.7+) | `{"name": "Ali"}` | Key-value mapping |

> 📌 *Master: list comprehensions, dictionary methods, `.append()`, `.remove()`*

---

## 🟡 Level 2: Functions & Modularity (Intermediate)

### 8. **Functions**
- Defining: `def greet(name):`
- Parameters & arguments
- `return` vs `print`
- Default arguments: `def func(x=5):`
- Keyword arguments: `func(name="Ali", age=25)`

> 💡 *Use Case: Reusable code blocks*

---

### 9. **Scope & Namespaces**
- Local vs Global variables
- `global` keyword
- LEGB rule (Local → Enclosing → Global → Built-in)

> ⚠️ *Avoid global variables when possible*

---

### 10. **Built-in Functions & Modules**
- Common functions: `len()`, `sum()`, `min()`, `max()`, `sorted()`, `enumerate()`, `zip()`
- Importing modules: `import math`, `from datetime import datetime`
- Standard library: `os`, `sys`, `json`, `random`

> 💡 *Use Case: File handling, date/time, randomness*

---

### 11. **File Handling**
- Reading/writing text files: `open("file.txt", "r")`
- Context manager: `with open(...) as f:`
- Working with JSON: `json.load()`, `json.dump()`

> 💡 *Use Case: Save/load data, config files*

---

### 12. **Error Handling**
- `try`, `except`, `else`, `finally`
- Handling specific errors: `ValueError`, `FileNotFoundError`
- Raising errors: `raise ValueError("Invalid input")`

> 💡 *Use Case: Make programs robust*

---

## 🟠 Level 3: Object-Oriented Programming (OOP) (Intermediate → Advanced)

### 13. **Classes & Objects**
- `class Person:`, `__init__()` constructor
- Creating objects: `p = Person("Ali")`
- Instance variables & methods
- `self` explained

> 💡 *Use Case: Modeling real-world entities (User, Car, Document)*

---

### 14. **OOP Principles**

| Concept | Explanation | Example |
|---|---|---|
| **Encapsulation** | Hide data using `_private` or `__very_private` | `self.__salary` |
| **Inheritance** | Child class inherits from parent | `class Student(Person):` |
| **Polymorphism** | Same method, different behavior | `student.walk()` vs `teacher.walk()` |
| **Abstraction** | Hide complex logic | Use methods without knowing internals |

> 💡 *Use Case: Code reuse, clean architecture*

---

### 15. **Special (Dunder) Methods**
- `__str__()` → `str(obj)`
- `__repr__()` → debug representation
- `__len__()` → `len(obj)`
- `__add__()` → `obj1 + obj2`

> 💡 *Make your classes behave like built-in types*

---

### 16. **Properties & Getters/Setters**
- Use `@property` to control access
- Avoid direct attribute access

```python
@property
def age(self):
    return self._age
```

> 💡 *Use Case: Validation, computed properties*

---

## 🔴 Level 4: Advanced Python (Advanced)

### 17. **Modules & Packages**
- Creating your own modules (`mymodule.py`)
- `__init__.py` for packages
- Installing packages: `pip install requests`

> 💡 *Use Case: Organize large projects*

---

### 18. **Functional Programming**
- First-class functions: pass functions as arguments
- `lambda`: `square = lambda x: x**2`
- `map()`, `filter()`, `reduce()`
- List/dict/set comprehensions (advanced)

> 💡 *Use Case: Data transformation, clean code*

---

### 19. **Iterators & Generators**
- `iter()`, `next()`
- `yield` vs `return`
- Memory-efficient: `def fib(): yield ...`

> 💡 *Use Case: Large datasets, streaming data*

---

### 20. **Decorators**
- `@decorator` syntax
- Create your own: timing, logging
- Accept arguments: `@retry(attempts=3)`

```python
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time()-start}s")
        return result
    return wrapper
```

> 💡 *Use Case: Logging, caching, authentication*

---

### 21. **Context Managers**
- `with open() as f:`
- Create your own: `__enter__`, `__exit__`
- `@contextmanager` decorator

> 💡 *Use Case: Safe resource handling (files, DB connections)*

---

### 22. **Exception Customization**
- Define custom exceptions:
  ```python
  class InsufficientFundsError(Exception):
      pass
  ```

> 💡 *Use Case: Domain-specific errors*

---

### 23. **Working with Libraries**
- `requests`: HTTP calls
- `json`, `csv`: Data formats
- `os`, `shutil`: File system
- `datetime`: Date/time
- `collections`: `defaultdict`, `Counter`, `namedtuple`

> 💡 *Use Case: Real-world scripting and automation*

---

### 24. **Virtual Environments & pip**
- `python -m venv myenv`
- `source myenv/bin/activate` (Linux/Mac) or `myenv\Scripts\activate` (Windows)
- `pip install`, `pip freeze > requirements.txt`

> 💡 *Use Case: Isolate project dependencies*

---

## 🔮 Level 5: Next Steps (After Mastery)

### 25. **Popular Libraries to Explore**

| Library | Purpose |
|---|---|
| `numpy` | Numerical computing |
| `pandas` | Data analysis |
| `matplotlib/seaborn` | Data visualization |
| `requests` | Web APIs |
| `flask/fastapi` | Web development |
| `pytest` | Testing |
| `jupyter` | Interactive notebooks |

---

### 26. **Best Practices**
- PEP 8 (code style)
- Docstrings: `"""Explain function here"""`
- Type hints: `def func(x: int) -> str:`
- Writing clean, readable code
- Unit testing with `unittest` or `pytest`

---

### 27. **Project Ideas to Practice**
1. **To-Do List App** (CLI) → Use lists, files
2. **Contact Book** → Use dictionaries, JSON
3. **Calculator** → Functions, error handling
4. **Web Scraper** → `requests`, `BeautifulSoup`
5. **Blog System** → Classes, file handling
6. **Quiz Game** → OOP, files, loops

---

## 📚 Learning Resources

| Resource | Link |
|---|---|
| **Official Python Docs** | [https://docs.python.org](https://docs.python.org) |
| **Real Python (Tutorials)** | [https://realpython.com](https://realpython.com) |
| **Automate the Boring Stuff** | [https://automatetheboringstuff.com](https://automatetheboringstuff.com) |
| **Corey Schafer (YouTube)** | [https://youtube.com/c/Coreyms](https://youtube.com/c/Coreyms) |
| **W3Schools Python** | [https://w3schools.com/python](https://w3schools.com/python) |
| **LeetCode / HackerRank** | Practice coding problems |

---

## 🗺️ Learning Plan (8-Week Suggestion)

| Week | Focus |
|---|---|
| 1-2 | Basics: variables, loops, strings, lists |
| 3 | Functions, file handling, error handling |
| 4 | Dictionaries, sets, comprehensions |
| 5 | OOP: classes, inheritance, methods |
| 6 | Advanced: decorators, generators, context managers |
| 7 | Projects & libraries (`requests`, `json`, `os`) |
| 8 | Virtual envs, best practices, type hints |
