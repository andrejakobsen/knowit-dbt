# knowit-dbt
Solution to Knowit's data engineering exercise. I have decided to make one fact table called `fct_character_appearances` that gives the appearance of a Star Wars character in a given movie, ordered by the date of appearance. There are also two dimensional tables, `dim_characters` and `dim_films`, that provide information about the character and the movie they appear in, respectively.

1. We will be using a `Makefile` in order to simplify all the commands.
    For Windows you may use [GnuWin](https://gnuwin32.sourceforge.net/install.html) and on Mac you can use [Homebrew](https://formulae.brew.sh/formula/make) by running
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
    This will open your browser that provides documentation and a lineage graph.