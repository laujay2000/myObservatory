import pytest
import os


def run_tests():
    """执行测试并生成Allure报告"""
    # 创建必要的目录
    for dir in ["screenshots", "allure-results"]:
        if not os.path.exists(dir):
            os.makedirs(dir)

    # 执行测试
    pytest.main([
        # "tests/ui/test_ui_case1.py",
        "tests/",
        "--alluredir", "allure-results",
        "-v", "-s"
    ])

    # 生成并打开Allure报告（需要系统安装Allure）
    print("测试执行完成，正在生成报告...")
    os.system("allure generate allure-results -o allure-report --clean")
    os.system("allure open allure-report")


if __name__ == "__main__":
    run_tests()
