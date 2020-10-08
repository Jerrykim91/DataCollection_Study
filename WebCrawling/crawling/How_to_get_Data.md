

# 데이터 획득

<hr>

1. level 1 

- 제공이 된다

- 사내 데이터, 공공 데이터, 대학및 연구기관의 제공 데이터

- 콘테스트 데이터(국내대회 해외대회(캐글kaggle)) 

  => 상업성이 없고, 정제된 데이터다    

  

2. level 2

- open API 사용

  - #### Open API(Rest API)란?

    - **API(Application Programming Interface):**
      특정 프로그램을 만들기 위해 제공되는 모듈(함수 등)을 의미
    - **Open API:** 공개 API로, 누구나 사용할 수 있도록 공개된 API (주로 Rest API 기술을 많이 사용함)
    - Rest API (Representational State Transfer API):HTTP프로토콜을 통해 서버 제공 기능을 사용할 수 있는 함수를 의미
      - 일반적으로 XML, JSON의 형태로 응답을 전달(원하는 데이터 추출이 수월)

- http 통신을 통해서 응답 데이터를 통해 수집

- ex) kakako ,naver, t, goggle 등등 포털이나 대기업 제공하는 open  API를 활용

- 단, 쿼리 제한(일일 쿼리수)

- 정제된 데이터다

  **<<  request 모듈>>**

  ```python
  import urllib.request
  import os
  import sys
  
  #Insatll
  >>> $ pip install request
  
  # DB
  >>>$ pip install pymysql  
  >>>$ pip install sqlalchemy
  ```

  - urllib.request 모듈을 사용하여 통신처리후 JSON 파싱을 통한 데이터 추출

  - **sys **
      - 변수와 함수를직접 제어할수있게 해주는 모듈 
      - 명령행 인자 처리
  - **os(Operating System)**
      - 환경 변수나 디렉터리 ,파일등의 os자원을 제어할수있게 해주는 모듈 
      - 파이썬 통해 파일을 카피, 디렉터리를 생성하고 특정 디렉터리 내의 파일 목록을 얻고자 할 때 os 모듈을 사용
        from os import(모듈내에 필요한것만) * 대신에 import os(모듈전체) 스타일을 사용 ->os.open() 이 내장 open() 을 안가림

  

3. level 3

- web scraping (웹 스크래핑)
  - open API를 이용한 데이터 수집이 불가한 경우 해당
  * 웹을 요청하여 html을 모두 받아서 DOM으로 올려서 데이터를 추출방식
  * DOM을 띠워서 데이터를 추출할때 사용하는 라이브러리
- 우리가 접근할수 잇는 모든 정보는 웹에서 접근이 가능하다라는 명제로 출발
- 보안 데이터는 불가
- 웹사이트를 긁어서 원하는 데이터를 추출하여 전처리 적제하는 방식
- request + beautifulsoup(bs4)

```python
>>> $ pip install beautifulsoup4
```



4. level 4

- **Crawling(크롤링)**

  Web상에 존재하는 Contents를 수집

  1. HTML 페이지를 **가져와서**, HTML/CSS등을 **파싱**하고, 필요한 데이터만 추출하는 기법
  2. **Open API(Rest API)**를 제공하는 서비스에 Open API를 호출해서, 받은 데이터 중 필요한 데이터만 추출하는 기법
  3. **Selenium**등 브라우저를 프로그래밍으로 조작해서, 필요한 데이터만 추출하는 기법

- 정보의 출처가 웹사이트는 맞는데 사람의 손을 타야지만 데이터를 획득할수 있는 경우

- ajax를 사용하거나, 디도스 방어가 들어갔거나,등등 사람손을 거친후에야만
  접근가능한 사이트가 대상
  
- selenium(셀레니움) + 자동화(qt5 or 스케쥴러를 활용)

```python
$ pip| install selenium
```



---

**Json(JavaScript Object Notation )**

- 웹환경에서 서버와 클라이언트 사이에 데이터를 주고 받을때 많이 사용
  - Rest API가 주요한 예제

---

[참고 도서]<a href='https://www.fun-coding.org/crawl_basic2.html'>잔재미코딩</a>

