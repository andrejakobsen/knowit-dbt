from abc import ABC, abstractclassmethod
import json
import logging
import os

import requests

class APIExtractor(ABC):
    @abstractclassmethod
    def fetch_json_data(self) -> dict:
        pass

    @abstractclassmethod
    def fetch_resource_results(self) -> list:
        pass

    def store_results(self) -> None:
        """Store the list `data` as a json file with name `name`."""
        with open(f"{DATA_PATH}/{self.name}.json", "w") as file:
            json.dump(self.data, file, indent=6)
            logging.info(f"Finished storing {name} in {DATA_PATH}")
        