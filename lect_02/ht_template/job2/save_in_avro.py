"""
Convert giles from raw json to avro format.
"""
import json
import os
from fastavro import writer, parse_schema


def avro(raw_dir, stg_dir):
    # create the parent dir if not exist
    os.makedirs(stg_dir, exist_ok=True)
    # join path and filename
    raw_path = os.path.join(raw_dir, 'sales_2022-08-09.json')
    stg_path = os.path.join(stg_dir, 'sales_2022-08-09.avro')
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


if __name__ == "__main__":
    avro()