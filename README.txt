1. 파이썬 기반의 데이터 과학 프로젝트
  - 데이터 분석및 수집 
  - 전처리
  - 적제
  - 분석 
  - 시각화
  - 머신러닝
  - 딥러닝 (AI 약한)

  2. git 를 이용한 공정 관리
 - github.com 가입및 로그인
 - git-scm.com 다운로드및 설치
    설치시 editor를 vs code로 적용 
 - github에 new > repogitory 생성
    생성시  readme, .gitignore (python)으로 체크및 생성
 - 로컬PC 프로젝트를 만들 위치에서
   public 이면
   $ git clone https://github.com/username/py_projects.git
   private 이면
   $ git clone https://username:password@github.com/username/py_projects.git
   간혹, 로그인 윈도우가 뜨면 거기서 다시 아이디 비번 넣어서 로그인하면됨
 - github.com 가입 및 로그인 
 - git-scm.com 다운로드 및 설치 
    설치시 editor를 vs code로 적용  
 - github에 new > repogitory 생성 
    생성시  readme, .gitignore (python)으로 체크및 생성 
 - 로컬PC 프로젝트를 만들 위치에서 
   > public 이면 
        $ git clone https://github.com/username/프로젝트이름.git 
   > private 이면 
        $ git clone https://username:password@github.com/username/프로젝트이름.git 
          간혹, 로그인 윈도우가 뜨면 거기서 다시 아이디 비번 넣어서 로그인하면됨

만약, 프로젝트를 먼저 작업하다가, git를 사용한 경우
   1) git clone을 다른 위치에서 수행
   2) clone를 통해 만들어진 위치에 먼저 만들어진 프로젝트 내용을 이동시킴
   3) vs code 에서 커밋(commit) and push 작업을 진행하면된다
   4) 단, 최초 수행시  git 오류가 나올수 있고, 이경우
     $ git config --global user.name "bongseop2822"
     $ git config --global user.email "bongseop2822@gmail.com"
     1회 수행해 주면(현재 프로젝트 위치에서) 처리된다
   5) 앞으로는 clone 한 프로젝트 위치가 실제 작업할 곳이 된다

         [윈도우상 서버 동기화 시킬때]  
         > 깃 주소를만들고  
         : username.github.io 
         >$ git clone username.github.io (주소를 끌어와야한다.) 
         >$ cd username.github.io 
         >$ git remote remove origin 
         >$ git remote add origin https://github.com/username/username.github.io.git 
         >$ git push -u origin master

 

 

 

** Git 용어 (수정 필요)

- Commit 
   수정 사항을 로컬에 저장하는것
   Commit을 쌓아두면 나중에 히스토리를 활용하고 보기에 좋다. 
   하지만 어디서 내 저장소를 Fork해 갈지 모르기 때문에 되도록 영어로 작성하면 좋다.
-Push 
   로컬에 저장한 수정 사항을 저장소로 보낸다. Commit과 Push는 한 번에 할 수 있다. 
-Pull 
   다른 사람이 저장소에 보낸 수정 사항을 내 로컬 파일에 적용한다. 협업할때 많이 사용 
-Branch 
   하나의 파일을 가지(Branch)를 치듯 나눠서 작업하는 방식을 ‘Branch를 나눠서 작업한다’ 고 한다. 예를 들어 아이콘만 다르고 나머지 요소는 같은 A, B, C UI 화면이 있다. 이때 디자인 툴에서는 A, B, C 세 개의 레이어를 추가해서 작업할 것이다. 개발에서는 A, B, C 3개의 Branch를 만들어서 아이콘만 다르게 작업할 것이다. 
   보통 Jekyll 블로그를 운영할 때는 아직 Master Branch에 Push하기5에는 부족하지만 수정 사항을 기록하고 싶은 글을 작성할 때 Branch를 나눠놓는다. 
-Merge 
   Branch를 나눌 수 있다면 합치는 과정도 필요하다. 이를 Merge라고 한다. Merge하는 과정에서 충돌이 있을 수 있다. 이런 충돌을 Conflict라고 한다. 에버노트를 쓸 때 발생하는 충돌과 비슷하다. 같은 노트인데 두 곳에서 수정했을 때, 어떤 노트를 유지할지 노트 내용을 보면서 하나씩 결정하는 게 Merge라고 보면 된다. 협업을 많이 하지 않는 이상 Conflict는 거의 겪을 일이 없다. 
-Stash 
   수정 사항들을 잠시 다른 곳에 보관하는 기능이다. 다양한 용도가 있겠지만 나 같은 경우 Master가 아닌 Branch에서 작업하다가 Master에만 푸시할 내용이 생길 때 주로 사용했다.

 