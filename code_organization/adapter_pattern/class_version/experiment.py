from typing import Any, Dict

from config_access import Config


class Experiment:
    def __init__(self, config: Config) -> None:
        self.config = config

    def load_data(self) -> None:
        data_path = self.config.get("data_path")
        if not data_path:
            raise ValueError("No data path specified.")
        print(f"Loading data from {data_path}.")

    def setup_log(self) -> None:
        log_path = self.config.get("log_path")
        if not log_path:
            raise ValueError("No log path specified.")
        print(f"Logging to {log_path}.")

    def train_model(self) -> None:
        epoch_count = self.config.get("epoch_count")
        if not epoch_count:
            raise ValueError("No epoch_count specified.")
        print(f"Trainig for {epoch_count} epochs.")

    def run(self) -> None:
        self.load_data()
        self.setup_log()
        self.train_model()
