def main():
    num = 800

    # normal number
    print(f"The number is {num}")

    # hex number
    print(f"The number is {num:x}")

    # binary number
    print(f"The number is {num:b}")

    # sci number
    print(f"The number is {num:e}")

    # total len number
    print(f"The number is {num:06}")

    # float formatting
    print(f"The number is {100.23459786:.2f}")

    # large number formatting
    print(f"The number is ${44000000000:,.2f}")

    # percentage formatting
    print(f"The number is {0.34567:.2%}")


if __name__ == "__main__":
    main()
