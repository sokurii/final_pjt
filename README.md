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
     * User model 성별(gender), 나이(age), 거주지(residence) 속성 추가

*   금융상품비교 화면 구현
     *   axios 요청으로 전체 금융상품 조회하여 화면에 올리기는 성공
     *   특정 금융상품명 클릭 시 상세 조회 페이지로 넘어가기 성공 -> 상세 내용 화면에 나타내기 (완료)
     *   백엔드에서 특정 상품 상세조회를 만들지 않아 제작해야함 -> 코드 작성 및 테스트 (완료)
     *   은행별 금융상품 조회 기능 구현 (완료)

*   지도
     * 광역시/도 선택 시, 해당 광역시/도에 맞는 행정구역이 나오게 구현 성공

*   환율
     * api로 받은 환율 데이터 목록 화면에 구현하기(예정)

*   기타
     * 진희가 만든 코드랑 일부분 합치기 -> App.vue(NavBar, FootBar 적용 포함), HomeView.vue, LoginView.vue, SignupView.vue merge 완료

#### 23-05-19

*   로그인/로그아웃 및 회원가입 기능 구현하기
     * User model 추가한 속성 바탕으로 회원가입 구현하기 -> 토큰 발급 확인 완료, 새로 추가된 속성(gender, age, residence)의 값이 DB에 저장되지 않는 현상 확인
     * AxiosError 발생 시(회원가입이 안될 시) 회원가입이 되지 않았다는 알림 및 사유 출력하기
       -> 조건별로 알림 문구 뜨게 만들어야 될 듯(아이디 최소 길이, 비밀번호 최소 길이 등)
     * 로그인이 안되어 있으면 로그인 링크만, 로그인이 되어있으면 로그아웃 및 프로필 링크만 뜨게 만들기 (완료)
     * 로그인이 안 된 상태에서 금융상품조회, 환율, 지도, 게시판 링크 클릭 시 '로그인이 필요한 서비스입니다.' 팝업 출력 후 로그인 페이지 이동 구현
          * router-link에서는 @click으로 이벤트가 발생하지 않아 검색해본 결과 @click.native를 붙여야 하는 것을 알게 됨
          * 미로그인 상태에서 HomeView에 있는 버튼 클릭 시 로그인 페이지 이동의 경우 router-link 태그가 아닌 button 태그로 설정해야 작동되는 것을 확인
          * 구현은 성공 했지만 간헐적으로 에러페이지가 반짝였다가 로그인 페이지로 이동하는 현상 발생 
          * 네비게이션 가드를 활용해야 할 듯

*   지도
     * 광역시/도, 시/군/구, 은행명에 해당하는 지도 검색 결과 구현하기(예정) 
          * MapSearchInput에서 얻은 키워드들을 KakaoMap으로 props하는데에는 성공
          * 이 props한 키워드들로 카카오맵 api 가이드 참고하여 구현 시도할 것

*   환율
     * api로 받은 환율 데이터 목록 화면(실시간 환율)에 구현하기 (완료) -> 예쁘게 배치해야함
     * 환율계산기 구현하기(예정)

#### 23-05-20

*   로그인 및 회원가입
     * 

*   금융상품조회
     * 정기적금 api 요청 완료
     * Tab기능 추가(정기예금 tab, 정기적금 tab)

*   환율
     * 비영업일(주말, 공휴일 등)의 경우 데이터 자료가 없는 것을 확인 -> 금요일 또는 공휴일 이전 영업일 날짜로 바꿔서 요청해야함

*   지도
     * 

*   게시판
     * 

*   프로필
     * 

---------------------------------------------

## 해결해야할 과제

#### 로그인/회원가입 관련

* 네비게이션 가드 활용하여 비로그인 상태일때 로그인 화면 전환
* 성별, 나이, 거주지 DB 저장 안되는 문제
* 비로그인 상태에서 로그인 페이지 이동 시 간헐적으로 반짝이는 에러 페이지 문제
* 아이디 저장 체크박스 클릭 시 이 후 로그인 화면으로 와도 아이디가 남아있게 만들기
* AxiosError 발생 시(회원가입이 안될 시) 회원가입이 되지 않았다는 알림 및 사유 출력하기
     -> 조건별로 알림 문구 뜨게 만들어야 될 듯(아이디 최소 길이, 비밀번호 최소 길이 등)

#### 금융상품비교

* ~~정기적금 api 불러오기~~
* 상세페이지에서 관심 상품 등록 기능 구현(프로필의 팔로우랑 같은 기능)
* 예치 기간 별 금리 나타내기
* (후순위) 상세페이지에서 만기시 금액 계산해주는 계산기 제작
* 예쁘게 배치하기

#### 환율

* 환율 계산기 제작

#### 지도

* 광역시/도, 시/군/구, 은행명에 해당하는 지도 검색 결과 구현하기

#### 커뮤니티

* 게시판 및 댓글 CRUD (전체 게시글 조회, 게시글 생성은 완료)

#### 프로필

* 유저 프로필 리스트 나열
* 유저 관심상품 등록 리스트 구현
* (가능하다면?) 상품 추천 알고리즘 제작

#### 기타

* View 및 Component 폴더 정리 (가능하다면 modules도 정리하여 폴더 제작하기)
* 진희가 만든 코드 합치기
* 남은 기간 만들 수 있는 기능 생각해보기
* CSS
* 발표 PPT 제작