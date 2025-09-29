from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):
    # 元素定位器
    MENU_BUTTON = (AppiumBy.ID, "gov.hko.weather:id/menu_button")  # 假设的ID，需根据实际应用调整
    DAILY_FORECAST_OPTION = (AppiumBy.XPATH, "//*[@text='每日天气预报']")  # 假设的文本，需根据实际应用调整
    SEARCH_BUTTON = (AppiumBy.ID, "gov.hko.weather:id/search_button")  # 假设的ID
    LOCATION_INPUT = (AppiumBy.ID, "gov.hko.weather:id/location_input")  # 假设的ID
    HONG_KONG_OPTION = (AppiumBy.XPATH, "//*[@text='香港']")  # 假设的文本
    ACCEPT_TERMS_BUTTON = (AppiumBy.ID, "gov.hko.weather:id/accept_terms")  # 假设的ID
    CLOSE_AD_BUTTON = (AppiumBy.ID, "gov.hko.weather:id/close_ad")  # 假设的ID

    def __init__(self, driver):
        super().__init__(driver)

    def handle_initial_popups(self):
        """处理初始弹窗"""
        if self.is_element_displayed(self.ACCEPT_TERMS_BUTTON):
            self.click_element(self.ACCEPT_TERMS_BUTTON)

        if self.is_element_displayed(self.CLOSE_AD_BUTTON):
            self.click_element(self.CLOSE_AD_BUTTON)

    def go_to_daily_forecast(self):
        """进入每日天气预报页面"""
        self.click_element(self.MENU_BUTTON)
        self.click_element(self.DAILY_FORECAST_OPTION)

    def search_location(self, location="香港"):
        """搜索并选择地点"""
        self.click_element(self.SEARCH_BUTTON)
        location_input = self.find_element(self.LOCATION_INPUT)
        location_input.clear()
        location_input.send_keys(location)

        # 选择搜索结果中的香港
        self.click_element(self.HONG_KONG_OPTION)

    def is_home_page_loaded(self):
        """验证首页是否加载完成"""
        return self.is_element_displayed(self.MENU_BUTTON)
