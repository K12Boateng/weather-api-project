# tests/test_weather.py
import json
from unittest.mock import patch, Mock
import pytest
from src import weather

SAMPLE_RESPONSE = {
    "weather": [{"description": "clear sky"}],
    "main": {"temp": 21.3, "feels_like": 20.0},
    "name": "Testville"
}

class DummyResp:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json = json_data or {}

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise Exception("HTTP error: status " + str(self.status_code))

    def json(self):
        return self._json

@patch("src.weather.requests.get")
def test_fetch_weather_success(mock_get):
    mock_get.return_value = DummyResp(200, SAMPLE_RESPONSE)
    result = weather.fetch_weather("Testville", api_key="fake")
    assert result["name"] == "Testville"
    assert result["weather"][0]["description"] == "clear sky"

@patch("src.weather.requests.get")
def test_fetch_weather_api_error(mock_get):
    mock_get.side_effect = Exception("network down")
    with pytest.raises(RuntimeError):
        weather.fetch_weather("Nowhere", api_key="fake")
