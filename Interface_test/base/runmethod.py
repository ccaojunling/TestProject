import requests


class RunMethod:

    def post_main(self, url, data, header=None):
        res = None
        if header:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res

    def get_main(self, url, data=None, header=None):
        res = None
        if header:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res

    def run_main(self, method, url, data=None,header=None):
        res = None
        if method == "post":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res
