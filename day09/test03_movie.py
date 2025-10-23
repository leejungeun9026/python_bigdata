from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker


# 동적 크롤링으로 네이버 영화 사이트에 접속하여 (https://m.entertain.naver.com/movie) 박스오피스 영화 정보 데이터를 수집
# 1. 총 10개의 데이터를 수집
# 2. 순위, 제목, 별점, 누적 관객수 naver_movie.csv 파일로 저장 
# 3. 아래 그림과 같이 별점에 대해 matplotlib 를 이용하여 막대그래프와 파이 그래프 그리기


# 세션 시작
driver = webdriver.Chrome()
driver.get('https://m.entertain.naver.com/movie')
time.sleep(1)

# 박스오피스 클릭
driver.find_element(By.XPATH, '//button[@data-section-id="boxOffice"]').click()
time.sleep(1)
# 더보기 클릭
driver.find_element(By.XPATH, '//button[contains(@class, "Home_button_group_more")]').click()
time.sleep(2)

# 요소 찾아서 배열에 담기
movie_list = driver.find_elements(By.XPATH, '//ol[contains(@class, "Home_section_ranking_list")]/li')

datas = []
for li in movie_list :
  ranking = li.find_element(By.XPATH, './/*[contains(@class, "Home_rank")]/span[@class="blind"]').text
  ranking = re.sub(r"[^0-9]","", ranking)
  title = li.find_element(By.XPATH, './/*[contains(@class, "Home_title")]').text
  stars = li.find_element(By.XPATH, './/*[contains(@class, "Home_star")]/span[contains(@class, "Home_number")]').text
  views = li.find_element(By.XPATH, './/*[contains(@class, "Home_count")]').text
  datas.append([ranking, title, stars, views])

# csv파일로 저장
df = pd.DataFrame(datas, columns=('순위', '제목', '별점', '누적 관객수'))
df.to_csv('day09/naver_movie.csv', mode='w', index=False, encoding='utf-8-sig')





# 그래프 그리기
# 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 데이터 가져오기
read_df = pd.read_csv('day09/naver_movie.csv')

# 별점 컬럼 수정
read_df['별점'] = pd.to_numeric(read_df['별점'], errors='coerce').fillna(0)
read_df['별점'] = read_df['별점'].astype(int)

starCount = read_df['별점'].value_counts()
x = starCount.index.tolist()
y = starCount.tolist()

plt.bar(x, y, color='blue')
plt.title('네이버 영화 별점 분포')
plt.xlabel('별점')
plt.ylabel('개수')
plt.xticks(x)
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
plt.show()


# 파이그래프
plt.pie(y, labels=x, autopct='%.1f%%')
plt.show()
