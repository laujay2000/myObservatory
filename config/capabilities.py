from appium import webdriver


def get_ios_capabilities():
    """get iOS device Capabilities configuration"""
    return {
        "platformName": "iOS",
        "platformVersion": "16.0",  # 根据实际设备版本调整
        "deviceName": "iPhone 14",  # 根据实际设备调整
        "app": "/path/to/hongkong_observatory.ipa",  # 香港天文台应用的IPA路径
        "automationName": "XCUITest",
        "noReset": False,  # 每次测试前重置应用状态
        "autoAcceptAlerts": True,  # 自动接受系统弹窗
        "allowProvisioningDeviceRegistration": True
    }


def get_android_capabilities():
    """获取Android设备的Capabilities配置"""
    return {
        "platformName": "Android",
        "platformVersion": "11.0",  # 根据实际设备版本调整
        "deviceName": "Android Emulator",  # 或实际设备名称
        "app": "/path/to/hongkong_observatory.apk",  # 香港天文台应用的APK路径
        "automationName": "UiAutomator2",
        "appPackage": "gov.hko.weather",  # 假设的包名，需根据实际应用调整
        "appActivity": ".MainActivity",  # 假设的主Activity，需根据实际应用调整
        "noReset": False,
        "autoGrantPermissions": True  # 自动授予应用权限
    }


def get_driver(platform="android"):
    """根据平台获取Appium Driver"""
    if platform.lower() == "ios":
        caps = get_ios_capabilities()
    else:
        caps = get_android_capabilities()

    return webdriver.Remote("http://localhost:4723/wd/hub", caps)
