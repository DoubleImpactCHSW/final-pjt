## 팀 구성 및 역할

- 최치훈
    - 역할
        - Vue 프론트엔드 개발 전반

- 이성원
    - 역할
        - Django 백엔드 개발 전반

## 서비스 목표 및 실제 달성도

- 목표
    - 프로젝트 기본 명세 사항 전체 구현 및 창의적인 상품 추천 알고리즘 구현

- 일별 진행도
    - 2023.05.17
        - 치훈
            - 회원 관련 View 구현
                - SignUpView
                - LoginView
        - 성원
            - 회원 커스터마이징
                - 회원 가입, 로그인, 로그아웃
            - 게시판
                - 게시글 CRUD
                - 댓글 CRD
    - 2023.05.18
        - 치훈
            - 게시판 구현
                - ArticleView
        - 성원
            - 예적금 상품 목록 DB 저장
            - 상품 전체 조회 및 상세 조회
            - 상품 가입
    - 2023.05.19
        - 치훈
            - 환율 불완전 구현
                - ExchangeView
            - 게시글 및 댓글에 작성자 표시, 작성자만 삭제 가능하도록 구현
            - BankMapView (지도) 구현
        - 성원
            - 프로필 api Read 구현
            - 관리자가 금리 변경 시 이메일 발송 시도
    - 2023.05.22
        - 치훈
            - 상품 목록 조회 구현
                - ProductView
        - 성원
            - 프로필 정보 Update api
            - DB에 상품 목록 중복 저장 방지
    - 2023.05.23
        - 치훈
            - 디자인 작업 첫 시작
                - ExchangeView, BankMapView
        - 성원
            - dummy data 생성
            - age, money, salary가 비슷한 사람들이 가입한 상품 추천 알고리즘 구현
    - 2023.05.24
        - 치훈
            - 상품 추천 밸런스 게임 동작 구현
                - RecommendView
            - 전반적인 디자인 작업 추가
        - 성원
            - 상품 추천 밸런스 게임 알고리즘 구현
    - 2023.05.25
        - 치훈
            - 상품 추천 두 가지 모두 구현 완료
            - 디자인 마감
            - 마무리 디버깅
        - 성원
            - HomeView 디자인

## ERD

## 추천 알고리즘

- 내 정보 기반 자동 추천 알고리즘
    1. 나의 나이, 현재 가진 금액, 월 수익 데이터를 회원가입시 입력하지 않고 회원 수정 페이지에서 입력 함
    2. 현재 사용자의 정보와 다른 사용자들 정보 간의 피어슨 상관계수 계산 (이 때, 표본 크기는 1000으로 한다)
    3. 피어슨 상관계수가 가장 높은 사용자들을 가져옴 (10명)
    4. 이들이 가입한 상품들을 찾아서 가장 많이 가입한 상위 10개의 상품을 찾음

- 밸런스 게임 기반 추천 알고리즘
    - 밸런스 게임 선택지 마다 필터링 작용 후 남은 상품들 중에서 금리가 높은 상품 순으로 5개 추천

## 서비스 대표 기능

- 예적금 상품 추천 밸런스 게임
    - 쉬운 금융 서비스를 제공한다는 프로젝트의 목표하에, 누구에게나 친숙한 밸런스 게임만을 통해서 상품 추천을 받을 수 있도록 구현.
    - 밸런스 게임을 진행하면 선택 사항들에 맞게 필터링 된 추천 상품 목록 제안.
    - setTimeOut과 CSS Animation를 활용하여 게임 구현

## 시행착오

- 디버깅에 종종 어려움 경험
    - 쉽게 해결되지 않는 사항들은 항상 함께 대화하며 생각하고 해결

## 기술적으로 아쉬웠던 점

- 환율 정보 get api의 CORS 문제 미결 (Vue)

## 향후 공부하고 싶은 부분

- 치훈
    - Tailwind CSS 혹은 다양한 CSS 라이브러리 체험
    - Vue2와 달라진 Vue3의 장점
    - TypeScript
    - 역동적인 디자인 구현 방법

- 성원
    - SQL, ORM을 활용한 DB 조작하고 활용하는 방법
    - ERD 더 효율적으로 활용하는 방법


## 후기
- 치훈
    -
- 성원
    - 처음으로 웹 서비스 개발 프로젝트에 참여해서 목표한대로 결과물을 만들어냈다는거에 큰 뿌듯함을 느꼈다. 프로젝트 개발 도중 작고 큰 에러들을 확인하고, 혼자 해결하기 어려웠던 부분은 팀원과의 협력을 통해 문제를 해결하였다. 이 경험을 통해 같은 팀원과의 소통이 얼마나 중요한지 다시 한번 깨닫게 되었다. 그리고 개발 도중 부족했던 역량을 향후에 더 공부하여 보완하고 싶다는 생각을 하였다.