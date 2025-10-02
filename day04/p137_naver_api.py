import urllib.request
import datetime
import json

clientId = 'kyGIFJcNnKF8SjSf81oB'
clientSecret = 'NvigH1o4CC'

# url 접속 요청 및 응답 반환 함수
def getRequestUrl(url) :
  req = urllib.request.Request(url)
  req.add_header('X-Naver-Client-Id', clientId)
  req.add_header('X-Naver-Client-Secret', clientSecret)
  try :
    response = urllib.request.urlopen(req)
    if response.getcode() == 200 :
      print('[%s] Url Request Success' %datetime.datetime.now())
      return response.read().decode('utf-8')
  except Exception as e :
    print(e)
    print('[%s] Error for URL %s' %(datetime.datetime.now(), url))
    return None


# 네이버 뉴스 검색 url 작성 및
# url호출하여 응답받은 json 데이터를 python 객체로 반환하는 함수
def getNaverSearch(node, srcText, start, display) :
  base = 'https://openapi.naver.com/v1/search'
  node = '/%s.json' %node
  parameters = '?query=%s&start=%s&display=%s' %(urllib.parse.quote(srcText), start, display)
  url = base + node + parameters
  responseDecode = getRequestUrl(url)
  if responseDecode == None :
    return None
  else :
    # loads() : json 문자열을 python 객체로 리턴
    return json.loads(responseDecode)


# json형식의 응답데이터를 필요한 데이터만 딕셔너리 형태로 만들어 반환 
def getPostData(post, jsonResult, cnt) :
  title = post['title']
  description = post['description']
  org_link = post['originallink']
  link = post['link']
  # strptime() : 날짜와 시간 형식의 문자열을 datetime으로 반환
  pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
  # strftime() : 날짜와 시간(datetime)을 문자열로 반환
  pDate = pDate.strftime('%Y=%m=%d %H:%M:%S')

  jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'org_link':org_link, 'link':link, 'pDate':pDate})


# 전체 작업 실행 함수
def main() :
  node = 'news'
  srcText = input('검색어를 입력하세요 >> ')
  cnt = 0
  jsonResult = []
  jsonResponse = getNaverSearch(node, srcText, 1, 100)
  total = jsonResponse['total']
  print(total)
  while ((jsonResponse != None) and (jsonResponse['display'] != 0)) :
    for post in jsonResponse['items'] :
      cnt += 1
      getPostData(post, jsonResult, cnt)
    
    start = jsonResponse['start'] + jsonResponse['display']
    if start == 1001 : break # 네이버 뉴스는 1000개까지만 무료 제공됨
    jsonResponse = getNaverSearch(node, srcText, start, 100)

  print('전체검색 : %d건' %total)
  with open('%s_naver_%s.json' %(srcText, node), 'w', encoding='utf-8') as outfile:
    # dumps() : 파이썬 객체를 json문자열로 반환
    jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(jsonFile)
  print("가져온 데이터 : %d건" %(cnt))
  print('%s_naver_%s.json SAVED' %(srcText, node))


main()