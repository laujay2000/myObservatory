from playwright.sync_api import Page, sync_playwright
from config.config import Config
import logging
from typing import Literal


class Base:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 3000  # 超时时间(毫秒)
        self.config = Config()

    # 统一的元素定位方法
    """
    attached：元素已添加到 DOM 树中
    detached：元素从 DOM 树中移除了，页面上不再有该元素的 DOM 节点
    visible：元素不仅在 DOM 中，还得是可见的
    hidden：元素从 DOM 移除，或者虽在 DOM 但不可见
    """

    def locate(self, selector: str, state: Literal["attached", "detached", "visible", "hidden"] = "visible"):
        try:
            self.page.wait_for_selector(selector, state=state, timeout=self.timeout)
            return self.page.locator(selector)
        except Exception as e:
            print(e)
            logging.error(f"定位元素{selector}失败")

    # 访问URL
    def goto(self, url):
        try:
            self.page.goto(url, timeout=self.timeout)
        except Exception as e:
            print(e)
            logging.error(f"访问URL{url}失败")

    # 点击事件
    def click(self, selector):
        try:
            self.locate(selector).click(timeout=self.timeout)
        except Exception as e:
            print(e)
            logging.error(f"点击元素{selector}失败")

    # 点击按钮
    def click_button(self, button_name):
        try:
            self.page.get_by_role("button", name=button_name).click()
        except Exception as e:
            print(e)
            logging.error(f"点击按钮{button_name}失败")

    # 点击事件
    def click_btn_by_role(self):
        try:
            self.page.get_by_role("button", name="登录").click()
        except Exception as e:
            print(e)
            logging.error(f"点击登录失败")

    # 输入事件
    def fill(self, selector, text):
        try:
            self.locate(selector).fill(text, timeout=self.timeout)
        except Exception as e:
            print(e)
            logging.error(f"在元素{selector}中输入{text}失败")

    # 获取元素文本值
    def get_text(self, selector):
        try:
            return self.locate(selector).inner_text(timeout=self.timeout)
        except Exception as e:
            print(e)
            logging.error(f"获取元素{selector}的文本失败")

    # 检查元素是否可见
    def is_visible(self, selector):
        try:
            return self.locate(selector, state="visible").is_visible()
        except Exception as e:
            print(e)
            logging.error(f"检查元素{selector}是否可见失败")

    # 检查元素是否存在
    def is_attached(self, selector):
        try:
            return self.locate(selector, state="attached").is_visible()
        except Exception as e:
            print(e)
            logging.error(f"检查元素{selector}是否存在失败")
