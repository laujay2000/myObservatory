import pytest
from appium import webdriver
from config.capabilities import get_android_capabilities, get_ios_capabilities
from config.config import PLATFORM, APPIUM_SERVER


@pytest.fixture(scope="function")
def driver():
    # select capabilities according to the platform
    if PLATFORM.lower() == 'android':
        capabilities = get_android_capabilities()
    elif PLATFORM.lower() == 'ios':
        capabilities = get_ios_capabilities()
    else:
        raise ValueError(f"not support platform: {PLATFORM}")

    # init driver
    driver = webdriver.Remote(
        command_executor=APPIUM_SERVER,
        desired_capabilities=capabilities
    )

    # set wait
    driver.implicitly_wait(10)

    yield driver

    # quit driver after testing
    driver.quit()