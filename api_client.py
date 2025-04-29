import requests

class APIClient:
    def __init__(self, base_url, headers=None):
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.base_url = base_url.rstrip("/")

    def get(self, path, **kwargs):
        return self.session.get(f"{self.base_url}/{path.lstrip('/')}", **kwargs)

    def post(self, path, **kwargs):
        return self.session.post(f"{self.base_url}/{path.lstrip('/')}", **kwargs)

    def put(self, path, **kwargs):
        return self.session.put(f"{self.base_url}/{path.lstrip('/')}", **kwargs)

    def patch(self, path, **kwargs):
        return self.session.patch(f"{self.base_url}/{path.lstrip('/')}", **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(f"{self.base_url}/{path.lstrip('/')}", **kwargs)
