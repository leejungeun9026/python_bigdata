import urllib.request
import json

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
  getRequestUrl(url)
  responseDecode = getRequestUrl(url)
  # 응답 객체 여부에 따라 반환
  if responseDecode == None :
    return None
  else :
    return json.loads(responseDecode)
   

# main 함수
def main(encText) :
  cnt = 0
  jsonResult = []
  responseJson = getNaverSearch(encText, 1, 100)
  while ((responseJson != None) and (responseJson['display'] != 0)) :
    for post in responseJson['items'] :
      cnt += 1
      title = post['title']
      link = post['link']
      description = post['description']
      bloggername = post['bloggername']
      bloggerlink = post['bloggerlink']
      postdate = post['postdate']
      jsonResult.append({'title':title, 'link':link, 'description':description, 'bloggerlink':bloggerlink, 'postdate':postdate})

    start = responseJson['start'] + responseJson['display']
    if start == 1001 : break
    responseJson = getNaverSearch(encText, start, 100)

  # json파일로 내보내기
  with open('day07\\%s_naver_%s.json' %(encText, "blog"), 'w', encoding='utf-8') as outfile:
      # 파이썬 객체를 json문자열로 반환
      jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
      outfile.write(jsonFile)



# 실행
encText = "인공지능"
main(encText)