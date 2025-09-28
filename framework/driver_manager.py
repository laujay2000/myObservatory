from playwright.sync_api import sync_playwright, Browser, Page
from config.config import Config

"""
集中处理浏览器的创建、配置和销毁
根据配置文件选择浏览器配置
支持同时在多个浏览器上运行
"""
class DriverManager:

    def __init__(self):
        self.config = Config()
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    # 初始化浏览器驱动
    def init_driver(self):
        # 启动Playwright实例
        self.playwright = sync_playwright().start()
        # 从配置中获取浏览器类型，默认为Chromium
        browser_type = self.config.get('browser', 'chromium').lower()

        if browser_type == 'chromium':
            browser = self.playwright.chromium
        elif browser_type == 'firefox':
            browser = self.playwright.firefox
        elif browser_type == 'webkit':
            browser = self.playwright.webkit
        else:
            raise ValueError(f"不支持的浏览器类型: {browser_type}")

        self.browser = browser.launch(
            # 是否界面运行
            headless=self.config.get('headless', False),
            # 执行延迟(毫秒)
            slow_mo=self.config.get('slow_mo', 0),
            # 操作超时时间(毫秒)
            timeout=self.config.get('timeout', 3000),
        )

        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.set_default_timeout(self.config.get('timeout', 3000))

        return self.page

    # 退出浏览器驱动
    def quit(self):
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
