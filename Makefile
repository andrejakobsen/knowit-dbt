venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

clean:
	rm -rf venv
	rm -rf data
	rm *.db*

elt: t

e:
	@echo "Extracting SWAPI data if it does not exist."
	python ./extract/fetch_and_store_sw_data.py

l: e
	@echo "Loading SWAPI data to duckdb."
	python ./load/load_raw_sw_data.py

t: l
	@echo "Transforming SWAPI data with dbt."
	cd transform; \
	dbt build

docs: t
	@echo "Generating and opening dbt docs."
	cd transform; \
	dbt docs generate; \
	dbt docs serve
