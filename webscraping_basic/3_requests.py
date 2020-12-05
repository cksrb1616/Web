# At terminal pip install requests
import requests
res = requests.get("http://google.com")
print("response code :", res.status_code)
res.raise_for_status()
# when there is problem show the problem and end the program
# 한 문장으로 밑에 if 문장 다 대

#if res.status_code == requests.codes.ok:
#    print("Normal")
#else:
#    print("There is a problem. [error code ", res.status_code, "]")체

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
