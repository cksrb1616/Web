import re
# abcd, book, desk
# ca?e
# care cafe case cave

p = re.compile("ca.e")
# . : (ca.e) one letter 하나의 문자 care cafe
# ^ : (^de) start of strings 문자열의 시작 desk destination
# $ : (se$) end of strings 문자열의 끝 case base

def print_match(m):
    #print(m.group()) #If there is no match -> show error
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string():", m.string) # 입력받은 문자열 반환
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index input된 값에서의 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span()", m.span()) # 일치하는 문자열의 시작/끝 index
    else:
        print("no matching")
# m = p.match("care") # careless 도 care로 출력. index 순서대로 맞는지 점검 후 출력해버리기 때문
# print_match(m)

# m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인 care 출력 careless
# print_match(m)

#lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
#print(lst)

# 1. p = re.compile("원하는형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 리스트 형태로 반환

