채집 메크로 연습 프로젝트

GatheringMacro/
├── main.py                      # 전체 실행 흐름 제어
├── capture_coords.py            # 좌표 수집 (Toplevel GUI)
├── get_interval.py              # 주기 입력 팝업
├── .gitignore                   # Git 제외 파일 설정
├── requirements.txt             # 설치 필요한 패키지 목록
├── screen.png                   # 캡처 이미지 (Git에 포함 안됨)
├── services/
│   ├── __init__.py              # (선택) 패키지화 표시용
│   ├── click_actions.py         # 각 세트의 자동화 동작 정의
│   └── macro_runner.py          # 반복 실행 + 중단 로직
└── venv/                        # 가상환경 (Git 제외 대상)
