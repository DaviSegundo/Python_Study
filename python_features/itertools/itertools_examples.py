import itertools


def main() -> None:
    # for i in itertools.accumulate(range(1, 11)):
    #     print(i)

    # items_list = ["a", "b", "c"]
    # perm_list = itertools.permutations(items_list)
    # for perm in perm_list:
    #     print(perm)

    # items_list = ["a", "b", "c"]
    # perm_list = itertools.combinations(items_list, 2)
    # for perm in perm_list:
    #     print(perm)

    # items_list = ["a", "b", "c"]
    # more_items_list = ["d", "e"]
    # two_list = list(itertools.chain(items_list, more_items_list))
    # print(two_list)
    # print(list(itertools.combinations(two_list, 4)))

    print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(10))))
    print(list(itertools.takewhile(lambda x: x != 5, range(10))))
    print(list(itertools.starmap(lambda x, y: x * y, [(2, 6), (8, 4), (5, 3)])))


if __name__ == "__main__":
    main()