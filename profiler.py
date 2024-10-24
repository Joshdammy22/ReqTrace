import httpx
import requests
import time

class Profiler:
    def __init__(self):
        self.logs = []

    def log_request(self, method, url, response_time):
        self.logs.append({
            'method': method,
            'url': url,
            'response_time': response_time,
        })

    def profile_request(self, method, url, async_mode=False):
        start_time = time.time()
        
        if async_mode:
            response = httpx.get(url)
        else:
            response = requests.get(url)
        
        end_time = time.time()
        response_time = end_time - start_time
        self.log_request(method, url, response_time)
        
        return response
