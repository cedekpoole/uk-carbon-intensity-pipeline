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


def validate_intensity_response(data):
    if not data:
        raise ValueError("Intensity response returned no data")
    for line in data["data"]:
        if "from" not in line or "to" not in line or "intensity" not in line:
            raise ValueError("Intensity response missing required fields")


def validate_generation_response(data):
    if not data:
        raise ValueError("Generation response returned no data")
    for line in data["data"]:
        if "from" not in line or "to" not in line or "generationmix" not in line:
            raise ValueError("Generation response missing required fields")


def main():
    try:
        intensity_data = get_carbon_data(INTENSITY_URL)
        generation_data = get_carbon_data(GENERATION_URL)

        validate_intensity_response(intensity_data)
        validate_generation_response(generation_data)

        print(intensity_data)
        print(generation_data)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except ValueError as ve:
        print(f"Validation error: {ve}")


if __name__ == "__main__":
    main()
