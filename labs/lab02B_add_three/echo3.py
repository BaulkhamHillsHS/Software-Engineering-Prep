def three_lines(word: str) -> list[str]:
    return [word] * 3


if __name__ == "__main__":
    w = input("Word: ")
    for line in three_lines(w):
        print(line)
