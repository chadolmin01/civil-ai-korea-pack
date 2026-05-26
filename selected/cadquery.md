---
name: "CadQuery"
slug: "cadquery"
category: "CAD_DWG"
summary: "Python 으로 파라메트릭 3D 모델링"
github: "https://github.com/CadQuery/cadquery"
license: "Apache-2.0"
language: "Python"
korean_applications:
  - "표준 프리캐스트 부재 (PSC 거더, 측구, 옹벽 블록) 의 파라메트릭 자동 모델링 + STEP/IFC 출력"
  - "반복 부재 1000+ 개를 1 함수 + 파라미터 테이블 (CSV) 로 일괄 생성"
added: 2026-05-25
---

OpenCASCADE (OCCT) 위에 Python API 를 얹은 파라메트릭 3D CAD 프레임워크.

SolidWorks / Inventor 의 *코드* 버전. 함수 호출로 3D 객체 생성, 변수 → 일괄 변형 → STEP / DXF / IFC 출력.

코드로 정의되므로 git 으로 버전 관리 + diff 가 의미를 가짐. 설계 변경 이력을 commit 단위로 추적.

학습 곡선 있음 (OCCT 개념 이해 필요), 대신 한 번 익히면 대량 자동화가 압도적으로 빠름.

한국 토목 시공사 / 표준 시방서 작성팀이 표준 부재 카탈로그를 파라메트릭으로 정리해 BIM 라이브러리화할 때 강력. 자동화에 익숙한 BIM R&D 팀이 주요 사용자.
