from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.nine_day_forecast_locators import NineDayForecastLocators
import time


class NineDayForecastPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.locators = NineDayForecastLocators

    def navigate_to_nine_day_forecast(self):
        """navigate to nine day forcast page"""
        try:
            # open menu
            menu_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.MENU_BUTTON)
            )
            menu_btn.click()

            # select option of nine forecast
            forecast_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.NINE_DAY_FORECAST_OPTION)
            )
            forecast_option.click()

            # wait for page loading
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.locators.FORECAST_TITLE)
            )
            return True
        except Exception as e:
            print(f"failed to navigate to nine day forecast: {e}")
            return False

    def get_ninth_day_forecast(self):
        """get the ninth day forecast"""
        try:
            # scroll to ninth day forecast
            self._scroll_to_ninth_day()

            # get the ninth day forecast
            ninth_day = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.DAY_9_CARD)
            )

            # get information
            date = ninth_day.find_element(*self.locators.DAY_DATE).text
            weather = ninth_day.find_element(*self.locators.WEATHER_DESC).text
            temp = ninth_day.find_element(*self.locators.TEMP_RANGE).text
            humidity = ninth_day.find_element(*self.locators.HUMIDITY_RANGE).text

            return {
                "date": date,
                "weather": weather,
                "temperature": temp,
                "humidity": humidity
            }
        except Exception as e:
            print(f"failed to get the ninth day forecast: {e}")
            return None

    def _scroll_to_ninth_day(self):
        """scroll to the ninth day"""
        # get all days cards
        days = self.driver.find_elements(*self.locators.DAY_CARDS)

        # try to scroll if days less nine
        if len(days) < 9:
            # get the size of screen
            window_size = self.driver.get_window_size()
            start_x = window_size['width'] * 0.5
            start_y = window_size['height'] * 0.8
            end_y = window_size['height'] * 0.2

            # scroll to the ninth day
            for _ in range(5):  # retry 5 times at most
                self.driver.swipe(start_x, start_y, start_x, end_y, 1000)
                time.sleep(2)
                days = self.driver.find_elements(*self.locators.DAY_CARDS)
                if len(days) >= 9:
                    break

    def take_screenshot(self, filename):
        """截取屏幕截图"""
        self.driver.save_screenshot(filename)