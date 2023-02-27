venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

clean:
	rm -rf venv

clean-dw:
	rm sw_warehouse.db
	rm sw_warehouse.db.wal

extract:
	python ./extract/fetch_and_store_sw_data.py 

load: extract
	python ./load/load_raw_sw_data.py

transform: load

