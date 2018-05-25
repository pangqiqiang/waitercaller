import requests
import json

ROOT_URL = "http://mrw.so"
SHORTEN = "/api.php?format={}&url={}"


class BitlyHelper():
    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format("json", longurl)
            r = requests.get(url)
            return r.json().get("url")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    BH = BitlyHelper()
    print(BH.shorten_url("www.baidu.com"))
