import allure
import pytest

from config.config import HKO_API_BASE_URL, TIMEOUT, API_YAML
from framework.api_request import ApiRequest
from utils.yamlUtils import YamlUtils
from utils.extractRelHumidity import extract_humidity_range


@allure.feature("天气预报功能")
@allure.story("获取第9天天气情况")
@pytest.mark.usefixtures("setup_test")
class TestGetNineDayForecast:

    @pytest.fixture(scope='class')
    def clint(self):
        clint = ApiRequest(HKO_API_BASE_URL, TIMEOUT)
        yield clint
    @allure.title("test the humidity of the day after tomorrow")
    def test_humidity(self, clint):
        api_data = YamlUtils.read_data(API_YAML)
        response_data = clint.get(api_data[0]['url'])
        humidity = extract_humidity_range(response_data.content)
        assert(float(humidity.split('-')[0]) > 0)