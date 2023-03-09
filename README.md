# Data Engineering at Knowit
I have decided to make one fact table called `fct_character_appearances` that gives the appearance of a Star Wars character in a given movie, ordered by the date of appearance. There are also two dimensional tables, `dim_characters` and `dim_films`, that provide information about the character and the movie they appear in, respectively.

1. We will be using a `Makefile` in order to simplify all the commands.
    For Windows you may use [GnuWin](https://gnuwin32.sourceforge.net/install.html) and on Mac you can install make with [Homebrew](https://formulae.brew.sh/formula/make) by running
    ```
    brew install make
    ```

1. To run the code make sure to have Python already installed.
    Create the virtual Python environment by running
    ```
    make venv
    ```
    Then activate the newly created environment. On Mac or Linux, you can use
    ```
    source venv/bin/activate
    ```

1. We are now ready to execute the whole ELT process using
    ```
    make elt
    ```
    This will fetch raw data from SWAPI, load it to `swapi.db` and create a small datawarehouse in dbt.
    You may also see the dbt documentation by running
    ```
    make docs
    ```
    This will open your browser with dbt's documentation and lineage graph.
    
1. If you wish to clean up the virtual environment and all the data files, you can run
    ```
    make clean
    ```

## Potential Improvements
1. Write integration/unit tests to ensure the Python scripts behave as expected and dbt tests that check for null and unique values.

1. Dockerize the project for easier deployment and adding CI/CD in GitHub.

1. Use an EL and DataOps tool such as Meltano and use a stable version of DuckDB.
