# #API Yandex.Translate
#
import requests
from pprint import pprint
# #
apiTocken = "dict.1.1.20220928T183617Z.4449b33063fe4328.b93679d48620ed6f3c20da6bff0237bcbd0e8d6a"
#
base_url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"

payload = {
    "key": apiTocken,
    "lang": "ru-en",
    "ui": "ru",
    "flags": 2,
    "text": "собака"
}
#
def translate_word(url, postData, word):
    postData["text"] = word
    resp = requests.get(url=url, params=postData).json()
    # pprint(resp)
    res = resp["def"][0]["tr"][0]["text"]
    print(res)
    return res

if __name__ == '__main__':
    print("let's start!")
    print()
    translate_word(base_url, payload, "кошка")
    print()
    print(f"Done")