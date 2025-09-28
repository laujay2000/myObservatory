import requests
from config.config import HKO_API_BASE_URL, API_PARAMS
import json


class HKOApiClient:
    def __init__(self):
        self.base_url = HKO_API_BASE_URL
        self.params = API_PARAMS

    def get_nine_day_forecast(self):
        """获取九天天气预报API数据"""
        try:
            response = requests.get(self.base_url, params=self.params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API请求失败: {e}")
            return None

    def extract_humidity_for_day_after_tomorrow(self, forecast_data):
        """提取后天的湿度数据"""
        try:
            # 获取天气预报数据
            weather_data = forecast_data.get('weatherForecast', [])

            # 找到后天的数据
            from datetime import datetime, timedelta
            day_after_tomorrow = (datetime.now() + timedelta(days=2)).strftime('%Y%m%d')

            for day_data in weather_data:
                if day_data.get('forecastDate') == day_after_tomorrow:
                    return day_data.get('forecastMinrh', {}).get('value'), day_data.get('forecastMaxrh', {}).get(
                        'value')

            return None, None
        except Exception as e:
            print(f"提取湿度数据失败: {e}")
            return None, None