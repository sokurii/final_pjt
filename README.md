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
*   정기예금, 정기적금 json 파일에 Nested Relationship 적용(Depositoptions, SavingOptions)
*   환율계산기 View 구현(최소한의 화면만 구현, 기능은 아직 X)
*   기타 CSS 약간 수정
*   로그인, 회원가입 기능 구현
     *   회원가입 기능, 비밀번호 변경은 토큰이 잘 받아지는 것 확인
     *   로그인은 현재 axioserror가 발생하여 원인을 찾아봐야함
     *   AllowAny상태에서 게시물 전체 조회, 게시물 생성에 대해 permission IsAuthenticated 데코레이터를 적용하여 headers에 Token을 정상적으로 기입했음에도 인증이 되지 않는 문제 발생

#### 23-05-18

*   로그인, 회원가입 관련 디버깅
     * 게시물 전체 조회, 게시물 생성(해결완료) -> settings에서 'DEFAULT_AUTHENTICATION_CLASSES'를 추가하지 않아 발생한 문제였음
     * 로그인, 회원가입(해결완료) -> 교안을 참고한 결과 payload후 mutations에서 id 변수명을 username으로 해야 정상적으로 진행되는 걸 알게 됨
     * 커뮤니티 게시판 진입 시 로그인되지 않으면 팝업이 생기게 하고 싶지만 뜨지 않음(해결중)

*   금융상품비교 화면 구현
     *   axios 요청으로 전체 금융상품 조회하여 화면에 올리기는 성공
     *   특정 금융상품명 클릭 시 상세 조회 페이지로 넘어가기 성공 -> 상세 내용 화면에 나타내기 (완료)
     *   백엔드에서 특정 상품 상세조회를 만들지 않아 제작해야함 -> 코드 작성 및 테스트 (완료)
     *   은행별 금융상품 조회 기능 구현 (완료)

*   지도
     * 광역시/도 선택 시, 해당 광역시/도에 맞는 행정구역이 나오게 구현 성공
     * 광역시/도, 시/군/구, 은행명에 해당하는 지도 검색 결과 구현하기(예정)

*   환율
     * api로 받은 환율 데이터 목록 화면에 구현하기(예정)

*   기타
     * 진희가 만든 코드랑 일부분 합치기 -> App.vue(NavBar, FootBar 적용 포함), HomeView.vue, LoginView.vue merge 완료
