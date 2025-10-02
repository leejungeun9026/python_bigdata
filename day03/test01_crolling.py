from bs4 import BeautifulSoup

html = """
  <html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
  </body></html>
"""

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')
print(html) # 있는 그대로 출력됨 (공백도 그대로)
print(soup) # 파싱해서 출력됨

print('-'*10)

# 계층 구조로 접근하기
h1 = soup.html.body.h1
print('<h1> : ', h1)

p = soup.html.body.p
print('<p> : ', p)  # 첫번째 일치항목만 출력됨

p1 = p.next_sibling.next_sibling  # 다음 형제 노드를 찾는 것
print('<p1> : ',p1)



# soup이 제공하는 함수를 이용해보기
# find() : 하나일 때 사용
h1 = soup.find('h1')
print('h1 find : ', h1)
p = soup.find('p')
print('p find : ', p)

# findAll(), find_all() : 여러개일 때 사용
print('=====find all=====')
p_list = soup.findAll('p')
print('p_list findAll : ', p_list)
p_list = soup.find_all('p')
print('p_list find_all : ', p_list)

# select_one(), select()
print('=====select=====')
h1 = soup.select_one('h1')
print('h1 select_one : ', h1)
p = soup.select_one('p')
print('p select_one : ', p)
p_list = soup.select('p')
print('p_list select : ', p_list)

# .text .string .getText() : 문자만 출력(태그 제외)
print('=====문자만 출력(태그 제외)=====')
print(h1.text)
print(h1.string)
print(h1.getText())

print(p.text)
print(p.string)
print(p.getText())

# print(p_list.text)  객체라 불가능함
# print(p_list.string)
# print(p_list.getText())


