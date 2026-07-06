import json
import os
import requests


INTENSITY_URL = "https://api.carbonintensity.org.uk/intensity"
GENERATION_URL = "https://api.carbonintensity.org.uk/generation"

OUTPUT_DIR = "data/raw/carbon"


def get_carbon_data(url):
    response = requests.get(url, timeout=30)
    # if the API returned error (e.g. 404, 500), script will stop and print error message
    response.raise_for_status()
    return response.json()


def main():
    intensity_data = get_carbon_data(INTENSITY_URL)
    generation_data = get_carbon_data(GENERATION_URL)

    print(intensity_data)
    print(generation_data)


if __name__ == "__main__":
    main()
