---
name: "CSFTools"
slug: "csftools"
category: "SURVEY_GIS"
summary: "LiDAR 점군에서 지표면 자동 추출"
github: "https://github.com/jianboqi/CSFTools"
license: "라이센스 명시 없음"
language: "Python"
korean_applications:
  - "산악지 LiDAR 데이터에서 식생 / 구조물 제거 후 DEM (수치표고모형) 생성"
  - "공사 진척 모니터링용 정기 드론 스캔에서 지표면만 추출 → 토공 물량 산정"
added: 2026-05-25
---

중국 지나칭화대 출신 jianboqi 가 만든 LiDAR 점군의 지표면 필터링 도구.

핵심 알고리즘은 Cloth Simulation Filter — 점군을 뒤집고 그 위에 "천" 을 떨어뜨려 지표면을 추출한다는 직관적 모델. 정확도가 높고 매개변수 조정이 단순.

PDAL 등 범용 라이브러리에도 CSF 필터가 내장되어 있지만, 이 Repo 는 원저자가 직접 구현·튜닝한 정밀 도구.

> 라이센스 명시 없음 — 사내 / 상용 활용 전 저자 (jianboqi) 에게 확인 필요.

토공량 산정, 사면 변위 모니터링, 산림 지표 추출 등 한국 토목 현장 LiDAR 작업의 1차 전처리.
