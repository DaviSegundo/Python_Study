def lunh_checksum(number: str) -> bool:
    def digits_of(nr: str) -> list[int]:
        return [int(d) for d in nr]

    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0


def is_eligible_for_bonus(
    contracts_landed: int, hours_worked: int, is_family: bool
) -> bool:
    if is_family:
        return True
    if contracts_landed > 0 and hours_worked > 40:
        return True
    return False


def main():

    print(lunh_checksum("1249190007575069"))


if __name__ == "__main__":
    main()
