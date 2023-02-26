FROM python:latest

WORKDIR /knowit-dbt

COPY ./requirements.txt /knowit-dbt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /knowit-dbt
