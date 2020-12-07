# Different by browser like chrome and explorer
# Able to find by what is my user agent
import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":}
res = requests.get(url,headers=headers)
print("response code :", res.status_code)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
