import requests


class Utils:
    @staticmethod
    def execute_get_request(url):
        response = requests.get(
            url,
            headers={"Content-Type": "application/json", "X-Finnhub-Token": "ccu7q2iad3iei7t0psugccu7q2iad3iei7t0psv0"},
        )
        return response
