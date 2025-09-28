import json
from datetime import datetime, timedelta


def extract_humidity_range(response):
    try:
        response_data = json.loads(response)
    except json.JSONDecodeError:
        print("Error: response is not json format")
        return None

    today = datetime.now()
    day_after_tomorrow = today + timedelta(days=2)
    target_date = day_after_tomorrow.strftime("%Y%m%d")
    print(f"current date：{today.strftime('%Y%m%d')}")
    print(f"next tomorrow date：{target_date}")

    hourly_forecasts = response_data.get("HourlyWeatherForecast", [])
    if not hourly_forecasts:
        print("Error: not found hourly forecast data（HourlyWeatherForecast）")
        return None

# filter humidity data
    humidity_values = []
    for forecast in hourly_forecasts:
        forecast_date = forecast.get("ForecastHour", "")[:8]
        if forecast_date == target_date and "ForecastRelativeHumidity" in forecast:
            humidity = forecast["ForecastRelativeHumidity"]
            humidity_values.append(humidity)

    if not humidity_values:
        print(f"Error: not found {target_date} data")
        return None

    min_humidity = round(min(humidity_values), 1)
    max_humidity = round(max(humidity_values), 1)
    humidity_range = f"{min_humidity}-{max_humidity}"

    print(f"\n{target_date} relative humidity range：{humidity_range}")
    return humidity_range

if __name__ == '__main__':
    response = '''{
    "LastModified": "20250923101319",
    "StationCode": "HKO",
    "Latitude": 22.302,
    "Longitude": 114.174,
    "ModelTime": "2025092800",
    "HourlyWeatherForecast": [
        {"ForecastHour": "2025093000", "ForecastRelativeHumidity": 82.8},
        {"ForecastHour": "2025093009", "ForecastRelativeHumidity": 88.1},
        {"ForecastHour": "2025093013", "ForecastRelativeHumidity": 80.3},
        {"ForecastHour": "2025093023", "ForecastRelativeHumidity": 84.2}
    ]
}'''
    extract_humidity_range(response)