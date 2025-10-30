# 🧍‍♀️ Python: User Input and Data Types

## 🎯 Learning Intentions
- Use `input()` to get data from users
- Understand the difference between strings, integers, and floats
- Convert between data types for calculations

---

### 📥 1. Collecting User Input
```python
name = input("What is your name? ")
print("Welcome,", name)
```

---

### 🔢 2. Input and Calculations
```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
total = int(num1) + int(num2)
print("The total is:", total)
```

---

### 🧮 3. Data Types Overview

| Type | Example | Description |
|------|----------|-------------|
| `str` | `"Caroline"` | Text |
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `bool` | `True` | True or False |

Check a variable’s type:
```python
x = 3.14
print(type(x))
```

---

### 📊 4. Input → Process → Output
```python
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
total_pay = hours * rate

print("You earned $", total_pay)
```

---

### 🧠 Reflection
- Why do we convert user input using `int()` or `float()`?  
- What is the difference between `str` and `int`?  
- What happens if you forget to convert before adding numbers?
