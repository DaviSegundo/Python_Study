import json
from bs4 import BeautifulSoup
from xml_adapter import XMLConfig
from experiment import Experiment


def main() -> None:
    # with open(
    #     "./code_organization/adapter_pattern/config.json", encoding="utf8"
    # ) as file:
    #     config = json.load(file)
    # experiment = Experiment(config)
    # experiment.run()
    with open(
        "./code_organization/adapter_pattern/config.xml", encoding="utf8"
    ) as file:
        config = file.read()
    bs = BeautifulSoup(config, "xml")
    adapter = XMLConfig(bs)
    experiment = Experiment(adapter)
    experiment.run()


if __name__ == "__main__":
    main()
