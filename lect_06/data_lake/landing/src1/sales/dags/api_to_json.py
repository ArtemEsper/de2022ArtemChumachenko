import argparse
import os
import json
import requests
from requests.exceptions import HTTPError

import config
from datetime import datetime


def get_date(fetch_date):
    return datetime.strptime(fetch_date, '%Y-%m-%d').date()


def get_sales(fetch_date: str):
    date = get_date(fetch_date)
    total_results = []
    data = {}
    for page_num in range(1, 5):
        url = config.API_URL + "sales?date=" + str(date) + "&page=" + str(page_num)
        try:
            response = requests.get(
                url=url,
                headers={'Authorization': config.AUTH_TOKEN}
            )
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            # print('Success!')
            data = response.json()
            total_results = [*total_results, *data]
            # total_results = total_results + [data]

    return total_results


def get_file_path(fetch_date: str):
    date = get_date(fetch_date)
    filename = "sales_{}.json".format(date)
    raw_dir = os.path.join(config.DATASET_DIR_LECT_06, "raw", "sales")
    # create the parent dir if not exist
    os.makedirs(raw_dir, exist_ok=True)
    if os.path.isfile(raw_dir):
        os.remove(raw_dir)
    return os.path.join(raw_dir, filename)


def save_to_disk(json_content, date: str):
    pathname = get_file_path(date)
    with open(pathname, "w") as f:
        json.dump(json_content, f)


def main(fetch_date: str):
    total_results = get_sales(fetch_date)
    save_to_disk(total_results, fetch_date)

    return {
               "message": "Data retrieved successfully from API",
           }, 201


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, type=str)
    args = parser.parse_args()
    main(args.date)
