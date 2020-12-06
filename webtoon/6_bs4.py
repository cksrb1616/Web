#pip install requests
#pip install beautifulsoup4
#pip install lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # The first 'a' element will be shown
# print(soup.a.attrs) # a element 의 속성정보 dictionary 형태를
# print(soup.a["href"]) # a element 의 href 속성정보

# print(soup.find("a", attrs = {"class":"Nbtn_upload"})) # class 값이 "Nbtn_upload"인 a element 를 찾아줘
# print(soup.find(attrs = {"class":"Nbtn_upload"})) # class 값이 "Nbtn_upload"인 element 를 찾아줘
# print(soup.find("li",attrs={"class":"rank01"}))
# print(rank1.a) # 그 중 a element만
rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text()) # 글자 부분만
# print(rank1.next_sibling) # 태그사이 줄바꿈이나 개행정보가 있어서 빈칸을 나타내느 것 일 수 있음
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") #그중 li에 해당하는 태그만
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li")) # 형제들을 모두

webtoon = soup.find("a", text="이번 생도 잘 부탁해-27화") # 여는 테그와 닫는 테그 사이의 값 제목 같은 <> ㅁㄴㅇㅁㅈㅁㅎ </>
print(webtoon)



