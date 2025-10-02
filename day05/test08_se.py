from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import urllib.request as req

url = 'https://www.google.com/imghp'
query = '고양이'
driver = wd.Chrome()
driver.get(url)
time.sleep(3)
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys(query)
search_box.submit()

time.sleep(5)

##### 현재 페이지 스크롤 위치 가져오기
# 윈도우의 높이
last_height = driver.execute_script("return window.scrollY")
print(last_height)

# 현재 페이지의 전체스크롤
pre_height = driver.execute_script("return document.body.scrollHeight")
print(pre_height)

interval = 2
while True :
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  time.sleep(interval)

# 현재 스크롤 높이
  curr_height = driver.execute_script("return document.body.scrollHeight")
  if curr_height == pre_height :
    break
  pre_height = curr_height
  
save_path = f'C:/Users/i/Desktop/bigdata/google/{query}'
import os
if not os.path.exists(save_path) : 
  os.makedirs(save_path)

img_elements = driver.find_elements(By.CSS_SELECTOR, 'div.H8Rx8c img.YQ4gaf')
imgs = []
for index, img in enumerate(img_elements) :
  try :
    img_src = img.get_attribute('src')
    img_alt = img.get_attribute('alt')
    if img_src and "http" in img_src :
      imgs.append({'src':img_src, 'alt' : img_alt})
      req.urlretrieve(img_src,f"{save_path}/{query}_{index}.png")
      print(f"{index} : 다운로드 완료 - {img_alt}")
  except :
    pass
driver.close()