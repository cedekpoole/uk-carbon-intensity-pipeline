import pytest

from fetch_carbon import validate_generation_response, validate_intensity_response


FAKE_INTENSITY_RESPONSE = {
    "data": [
        {
            "from": "2026-07-04T16:00Z",
            "to": "2026-07-04T16:30Z",
            "intensity": {
                "forecast": 43,
                "actual": 43,
                "index": "low",
            },
        }
    ]
}


FAKE_GENERATION_RESPONSE = {
    "data": {
        "from": "2026-07-04T16:00Z",
        "to": "2026-07-04T16:30Z",
        "generationmix": [
            {"fuel": "wind", "perc": 46.9},
            {"fuel": "solar", "perc": 20.2},
        ],
    }
}


def test_validate_intensity_response_accepts_valid_payload():
    validate_intensity_response(FAKE_INTENSITY_RESPONSE)


def test_validate_intensity_response_rejects_missing_data():
    with pytest.raises(ValueError):
        validate_intensity_response({})


def test_validate_generation_response_accepts_valid_payload():
    validate_generation_response(FAKE_GENERATION_RESPONSE)


def test_validate_generation_response_rejects_missing_data():
    with pytest.raises(ValueError):
        validate_generation_response({})
