def add(a: float, b: float) -> float:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b


if __name__ == "__main__":
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f"sum: {add(a, b)}")
        try:
            print(f"quotient: {divide(a, b)}")
        except ValueError:
            print("quotient: undefined")
    except Exception as e:
        print(f"error: {e}")
