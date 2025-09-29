import os
from datetime import datetime


def create_screenshot_dir():
    """create screenshot dir"""
    screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    return screenshot_dir


def get_timestamp():
    """get timestamp"""
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def format_humidity_range(min_humidity, max_humidity):
    """format humidity range"""
    if min_humidity and max_humidity:
        return f"{min_humidity}-{max_humidity}%"
    return "N/A"
