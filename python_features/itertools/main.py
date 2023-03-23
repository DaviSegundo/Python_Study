def main() -> None:
    countries = ("Germany", "France", "Italy", "Spain", "Portugal", "Greece")
    country_iter = iter(countries)

    # print(next(country_iter))
    # print(next(country_iter))
    # print(next(country_iter))
    # print(next(country_iter))
    # print(next(country_iter))

    for country in countries:
        print(country)


if __name__ == "__main__":
    main()