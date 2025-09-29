import pytest
from config.capabilities import get_driver
from pages.home_page import HomePage
from pages.nine_day_forecast_page import ForecastPage
from config.config import UI_LOG
from utils.logging_use import Logger

logger = Logger.init_log_config(__name__, UI_LOG)

@pytest.fixture(scope="module", params=["android", "ios"])
def driver(request):
    """创建并返回Appium Driver，测试结束后关闭"""
    platform = request.param
    driver = get_driver(platform)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def home_page(driver):
    """创建首页对象"""
    return HomePage(driver)


@pytest.fixture(scope="module")
def forecast_page(driver):
    """创建天气预报页面对象"""
    return ForecastPage(driver)


@pytest.fixture(scope="function")
def setup_test(home_page, forecast_page):
    """测试前置操作：确保在正确的页面"""
    if not home_page.is_home_page_loaded():
        # 如果不在首页，尝试回到首页（具体实现取决于应用的导航逻辑）
        pass

    home_page.handle_initial_popups()
    home_page.search_location("香港")
    home_page.go_to_daily_forecast()

    # 确保天气预报页面加载完成
    assert forecast_page.is_forecast_displayed(), "天气预报页面未加载成功"
