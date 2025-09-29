from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger(__name__)

    def find_element(self, locator):
        """查找单个元素"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException):
            self.logger.error(f"element not found: {locator}")
            self.take_screenshot(f"element_not_found_{locator}")
            raise

    def find_elements(self, locator):
        """查找多个元素"""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except (TimeoutException, NoSuchElementException):
            self.logger.error(f"elements not found: {locator}")
            self.take_screenshot(f"elements_not_found_{locator}")
            raise

    def click_element(self, locator):
        """点击元素"""
        element = self.find_element(locator)
        element.click()
        self.logger.info(f"click element: {locator}")
        time.sleep(1)  # 等待操作完成

    def get_element_text(self, locator):
        """获取元素文本"""
        element = self.find_element(locator)
        text = element.text
        self.logger.info(f"get text of element: {locator} -> {text}")
        return text

    def is_element_displayed(self, locator):
        """检查元素是否显示"""
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    def take_screenshot(self, name):
        """截取屏幕截图"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"截图保存至: {screenshot_path}")
        return screenshot_path

    def scroll_down(self):
        """向下滚动页面"""
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] / 2
        start_y = window_size['height'] * 0.8
        end_y = window_size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, 500)
        self.logger.info("向下滚动页面")
        time.sleep(1)

    def scroll_to_element(self, locator):
        """滚动到元素可见"""
        while not self.is_element_displayed(locator):
            self.scroll_down()
            # 防止无限滚动
            if self.driver.execute_script("return arguments[0].scrollTop",
                                        self.driver.find_element_by_tag_name('scroll')) == 0:
                break
