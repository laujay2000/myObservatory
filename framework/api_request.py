import time
import requests

from utils.logging_use import Logger
from config.config import API_LOG


class ApiRequest:
    logger = Logger.init_log_config(__name__, API_LOG)

    def __init__(self, base_url, timeout):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    def _send_request(self, method, url, data=None, **kwargs):
        start_time = time.time()
        full_url = self.base_url + url
        method = str(method).lower()
        if method == 'get':
            resp = self.session.request(method, full_url, timeout=self.timeout, params=data, **kwargs)
        elif method in ["post"]:
            headers = kwargs.get("headers", {})
            if "Content-Type" not in headers:
                headers["Content-Type"] = "application/json"
                kwargs["headers"] = headers
            resp = self.session.request(method, full_url, timeout=self.timeout, data=data, **kwargs)
        else:
            ApiRequest.logger.error("method is not support")
            raise ValueError("method is not support")

        try:
            resp.raise_for_status()
            ApiRequest.logger.info(
                f"url：{url}, request method：{method}，request header：{kwargs.get('headers')}, request body：{data}")
            return resp
        except requests.exceptions.RequestException as e:
            ApiRequest.logger.error(f"Request to {full_url} failed: {e}")
            raise

    def get(self, url, params=None, **kwargs):
        return self._send_request("get", url, data=params, **kwargs)

    def post(self, url, data=None, **kwargs):
        return self._send_request("post", url, data=data, **kwargs)


if __name__ == '__main__':
    api = ApiRequest("https://pda.weather.gov.hk", 10)
    response_data = api.get("/locspc/data/ocf_data/v3/HKO.json")
