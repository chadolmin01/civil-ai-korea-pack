---
name: "PDAL"
slug: "pdal"
category: "SURVEY_GIS"
summary: "포인트 클라우드의 GDAL — 파이프라인 처리"
github: "https://github.com/PDAL/PDAL"
license: "BSD-3-Clause"
language: "C++"
korean_applications:
  - "도로 / 교량 LiDAR 스캔을 KGD2002 좌표계로 변환·필터링·격자화"
  - "공항 / 항만 측량 결과를 BIM 모델과 정합 (registration) 하는 사내 파이프라인"
added: 2026-05-25
---

포인트 클라우드 (LiDAR / 사진측량) 처리의 사실상 표준 라이브러리. GDAL 이 래스터·벡터에서 하는 역할을 점군 데이터에서 한다.

C++ 코어 + Python 바인딩 (`pdal` PyPI). 포맷 변환 (LAS, LAZ, PLY, PCD, E57 등 30+), 좌표계 변환, 필터 (분류 / 노이즈 제거 / 격자화) 를 JSON 파이프라인으로 선언적으로 조합한다.

연관 프로젝트: `python` (PyPI 패키지). 단독으로 쓸 수 있음.

한국 측량·토목 분야에서 점군 데이터를 다루는 모든 사내 도구의 첫 의존성.
