from utils.logging_use import Logger
from config.config import ASSERTION_LOG


class Assertion:
    # init log obj
    logger = Logger.init_log_config('assertion', ASSERTION_LOG)

    @staticmethod
    def assert_equal(actual, expected, identifier, message=""):
        """
        assert two values equal
        :param identifier: identifier
        :param actual: actual value
        :param expected: expected value
        :param message: error message
        """
        try:
            assert actual == expected, f"\nactual: {actual}，expected: {expected}，{message}"
            Assertion.logger.info(f"Assertion success: {actual} == {expected}，relative scenario {identifier}")
        except AssertionError as e:
            Assertion.logger.error(f"Assertion failed: {str(e)}")
            raise

    @staticmethod
    def assert_in(member, container, identifier, message=""):
        """
        assert member in container
        :param identifier: identifier
        :param member: member
        :param container: container
        :param message: error message
        """
        try:
            assert member in container, f"期望 {member} 在 {container} 中{message}"
            Assertion.logger.info(f"断言成功: {member} in {container}，对应的业务场景{identifier}")
        except AssertionError as e:
            Assertion.logger.error(f"断言失败: {str(e)}，对应的业务场景{identifier}")
            raise

    @staticmethod
    def assert_true(expr, identifier, message=""):
        """
        assert expr True
        :param identifier: identifier
        :param expr: expr
        :param message: error msg
        """
        try:
            assert expr, f"expected expr True\n{message}"
            Assertion.logger.info(f"assert success: expr True, relative scenario: {identifier}")
        except AssertionError as e:
            Assertion.logger.error(f"assert failed: {str(e)}，relative scenario {identifier}")
            raise
