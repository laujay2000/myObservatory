from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import re


class ForecastPage(BasePage):
    # 元素定位器
    # 第9天天气预报的通用定位器（假设的ID和XPath，需根据实际应用调整）
    DAY_9_CONTAINER = (AppiumBy.XPATH, "//*[@resource-id='gov.hko.weather:id/forecast_days']/android.view.ViewGroup[9]")
    DAY_9_DATE = (AppiumBy.XPATH,
                  "//*[@resource-id='gov.hko.weather:id/forecast_days']/android.view.ViewGroup[9]//*[@resource-id='gov.hko.weather:id/date']")
    DAY_9_WEATHER = (AppiumBy.XPATH,
                     "//*[@resource-id='gov.hko.weather:id/forecast_days']/android.view.ViewGroup[9]//*[@resource-id='gov.hko.weather:id/weather_condition']")
    DAY_9_TEMP = (AppiumBy.XPATH,
                  "//*[@resource-id='gov.hko.weather:id/forecast_days']/android.view.ViewGroup[9]//*[@resource-id='gov.hko.weather:id/temperature']")
    DAY_9_HUMIDITY = (AppiumBy.XPATH,
                      "//*[@resource-id='gov.hko.weather:id/forecast_days']/android.view.ViewGroup[9]//*[@resource-id='gov.hko.weather:id/humidity']")
    DAY_9_WIND = (AppiumBy.XPATH,
                  "//*[@resource-id='gov.hko.weather:id/forecast_days']/android.view.ViewGroup[9]//*[@resource-id='gov.hko.weather:id/wind']")
    DAY_9_UV_INDEX = (AppiumBy.XPATH,
                      "//*[@resource-id='gov.hko.weather:id/forecast_days']/android.view.ViewGroup[9]//*[@resource-id='gov.hko.weather:id/uv_index']")

    # 切换摄氏度/华氏度的按钮
    TEMP_UNIT_SWITCH = (AppiumBy.ID, "gov.hko.weather:id/temp_unit_switch")

    # 刷新按钮
    REFRESH_BUTTON = (AppiumBy.ID, "gov.hko.weather:id/refresh_button")

    # 语言切换按钮
    LANGUAGE_SWITCH = (AppiumBy.ID, "gov.hko.weather:id/language_switch")

    def __init__(self, driver):
        super().__init__(driver)

    def get_day_9_date(self):
        """获取第9天的日期"""
        self.scroll_to_element(self.DAY_9_CONTAINER)
        return self.get_element_text(self.DAY_9_DATE)

    def get_day_9_weather_condition(self):
        """获取第9天的天气状况"""
        self.scroll_to_element(self.DAY_9_CONTAINER)
        return self.get_element_text(self.DAY_9_WEATHER)

    def get_day_9_temperature(self):
        """获取第9天的温度"""
        self.scroll_to_element(self.DAY_9_CONTAINER)
        temp_text = self.get_element_text(self.DAY_9_TEMP)

        # 提取温度数值
        match = re.search(r'(\d+)-(\d+)', temp_text)
        if match:
            return {
                'min': int(match.group(1)),
                'max': int(match.group(2)),
                'unit': 'C' if '°C' in temp_text else 'F'
            }
        return None

    def get_day_9_humidity(self):
        """获取第9天的湿度"""
        self.scroll_to_element(self.DAY_9_CONTAINER)
        humidity_text = self.get_element_text(self.DAY_9_HUMIDITY)

        # 提取湿度数值
        match = re.search(r'(\d+)-(\d+)%', humidity_text)
        if match:
            return {
                'min': int(match.group(1)),
                'max': int(match.group(2))
            }
        return None

    def get_day_9_wind(self):
        """获取第9天的风向风力"""
        self.scroll_to_element(self.DAY_9_CONTAINER)
        return self.get_element_text(self.DAY_9_WIND)

    def get_day_9_uv_index(self):
        """获取第9天的紫外线指数"""
        self.scroll_to_element(self.DAY_9_CONTAINER)
        uv_text = self.get_element_text(self.DAY_9_UV_INDEX)

        # 提取UV指数数值
        match = re.search(r'(\d+)', uv_text)
        if match:
            return int(match.group(1))
        return None

    def switch_temperature_unit(self):
        """切换温度单位（摄氏度/华氏度）"""
        self.click_element(self.TEMP_UNIT_SWITCH)

    def refresh_forecast(self):
        """刷新天气预报数据"""
        self.click_element(self.REFRESH_BUTTON)

    def switch_language(self):
        """切换语言（假设切换中英文）"""
        self.click_element(self.LANGUAGE_SWITCH)

    def is_forecast_displayed(self):
        """验证天气预报是否显示"""
        return self.is_element_displayed(self.DAY_9_CONTAINER)
