"""
Layer of persistence. Save content to outer world here.
"""
import json
import os


def save_to_disk(json_content, path):
    # create the parent dir if not exist
    os.makedirs(path, exist_ok=True)

    if os.path.isfile(path):
        os.remove(path)
    # join path and filename
    pathname = os.path.join(path, 'sales_2022-08-09.json')
    with open(pathname, "w") as f:
        json.dump(json_content, f)


if __name__ == "__main__":
    save_to_disk()
