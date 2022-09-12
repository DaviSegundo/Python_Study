import datetime


def main():
    today = datetime.datetime.now()
    print(f"Simple date printing: {today}")
    print(f"{today:%Y-%m-%d %H:%M:%S}")
    print(f"Today is: {today:%A, %B %d, %Y}")
    print(f"Today is: {today:%x}")


if __name__ == "__main__":
    main()
