#  여기서는 주피터가 아니라 vscode로 넘어간다. 서버를 생성할것이다 
# 아나콘다에서 vs코드 런처를 실행한다. 
# 그리고 아나콘다 콘솔 창에서 패키지 flask가 설치되어있는지 확인한다 

#---------------------------------------------------------------

#엔트리 포인트 ->  여기서부터 경로를 따진다
#1. 모듈가져오기 
from flask import Flask
#2. flask 객체 생성 
app = Flask(__name__)
#3.라우팅
#~/요청하면 home() 함수가 응답 (return)
@app.route('/')
def home(): 
    return '<b>helloworld</b>'
#4. 서버가동 
if __name__=='__main__':
# 조건문 이하 코드는 run.py직접 구동될때만 작동 
    app.run(debug=True)
