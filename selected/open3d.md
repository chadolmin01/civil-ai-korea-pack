---
name: "Open3D"
slug: "open3d"
category: "SURVEY_GIS"
summary: "Python 친화 점군·메시 통합 처리"
github: "https://github.com/isl-org/Open3D"
license: "MIT"
language: "C++ / Python"
korean_applications:
  - "교량 / 터널 / 시설물 LiDAR 점군의 ICP 정합 + 변위 자동 검출"
  - "한국 토목 연구실의 점군 학습 데이터 가공 (필터링 / 다운샘플 / 라벨링)"
added: 2026-05-25
---

Intel Labs 가 시작해 ISL (Intel Smart Lab) 가 유지하는 모던 3D 데이터 처리 라이브러리. ★13.6k.

C++ 코어 + Python 바인딩 (pip 한 줄). PDAL 이 *파이프라인 처리* 강점이라면, Open3D 는 *대화형 처리 + 알고리즘 라이브러리* 강점.

핵심: 점군 + 메시 + RGB-D 모두 1급 시민. 정합 (ICP, FGR), 등록 (Registration), 분할 (Segmentation), 평면 / 구체 / 박스 추출, 텐서 기반 GPU 가속.

Jupyter 노트북 친화. matplotlib 처럼 시각화 한 줄 가능.

연구실의 점군 학습 데이터 가공, 한국 토목 현장의 시설물 변위 검출 (베이스라인 vs 정기 스캔 정합) 에 가장 폭넓은 선택지.
