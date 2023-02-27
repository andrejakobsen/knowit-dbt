import os

import duckdb

DATA_PATH = "../data"


def main():
    """Creates a duckdb database and stores all raw `.json` files that
    have been extracted to `data`."""
    # use existing persistent storage or create a new one
    con = duckdb.connect("sw_warehouse.db")
    resources = get_resource_names()
    for resource in resources:
        con.execute(
            f"""
            CREATE OR REPLACE TABLE {resource} AS
            SELECT
                *
            FROM
                read_json_auto('{DATA_PATH}/{resource}.json');
        """
        )
        con.table(resource).show()


def get_resource_names():
    os.chdir("load")
    return [file_name.split(".")[0] for file_name in os.listdir(DATA_PATH)]


if __name__ == "__main__":
    main()
