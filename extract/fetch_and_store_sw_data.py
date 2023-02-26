import json
import logging
import os

import requests

logging.basicConfig(level=logging.INFO)

ROOT_URL = "https://swapi.dev/api/"
DATA_PATH = "./data"


def main():
    """Retrieve and store all raw data for the Star Wars API (SWAPI)."""
    if not os.path.isdir(DATA_PATH):
        logging.info(f"Creating directory: {DATA_PATH}")
        os.mkdir(DATA_PATH)
    resources = fetch_json_data(ROOT_URL)
    for resource_name, url in resources.items():
        resource_results = fetch_resource_results(url)
        store_results(resource_results, resource_name)
    logging.info("Finished fetching and storing all data for the SWAPI")


def fetch_json_data(url: str) -> dict:
    """Fetches json data from a given url and raises an exception if
    the response does not give status code `200` ('OK').
    """
    response = requests.get(url)
    status_code = response.status_code
    if status_code != 200:
        logging.error(f"Recieved status code {status_code} from {url}")
        raise Exception(status_code)
    return response.json()


def fetch_resource_results(url: str) -> list:
    """Recursively fetches the results from all pages of a given url and
    returns it as a list. Used for resources with pagination.
    """
    results = []
    logging.info(f"Fetching results from all pages in {url}")

    def fetch_and_append_page_results(url: str):
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


def store_results(data: list, name: str) -> None:
    """Store the list `data` as a json file with name `name`."""
    with open(f"{DATA_PATH}/{name}.json", "w") as file:
        json.dump(data, file, indent=6)
        logging.info(f"Finished storing {name} in {DATA_PATH}")


if __name__ == "__main__":
    main()
