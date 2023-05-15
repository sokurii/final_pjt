# 사전 준비

## 1) Back-End(Django)

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



## 2) Front-End(Vue)

1.   final-pjt-front 폴더 이동 후 node_modules 설치

     ```bash
     (폴더 미이동 시) cd final-pjt-front
     npm install
     ```

2.   서버 켜기

     ```bash
     npm run serve
     ```