"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer for job2
"""
import os

from flask import Flask, request
from flask import typing as flask_typing

from lect_02.ht_template.job2 import save_in_avro

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
     Controller that accepts command via HTTP and
     trigger business logic layer
     Proposed POST body in JSON:
     {
       "data: "2022-08-09",
       "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"
     }
     """
    input_data: dict = request.json
    save_in_avro.avro(input_data['raw_dir'], input_data['stg_dir'])
    return {
               "message": "Data retrieved successfully from API",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)
