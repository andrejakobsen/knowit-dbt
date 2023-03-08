import json
import logging
import os

from extractor import APIExtractor

import requests

def SWAPIExtractor(APIExtractor):
    def __init__(self):
        self.session = requests.Session()

    ROOT_URL = "https://swapi.dev/api/"
    def __init__(self, url: str = ROOT_URL, name: str) -> None:
        self.url = url
        self.name = name
        self.

    def fetch_json_data(self) -> dict:
        """Fetches json data from a given url and raises an exception if
        the response does not give status code `200` ('OK').
        """
        response = requests.get(self.url)
        status_code = response.status_code
        if status_code != 200:
            logging.error(f"Recieved status code {status_code} from {self.url}")
            raise Exception(status_code)
        return response.json()


    def fetch_resource_results(self) -> list:
        """Recursively fetches the results from all pages of a given url and
        returns it as a list. Used for resources with pagination.
        """
        results = []
        logging.info(f"Fetching results from all pages in {self.url}")

        def fetch_and_append_page_results(self):
            data = fetch_json_data(url)
            page_results = data["results"]
            next_page = data["next"]
            for result in page_results:
                results.append(result)
            if not next_page:
                return
            return fetch_and_append_page_results(next_page)

        fetch_and_append_page_results(url)
        logging.info(f"Sucessfully fetched all results from {url}")
        return results


    def store_results(self -> None:
        """Store the list `data` as a json file with name `name`."""
        with open(f"{DATA_PATH}/{name}.json", "w") as file:
            json.dump(data, file, indent=6)
            logging.info(f"Finished storing {name} in {DATA_PATH}")
