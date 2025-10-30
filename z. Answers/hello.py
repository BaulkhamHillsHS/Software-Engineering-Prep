def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    try:
        name = input("What's your name? ")
        print(greet(name))
    except Exception as e:
        print(f"error: {e}")
