# Autofolio 

2019 멋사 중앙 해커톤 프로젝트입니다.

## installation

본 프로젝트는 gitignore에서 db 관련 정보를 모두 배제해두었으므로 마이그레이트 과정이 필수 입니다.

~~~
// 설치 
pip install -r requirements.txt && 
python manage.py makemigrations && 
python manage.py migrate
~~~

