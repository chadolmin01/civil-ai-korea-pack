---
name: "mapshaper"
slug: "mapshaper"
category: "SURVEY_GIS"
summary: "SHP/GeoJSON/TopoJSON 편집·간소화"
github: "https://github.com/mbloch/mapshaper"
license: "MPL-2.0"
language: "JavaScript"
korean_applications:
  - "한국 지자체 / 국토부 SHP 데이터의 *간소화 + 정리 + 형식 변환* (QGIS 무거움 회피)"
  - "웹 GIS / Cesium / Mapbox 용 GeoJSON / TopoJSON 빌드 전처리"
added: 2026-05-25
---

Matthew Bloch 가 만든 벡터 GIS 데이터 *편집 / 단순화 / 변환* 도구. ★4.1k.

웹 GUI (mapshaper.org) + CLI 양쪽. Shapefile / GeoJSON / TopoJSON / CSV 입력 → 동일 포맷 출력 + 간소화 (Visvalingam / Douglas-Peucker) + 필터 / 머지 / 분할.

웹 지도용 *경량화* 가 강점 — 수십 MB SHP 를 *시각적으로 동등* 한 수백 KB GeoJSON 으로 압축.

QGIS 의 *전체 GIS 분석* 이 부담일 때 *전처리 한 단계* 만 필요한 흐름에 적합.

한국 국토부 / 지자체 SHP 데이터 (행정구역, 도로망, 지적) 의 웹 호환 전처리에 사실상 표준 도구.
