

- ## 데이터획득_level2_api를이용한수집

  > OPEN  API를 이용한 서버 통신 - Naver 이용 
  >
  > DB연결 
  >
  > ```python
  > >>> $ pip install request
  > 
  > # DB
  > >>>$ pip install pymysql  
  > >>>$ pip install sqlalchemy
  > ```
  >
  > 





- ## level3_webscraping

  > #### 웹스크래핑을 이용한 데이터 수집
  >
  > * open API를 이용한 데이터 수집이 불가한 경우 해당
  >
  > * 웹을 요청하여 html을 모두 받아서 DOM으로 올려서 데이터를 추출방식
  >
  > * DOM을 띠워서 데이터를 추출할때 사용하는 라이브러리
  >
  >   ```python
  >   >>> beautifulsoup (bs4)를 활용  
  >   >>> $ pip install beautifulsoup4
  >   ```
  >
  >   - **request + beautifulsoup(bs4)**
  >   - 콘텐츠가 존재하는 해당 페이지까지 진입
  >   - 진입간에 로그인, ajax등등 사람의 손을 타지 않는지 체크
  >   - 그냥 url만 넣으면 화면이 구성된다 => OK
  >   - html 자체에 프레임이 적용된경우 실제 주소까지 찾아서 이동
  >   - 통신시 get, post등 데이터를 전달해서 획득하는 것도 OK





## 1-level4_crawling_youtube

- 유튜브를 크롤링하여 데이터를 획득
- 크롤링을 해야 이유는 유튜브 자체가 ajax를 이용한 방식이므로 사람의 손길이 필요한 사이트
- 일반적인 html 자체에는 자체 정의 태그를 들을 혼용한다 => Angular.js를 부분 사용을 했다라고 판단됨.
- 일반적인 css selector의 규칙중에 id규칙(문서내에 고유하다)을 무시한다 => 사용 주의
- 데이터 로드는 ajax를 통해서 사용자가 스크롤링을 해서 리스트의 끝에 도착할때 더보기(이런 기능)이 처리되므로, 전체 데이터르 수집하기 위해서는 js를 가동시켜야 한다
- 사용라이브러리는 selenium을 사용

  - https://www.seleniumhq.org/
- 웹드라이버(여기서는 크롬을 사용)
  > https://sites.google.com/a/chromium.org/chromedriver/downloads  
  > 최신버전이 적용 않되는 혹은 버그가 있는 기능이 잇으므오, 혹시 않되면, 계속 버전을 내려가몃서 사용  
- API-DOCs
  > https://seleniumhq.github.io/selenium/docs/api/py/index.html 
  > https://selenium-python.readthedocs.io/

```python
$ pip| install selenium
```

