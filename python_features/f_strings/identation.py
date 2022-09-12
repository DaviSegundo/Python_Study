def main():
    for number in range(8, 12):
        print(f"The number is {number:6}.")

    greet = "Hi"

    # insert spaces before the str
    print(f"{greet:>10}")
    print(f"{greet:^10}")
    print(f"{greet:<10}")


if __name__ == "__main__":
    main()
