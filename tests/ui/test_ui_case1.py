import pytest
import allure
from datetime import datetime, timedelta


@allure.feature("天气预报功能")
@allure.story("获取第9天天气情况")
@pytest.mark.usefixtures("setup_test")
class TestNinthDayWeatherForecast:

    @allure.title("验证第9天天气预报基本信息显示")
    def test_ninth_day_weather_basic_info(self, forecast_page):
        """验证第9天天气预报的基本信息是否正确显示"""
        # 获取第9天的日期
        day9_date = forecast_page.get_day_9_date()
        assert day9_date is not None, "第9天的日期未显示"

        # 验证日期是否合理（应该是当前日期加8天左右）
        today = datetime.now()
        expected_date = today + timedelta(days=8)
        # 简单验证年份和月份是否匹配（具体日期格式需根据应用调整）
        assert str(expected_date.year) in day9_date, f"日期年份不正确: {day9_date}"
        assert str(expected_date.month) in day9_date or \
               datetime.strftime(expected_date, "%b") in day9_date, \
            f"日期月份不正确: {day9_date}"

        # 验证天气状况显示
        weather_condition = forecast_page.get_day_9_weather_condition()
        assert weather_condition is not None and weather_condition != "", "天气状况未显示"

        # 验证温度显示
        temperature = forecast_page.get_day_9_temperature()
        assert temperature is not None, "温度信息未显示"
        assert temperature['min'] <= temperature['max'], "最低温度大于最高温度"

    @allure.title("验证第9天湿度信息")
    def test_ninth_day_humidity(self, forecast_page):
        """验证第9天的湿度信息是否合理"""
        humidity = forecast_page.get_day_9_humidity()
        assert humidity is not None, "湿度信息未显示"
        assert 0 <= humidity['min'] <= 100, f"最低湿度值不合理: {humidity['min']}"
        assert 0 <= humidity['max'] <= 100, f"最高湿度值不合理: {humidity['max']}"
        assert humidity['min'] <= humidity['max'], "最低湿度大于最高湿度"

    @allure.title("验证第9天风信息")
    def test_ninth_day_wind(self, forecast_page):
        """验证第9天的风信息是否显示"""
        wind_info = forecast_page.get_day_9_wind()
        assert wind_info is not None and wind_info != "", "风信息未显示"
        # 验证风信息包含预期的元素（如风向、风力等级或风速）
        assert any(keyword in wind_info for keyword in ["北", "南", "东", "西", "风", "级", "km/h"]), \
            f"风信息格式异常: {wind_info}"

    @allure.title("验证第9天紫外线指数")
    def test_ninth_day_uv_index(self, forecast_page):
        """验证第9天的紫外线指数是否合理"""
        uv_index = forecast_page.get_day_9_uv_index()
        assert uv_index is not None, "紫外线指数未显示"
        assert 0 <= uv_index <= 11, f"紫外线指数值不合理: {uv_index}"

    @allure.title("测试温度单位切换功能")
    def test_temperature_unit_switch(self, forecast_page):
        """测试温度单位在摄氏度和华氏度之间切换是否正常"""
        # 获取切换前的单位
        temp_before = forecast_page.get_day_9_temperature()
        assert temp_before is not None, "切换前未获取到温度信息"
        original_unit = temp_before['unit']

        # 切换温度单位
        forecast_page.switch_temperature_unit()

        # 验证单位已切换
        temp_after = forecast_page.get_day_9_temperature()
        assert temp_after is not None, "切换后未获取到温度信息"
        assert temp_after['unit'] != original_unit, "温度单位未切换成功"

        # 切换回原始单位
        forecast_page.switch_temperature_unit()

    @allure.title("测试刷新天气预报功能")
    def test_refresh_forecast(self, forecast_page):
        """测试刷新功能后第9天的天气信息仍然可以获取"""
        # 获取刷新前的天气状况
        weather_before = forecast_page.get_day_9_weather_condition()

        # 刷新数据
        forecast_page.refresh_forecast()

        # 验证刷新后仍能获取天气信息
        weather_after = forecast_page.get_day_9_weather_condition()
        assert weather_after is not None and weather_after != "", "刷新后天气状况未显示"

        # 注意：天气信息可能刷新后不变，所以不验证内容变化，只验证可以获取

    @allure.title("测试多语言环境下第9天天气显示")
    def test_language_switch(self, forecast_page):
        """测试切换语言后第9天的天气信息仍然可以获取"""
        # 获取切换前的天气状况
        weather_before = forecast_page.get_day_9_weather_condition()

        # 切换语言
        forecast_page.switch_language()

        # 验证切换后仍能获取天气信息
        weather_after = forecast_page.get_day_9_weather_condition()
        assert weather_after is not None and weather_after != "", "切换语言后天气状况未显示"
        assert weather_after != weather_before, "语言未切换成功"

        # 切换回原始语言
        forecast_page.switch_language()
