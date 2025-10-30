# ⚖️ Python: Conditional Statements and Boolean Logic

## 🎯 Learning Intentions
- Make decisions using `if`, `elif`, and `else`
- Use comparison and logical operators
- Write programs that respond to user input

---

### 🤔 1. Basic `if` Statement
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to vote.")
```

---

### 🔄 2. Adding `else`
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to vote.")
else:
    print("Sorry, you are too young to vote.")
```

---

### 🧮 3. Using `elif`
```python
mark = int(input("Enter your mark: "))

if mark >= 90:
    print("Excellent! A grade.")
elif mark >= 70:
    print("Good job! B grade.")
elif mark >= 50:
    print("You passed.")
else:
    print("Sorry, you failed.")
```

---

### ⚙️ 4. Comparison Operators

| Operator | Meaning | Example |
|-----------|----------|----------|
| `==` | equal to | `5 == 5` |
| `!=` | not equal | `5 != 3` |
| `>` | greater than | `7 > 2` |
| `<` | less than | `2 < 5` |
| `>=` | greater or equal | `8 >= 8` |
| `<=` | less or equal | `3 <= 4` |

---

### 💡 5. Logical Operators

| Operator | Example | Meaning |
|-----------|----------|----------|
| `and` | `age >= 18 and age < 65` | Both must be true |
| `or` | `day == "Saturday" or day == "Sunday"` | One must be true |
| `not` | `not raining` | Reverses a condition |

---

### 🧩 6. Nested `if`
```python
age = int(input("Enter your age: "))
has_Ls = input("Do you have your learner’s licence? (yes/no): ")

if age >= 17:
    if has_Ls == "yes":
        print("You can apply for your provisional licence!")
    else:
        print("You need to get your learner’s licence first.")
else:
    print("You are too young to apply.")
```

---

### 🧠 Reflection
- What is the difference between `if`, `elif`, and `else`?  
- When should you use `and` vs `or`?  
- Why is indentation so important in Python?
