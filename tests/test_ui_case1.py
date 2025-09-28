# import pytest
# from pages.nine_day_forecast_page import NineDayForecastPage
# from utils.helpers import create_screenshot_dir, get_timestamp
#
#
# class TestNineDayForecastUI:
#     @pytest.mark.order(1)
#     def test_navigate_to_nine_day_forecast(self, driver):
#         """测试导航到九天预报页面"""
#         forecast_page = NineDayForecastPage(driver)
#         assert forecast_page.navigate_to_nine_day_forecast(), "无法导航到九天预报页面"
#
#     @pytest.mark.order(2)
#     def test_get_ninth_day_forecast(self, driver):
#         """测试获取第九天天气预报"""
#         forecast_page = NineDayForecastPage(driver)
#
#         # 获取第九天预报
#         forecast = forecast_page.get_ninth_day_forecast()
#
#         # 验证数据存在
#         assert forecast is not None, "无法获取第九天天气预报"
#         assert forecast['date'] != "", "日期为空"
#         assert forecast['weather'] != "", "天气描述为空"
#         assert forecast['temperature'] != "", "温度为空"
#         assert forecast['humidity'] != "", "湿度为空"
#
#         print(f"第九天天气预报: {forecast}")
#
#         # 截取屏幕截图
#         screenshot_dir = create_screenshot_dir()
#         timestamp = get_timestamp()
#         screenshot_path = f"{screenshot_dir}/ninth_day_forecast_{timestamp}.png"
#         forecast_page.take_screenshot(screenshot_path)
#         print(f"截图已保存: {screenshot_path}")