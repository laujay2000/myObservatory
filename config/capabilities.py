def get_android_capabilities():
    return {
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'Android Emulator',
        'automationName': 'UiAutomator2',
        'appPackage': 'hko.MyObservatory_v1_0',
        'appActivity': 'hko.MyObservatory_v1_0.A81_Main',
        'autoGrantPermissions': True,
        'newCommandTimeout': 300,
        'androidInstallTimeout': 90000,
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }


def get_ios_capabilities():
    return {
        'platformName': 'iOS',
        'platformVersion': '15.0',
        'deviceName': 'iPhone Simulator',
        'automationName': 'XCUITest',
        'bundleId': 'com.hko.MyObservatory',
        'autoAcceptAlerts': True,
        'newCommandTimeout': 300
    }