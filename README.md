## 개발일지

### 23-05-15

- 프로젝트 구상(컴포넌트 뷰 등)
- 전체적인 웹 틀 만들기
- API 활용하여 카카오 맵 웹 화면 구현 테스트
- 웹 페이지 서비스 아이디어 회의 

### 23-05-16

- HomeView 레이아웃 및 디자인, 스크롤 내려 각 기능 버튼 클릭 시 해당 페이지로 이동되도록 구현 
     - 요소들을 원하는 위치에 나타내게 하는 것이 어려웠다. css나 bootstrap 다루는 것이 재밌었지만
     아무래도 상하좌우 가운데 정렬하는 법, 화면 크기에 따라 유연하게 바뀌는 반응형 웹 구현 등 더 익힐 부분이 많았다.
- 추가적으로 필요한 기능 아이디어 고민(로그인 후 서비스 이용 가능하도록 / HomeView 에서 최신 금융 뉴스 볼 수 있도록 크롤링 / 예적금 상품 상세 페이지에 사람들 코멘트나 게시글 달 수 있는 기능, 별점 시스템 / 상품 상세 페이지에 만기 시 받는 금액 계산기 )

### 23-05-17

- LoginView 레이아웃 및 디자인, 아이디 및 비밀번호 입력 창 생성. 
     - 배경이 조금 허전하고, 사소한 부분들이 신경쓰여서 여유가 된다면 조금씩 수정할 예정 
     - 역시나 화면 크기에 따라 폰트나 로그인 창이 반응형으로 되게 하고 싶은데 미완.. 
- 아이디 저장 체크박스 (미완.. 사유:로그인 기능 구현이 덜 되어서 어떻게 작동하는 지 테스트 안해봄!)

- 집 가서 해야할 일 : 
     - django에서 구현했었던 커뮤니티(CRUD) template을 vue에 옮기기 시도 
     - navbar 화면에 고정 
