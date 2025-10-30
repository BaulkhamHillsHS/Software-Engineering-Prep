def add3(a: float, b: float, c: float) -> float:
    return a + b + c


if __name__ == "__main__":
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    print(f"sum: {add3(a,b,c)}")
