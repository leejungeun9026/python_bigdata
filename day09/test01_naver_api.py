import urllib.request
import json
import re
import pandas as pd

# 네이버 Open API 를 활용한 블로그 데이터 수집
# 1. 입력한 검색어에 해당하는 데이터를 수집하여 .json 파일로 내보내기
#     파일명은 본인이름_naverblog_검색어.json
# 2. json 파일을 읽어 title 컬럼만 추출한 뒤 특수문자를 제거하여 DataFrame에 저장한다.


# 요청 및 응답 반환
def getRequestUrl(url) :    
  clientId = 'kyGIFJcNnKF8SjSf81oB'
  clientSecret = 'NvigH1o4CC'
  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",clientId)
  request.add_header("X-Naver-Client-Secret",clientSecret)
  response = urllib.request.urlopen(request)
  rescode = response.getcode()
  if(rescode==200):
      # 응답 객체 담기
      print('Url Request Success')
      return response.read().decode('utf-8')
  else:
      print("Error Code:", rescode)
      return None

# 쿼리 작성 및 요청
def getNaverSearch(encText, start, display) :
  base = "https://openapi.naver.com/v1/search/blog.json"
  parameters = '?query=%s&start=%s&display=%s' %(urllib.parse.quote(encText), start, display)
  url = base + parameters
  # 요청 실행
  responseDecode = getRequestUrl(url)  
  # 응답 객체 여부에 따라 반환
  if responseDecode == None :
    return None
  else :
    return json.loads(responseDecode)




# 변수 초기화
encText = "파이썬"
file_name = f"이정은_naverblog_{encText}.json"

# 1-1. 검색 요청 및 응답 객체 저장
cnt = 0
jsonResult = []
responseJson = getNaverSearch(encText, 1, 100)
while ((responseJson != None) and (responseJson['display'] != 0)) :
  for post in responseJson['items'] :
    cnt += 1
    title = post['title']
    description = post['description']
    link = post['description']
    postdate = post['postdate']
    jsonResult.append({'title':title , 'description':description, 'link':link, 'postdate':postdate})
  start = responseJson['start'] + responseJson['display']
  if start == 1001 : break
  responseJson = getNaverSearch(encText, start, 100)


# 1-2. 결과를 json파일로 내보내기
with open(f'day09/{file_name}', 'w', encoding='utf-8') as outFile:
  # 파이썬 객체를 json문자열로 반환
  jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
  outFile.write(jsonFile)



# 2-1. json파일 읽어오기
with open(f'day09/{file_name}', 'r', encoding='utf-8') as inFile:
  readJson = json.load(inFile)

# 2-2. title만 추출, 특수문자 제거, DataFrame에 저장
result = []
for i in readJson :
  title = i['title']
  title = re.sub(r'</?b>', '', title) # 태그 제거
  title = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', title) # 특수문자 제거
  result.append(i['title'])
df = pd.DataFrame(result, columns=['title'])
print(df)