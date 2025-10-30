# 🔁 Python: Loops and Iteration

## 🎯 Learning Intentions
- Repeat code using `for` and `while` loops
- Use loop control to manage repetition safely
- Avoid infinite loops by updating variables correctly

---

### 🔢 1. The `for` Loop
```python
for i in range(1, 6):
    print(i)
```

---

### 🍎 2. Looping Through Lists
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

### ⏳ 3. The `while` Loop
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

---

### ⚠️ 4. Common Mistakes
```python
# Infinite loop example
count = 1
while count <= 5:
    print(count)
# Missing count += 1 causes infinite loop
```

✅ Always ensure your loop **can end**.

---

### 🚫 5. Break and Continue
```python
# break example
for num in range(1, 10):
    if num == 5:
        break
    print(num)

# continue example
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
```

---

### 🧮 6. Nested Loops
```python
for x in range(1, 4):
    for y in range(1, 3):
        print("x =", x, "y =", y)
```

---

### 🧩 7. Challenge
Ask the user for a word and display each letter on a new line.

```python
word = input("Enter a word: ")
for letter in word:
    print(letter)
```

---

### 🧠 Reflection
- How does a `for` loop differ from a `while` loop?  
- When might you use `break` or `continue`?  
- What causes an infinite loop?
