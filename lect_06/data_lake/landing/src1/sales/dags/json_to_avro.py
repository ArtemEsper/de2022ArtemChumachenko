import os
import json
import argparse
from datetime import datetime
from fastavro import writer, parse_schema
import config


def get_date(fetch_date):
    return datetime.strptime(fetch_date, '%Y-%m-%d').date()


def get_raw_file_path(date: str):
    filename = "sales_{}.json".format(date)
    raw_dir = os.path.join(config.DATASET_DIR_LECT_06, "raw", "sales")
    # create the parent dir if not exist
    os.makedirs(raw_dir, exist_ok=True)
    if os.path.isfile(raw_dir):
        os.remove(raw_dir)
    return os.path.join(raw_dir, filename)


def get_stg_file_path(date: str):
    filename = "sales_{}.avro".format(date)
    stg_dir = os.path.join(config.DATASET_DIR_LECT_06, "stg", "sales")
    # create the parent dir if not exist
    os.makedirs(stg_dir, exist_ok=True)
    if os.path.isfile(stg_dir):
        os.remove(stg_dir)
    return os.path.join(stg_dir, filename)


def avro(fetch_date: str):
    date = get_date(fetch_date)
    raw_path = get_raw_file_path(date)
    stg_path = get_stg_file_path(date)
    schema = {
        "namespace": "sales_2022-08-09.avro",
        "type": "record",
        "name": "store",
        "fields": [
            {"name": "client", "type": "string"},
            {"name": "purchase_date", "type": "string"},
            {"name": "product", "type": "string"},
            {"name": "price", "type": "int"}
        ]
    }

    with open(raw_path, "r") as f:
        json_export = json.loads(f.read())

    with open(stg_path, 'wb') as avro_file:
        writer(avro_file, parse_schema(schema), json_export)


def main(fetch_date: str):
    avro(fetch_date)

    return {
               "message": "Data saved successfully in avro format",
           }, 201


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, type=str)
    args = parser.parse_args()
    main(args.date)
