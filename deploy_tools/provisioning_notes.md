신규 사이트 프로비저닝
==================

## 필요 패키지

* nginx
* Python 3
* Git
* pip 3
* virtualenv

CenteOs 에서 실행 방법 예:

	> sudo yum install nginx git python3 pyton3-pip
	> sudo pip3 install virtualenv

## Nginx 가상 호스트 설정

* nginx.template.conf 참조
* SITENAME 부분을 다음과 같이 수정 superlists-staging.neoffrost.iptime.org

## 폴더 구조:
사용자 계정의 홈 폴더가 /home/username 이라고 가정

/home/username
┗━━sites
	┗━━SITENAME
		┣━━database
		┣━━source
		┣━━static
		┗━━virtualenv