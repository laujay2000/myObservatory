import os
from datetime import datetime, timedelta

# base config
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)

ASSERTION_LOG = os.path.join(BASE_DIR, 'log', 'assertion.log')
YAML_LOG = os.path.join(BASE_DIR, 'log', 'yaml_utils.log')
API_LOG = os.path.join(BASE_DIR, 'log', 'api_request.log')
UI_LOG = os.path.join(BASE_DIR, 'log', 'ui_test.log')
API_YAML = os.path.join(BASE_DIR, "data", "api.yaml")



TIMEOUT = 10
PLATFORM = os.getenv('PLATFORM', 'android')  # or 'ios'
APPIUM_SERVER = os.getenv('APPIUM_SERVER', 'http://localhost:4723/wd/hub')
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 10))

# API config
HKO_API_BASE_URL = 'https://pda.weather.gov.hk'
API_PARAMS = {
    'dataType': 'fnd',
    'lang': 'tc'
}

# get the date after tomorrow
day_after_tomorrow = (datetime.now() + timedelta(days=2)).strftime('%Y%m%d')
