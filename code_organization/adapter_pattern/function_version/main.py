import json
from functools import partial

from bs4 import BeautifulSoup

from experiment import Experiment
from xml_adapter import get_from_bs


def main() -> None:
    # with open(
    #     "./code_organization/adapter_pattern/function_version/config.json",
    #     encoding="utf8",
    # ) as file:
    #     config = json.load(file)
    # experiment = Experiment(config.get)
    # experiment.run()
    with open(
        "./code_organization/adapter_pattern/function_version/config.xml",
        encoding="utf8",
    ) as file:
        config = file.read()
    bs = BeautifulSoup(config, "xml")
    get_from_bs_adapter = partial(get_from_bs, bs)
    experiment = Experiment(get_from_bs_adapter)
    experiment.run()


if __name__ == "__main__":
    main()
