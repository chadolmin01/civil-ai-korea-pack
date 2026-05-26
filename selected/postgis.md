---
name: "PostGIS"
slug: "postgis"
category: "SURVEY_GIS"
summary: "PostgreSQL 위 공간 데이터 표준 엔진"
github: "https://github.com/postgis/postgis"
license: "GPL-2.0"
language: "C / PL/pgSQL"
korean_applications:
  - "지자체 / 공기업의 GIS 데이터 (지적, 도로, 시설물) 통합 사내 DB"
  - "QGIS / 사내 웹 GIS 의 공통 데이터 백엔드 (좌표계 변환, 공간 인덱스, 분석 함수)"
added: 2026-05-25
---

PostgreSQL 위에 공간 데이터 처리 능력을 더한 사실상 표준 익스텐션. ★2.1k.

공간 인덱스 (GIST), 좌표계 변환 (PROJ 내장), 거리/면적/교차 등 OGC SQL Simple Features 함수 1000+ 개, 토폴로지, 래스터 처리까지.

QGIS 의 *서버 측 짝꿍*. 한 사내 PostGIS DB → 여러 사용자가 QGIS / 웹앱 / Python (geopandas) 으로 동시 접근.

KGD2002 등 한국 좌표계는 proj4js 와 동일한 EPSG 코드 기반 변환 지원.

한국 지자체 / K-water / 한국도로공사 / 공기업의 GIS 인프라 백엔드 사실상 표준. ArcGIS Server / Oracle Spatial 대안.
