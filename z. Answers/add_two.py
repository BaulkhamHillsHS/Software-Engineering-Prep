def add(a: float, b: float) -> float:
    return a + b


if __name__ == "__main__":
    a = float(input("A: "))
    b = float(input("B: "))
    print(f"sum: {add(a,b)}")
