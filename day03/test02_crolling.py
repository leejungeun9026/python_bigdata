from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id="meigen">
            <h1>위키북스 도서</h1>
            <ul class="items">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
        <h1>위키북스 도서2</h1>
    </body></html>
"""

# 1. 위키북스 도서 추출
# .find() 사용
# .select() 사용

soup = BeautifulSoup(html, 'html.parser')
print(soup)

h1 = soup.find('h1').text
print("h1 find().text :", h1)

h1 = soup.select_one('h1').text
print("h1 select_one().text :", h1)

h1_1 = soup.select_one('div#meigen > h1').string
print(h1_1)

# 2. li 출력
lis = soup.select('div > ul > li')
for i in lis :
  print(i.string)

lis = soup.select('div#meigen > ul.items > li')
for i in lis :
  print(i.string)

lis = soup.select('div#meigen > ul.items > li')
for i in lis :
  print(i.text)