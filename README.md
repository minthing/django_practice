##### django 실습

##### 초기 세팅
* 장고 : 2.0.1버전
* python3 : 이미 깔려 있음
* 위치 : `facebook_django > facebookclone`

1. 가상환경 설치 : `python3 -m venv myvenv`
2. 가상환경 실행 : `source myvenv/bin/activate`
3. pip 최신 버전으로 유지 : `python3 -m pip install --upgrade pip`
4. 장고 설치 (실습 버전 통일을 위해 다운그레이드) : `pip install django~=2.0.1` => `python manage.py --version` 버전 확인해보면 3.0.14라고 나옴 🤨 (저 분명 다운그레이드 했거든요...?)
5. 프로젝트 만들기 : `django-admin startproject 당신의프로젝트이름 .`
데이터 베이스는 sqlite3로 미리 설정 되어 있음 -> 데이터 베이스 설치 : `python manage.py migrate`
포트 변경 매번 수동으로 해줘야 하는듯 `python manage.py runserver 8080`
6. html 파일은 `appname > templates > appname` 아래에 작성한다.

##### 210724 (토)
- 새로운 앱을 만들 때에는 `python manage.py startapp 앱네임`
- `OperationalError at /admin/login/` : migrate 안 해줘서 생기는 에러
- `path('accounts/', include('accounts.urls')),` 여기서 `/` 빼먹었다가 에러남 🥲 주의하자

##### 210725 (일)
- `pip install django-allauth` : 인증 관련 패키지
- `pip install django-imagekit & pillow` : 이미지 업로드 관련 패키지
