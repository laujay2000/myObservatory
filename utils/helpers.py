import os
from datetime import datetime


def create_screenshot_dir():
    """创建截图目录"""
    screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    return screenshot_dir


def get_timestamp():
    """获取时间戳"""
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def format_humidity_range(min_humidity, max_humidity):
    """格式化湿度范围"""
    if min_humidity and max_humidity:
        return f"{min_humidity}-{max_humidity}%"
    return "N/A"
