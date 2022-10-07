import os

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")
BASE_DIR = os.environ.get("BASE_DIR")
DATASET_DIR_LECT_06 = os.getenv("DATASET_DIR_LECT_06", "/Users/macbook/Documents/GitHub/de2022_last/lect_06/data_lake/landing/src1/sales/dags/datasets")
