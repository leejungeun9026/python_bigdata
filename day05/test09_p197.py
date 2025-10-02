# p197
import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup

def CoffeeBean_store(result):
  CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
  wd = webdriver.Chrome()

  for i in range(1,5) :  # 마지막 매장번호(최근 신규매장 포함)
    wd.get(CoffeeBean_URL)
    time.sleep(1)
    try:
      wd.execute_script("storePop2(%d)" %i)
      time.sleep(1)
      html = wd.page_source
      soupCB = BeautifulSoup(html, 'html.parser')
      #matizCoverLayer0Content > div > div > div.store_txt > h2
      store_name_h2 = soupCB.select('div.store_txt > h2')
      store_name = store_name_h2[0].string  # 매장명
      
      # div.store_txt > table > tbody > tr > td
      store_info = soupCB.select('div.store_txt > table > tbody > tr > td')
      store_address_list = list(store_info[2])
      store_address  = store_address_list[0]
      store_phone = store_info[3].string
      result.append([store_name]+[store_address]+[store_phone])
    except:
      continue  
  return


def main():
  result = []
  print('CoffeBean store crawling >>>>>>>>>>>>>>>>>>>>')
  CoffeeBean_store(result)
  # print(result)
  CB_tbl = pd.DataFrame(result, columns=('store','address','phone'))
  CB_tbl.to_csv('day05\\CoffeeBean.csv',encoding='utf-8-sig', mode='w', index=True)
  print('CoffeeBean.csv  파일 저장 완료 >>>')


main()  