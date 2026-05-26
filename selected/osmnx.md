---
name: "OSMnx"
slug: "osmnx"
category: "SURVEY_GIS"
summary: "OpenStreetMap 도로망 분석 자동화"
github: "https://github.com/gboeing/osmnx"
license: "MIT"
language: "Python"
korean_applications:
  - "한국 시 단위 도로망의 토폴로지 / 연결성 분석 (재난 시 우회로, 응급차 도착 시간 시뮬레이션)"
  - "신규 도로 / 교량 설치 후 광역 통행시간 변화 사전 분석"
added: 2026-05-25
---

Geoff Boeing (USC 도시계획학과 교수) 가 만든 OpenStreetMap 도로망 분석 Python 라이브러리. ★5.6k.

OSM 데이터 다운로드 → NetworkX 그래프 변환 → 그래프 알고리즘 (최단경로, 중심성, 클러스터) 적용을 한 줄로 압축.

핵심 메서드: `graph_from_place("Seoul, South Korea", network_type="drive")` 한 줄이면 서울 차량 도로망 그래프 즉시 생성.

토목·교통 학술 논문에서 사실상 표준 도구. 학습 곡선 작고 시각화 (geopandas + matplotlib) 통합.

한국 지자체 교통계획 / 도시정비 부서가 광역 네트워크 분석을 사내 자산화할 때 첫 후보. ArcGIS / TransCAD 없이도 충분.
