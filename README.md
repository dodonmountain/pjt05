# 05 - CRUD by Django

## Django와 Python을 통한 Web app 제작

>requirements.txt -> 사용된 외부 라이브러리 기록



### 1. 요구 사항

* Class name `Movie`에 다음 정보 저장

| 필드명      | 자료형  | 설명              |
| ----------- | ------- | ----------------- |
| title       | String  | 영화명            |
| title_en    | String  | 영화명(영문)      |
| audience    | Integer | 누적 관객수       |
| open_date   | Date    | 개봉일            |
| genre       | String  | 장르              |
| watch_grade | String  | 관람등급          |
| score       | Float   | 평점              |
| poster_url  | Text    | 포스터 이미지 URL |
| description | Text    | 영화 소개         |

* 영화 목록(index.html)
* 영화 정보 입력 폼(movies/new/)
* 영화 정보 생성 url(movies/create/)
* 영화 정보 조회 `detail`
* 영화 정보 수정 
* 영화 정보 삭제 `delete`

 ### 2. 세부 정보

* base.html에서 extend하여 페이지 작성
  * base.html에 bootstrap, font-awesome 등 외부 스크립트 로드
* Form 간 정보 전송은 POST 메소드 사용
  * { csrf_token }
* Django에서 제공하는 DB `sqlite` 사용. (로컬 파일 형태)
* csv파일을 로드 (구글링), 하지만 내부 정보는 두 개 뿐이었다.(실망)

### 3. 개선점

* 대용량의 데이터베이스가 필요.
* 크롤링과 파싱으로 구현할 수 있을듯
* 로그인 폼, 소셜 댓글 등 기본적인 기능 구현 방법 숙지 필요
* 부트스트랩이 아니라 css 한땀 한땀 구현해보는 시간을 가져야 할것
* A형 시험이 끝나고 블로그 제작할 때 django 사용해보기