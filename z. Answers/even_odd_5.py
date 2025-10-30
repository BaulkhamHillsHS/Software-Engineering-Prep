def label_even_odd(n: int) -> str:
    return "even" if n % 2 == 0 else "odd"


if __name__ == "__main__":
    for i in range(5):
        n = int(input(f"Number {i+1}: "))
        print(label_even_odd(n))
