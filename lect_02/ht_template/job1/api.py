import os

import requests

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")


def get_sales(date: str):
    total_results = []
    for page_num in range(1, 5):
        url = API_URL + "sales?date=" + str(date) + "&page=" + str(page_num)
        response = requests.get(
            url=url,
            headers={'Authorization': AUTH_TOKEN}
        )
        data = response.json()
        total_results = total_results + data

    return total_results


if __name__ == "__main__":
    get_sales()
