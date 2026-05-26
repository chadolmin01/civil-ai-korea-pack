---
name: "proj4js"
slug: "proj4js"
category: "SURVEY_GIS"
summary: "좌표계 변환 (KGD2002 등)"
github: "https://github.com/proj4js/proj4js"
license: "MIT (Apache-2.0 듀얼)"
language: "JavaScript"
korean_applications:
  - "한국 표준 KGD2002 좌표계 ↔ WGS84 변환 (Cesium / OSM / 사내 BIM 연동 필수)"
  - "발주처 도면 (TM 중부원점) ↔ 위성 영상 (WGS84) 정합 자동화"
added: 2026-05-25
---

전 세계 좌표계 변환의 사실상 표준 PROJ 의 JavaScript 포트.

브라우저 / Node 양쪽 동작. WGS84 (위경도) ↔ UTM ↔ TM (한국 평면 직각좌표) ↔ EPSG 코드 기반 어떤 조합도 한 줄로 변환.

한국 표준 KGD2002 (EPSG:5179 등 한국 평면 직각좌표계) 의 변환을 별도 라이브러리 없이 표준 EPSG 코드로 호출.

지형 / 도면 / BIM / GIS 데이터의 좌표계가 다른 한국 토목 실무에서 *변환 단계의 사실상 의무 의존성*.

Cesium / web-ifc / Turf.js / xeokit 등 모든 웹 지오 라이브러리의 좌표계 매개체.
