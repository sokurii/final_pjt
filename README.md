### commit할 때마다 변경사항 commit message로 써놓기!!!

## 사전 준비

### 1) Back-End(Django)

1.   final-pjt-back 폴더 이동 후 venv 설치 및  활성화

     ```bash
     (폴더 미이동 시) cd final-pjt-back
     python -m venv venv
     source venv/Scripts/activate
     ```

2.   requirement 설치

     ```bash
     pip install -r requirements.txt
     (작업 중 설치 파일 추가 시) pip freeze > requirements.txt
     ```

3.   (필요 시) migrate 진행

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

4.   서버 켜기

     ```bash
     python manage.py runserver
     ```



### 2) Front-End(Vue)

1.   final-pjt-front 폴더 이동 후 node_modules 설치

     ```bash
     (폴더 미이동 시) cd final-pjt-front
     npm install
     ```

2.   서버 켜기

     ```bash
     npm run serve
     ```



## 개발일지

#### 23-05-15

*   프로젝트 구상(컴포넌트 뷰 등)
*   전체적인 웹 틀 만들기
*   API 활용하여 카카오 맵 웹 화면 구현 테스트

#### 23-05-16

*   HomeView → Carousel 구현 시도(제대로 구현되지 않아 수정 필요)
*   로그인 화면, 회원가입 화면 구현(router-link 활용하여 회원가입 클릭 시 화면 이동도 성공, 기능은 아직 추가X)
*   API 활용하여 정기예금 자료 요청 테스트 → 성공하여 정기적금도 시도 예정

#### 23-05-17

*   정기예금, 정기적금, 환율 model 생성 및 api 데이터 요청
*   환율계산기 View 구현(최소한의 화면만 구현, 기능은 아직 X)
*   로그인, 회원가입 기능 구현(예정) -> 오늘 안에 무조건!!!!
*   기타 CSS 약간 수정(예정)
