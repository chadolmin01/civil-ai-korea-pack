---
name: "Turf.js"
slug: "turf"
category: "SURVEY_GIS"
summary: "브라우저 지오스페이셜 분석 엔진"
github: "https://github.com/Turfjs/turf"
license: "MIT"
language: "TypeScript / JavaScript"
korean_applications:
  - "현장 점검 웹앱에서 GPS 좌표 → 시설물 거리 / 영역 / 교차 즉시 계산"
  - "발주처 검토 웹 GIS 의 폴리곤 buffer / intersect 등 분석을 클라이언트에서"
added: 2026-05-25
---

Mapbox 가 시작한 JavaScript 지오스페이셜 분석 모듈 라이브러리. ★10k.

GeoJSON 입력 → 거리 / 영역 / buffer / intersect / convex hull 등 100+ 알고리즘. 함수 단위 import 로 번들 크기 작게 유지 가능.

브라우저 단독 + 서버 (Node) 양쪽 동작. Cesium / Leaflet / MapboxGL 등 모든 웹 지도 라이브러리와 결합.

PostGIS / GeoPandas 가 서버 / 데이터 처리용이면, Turf 는 *클라이언트 실시간* 분석 영역.

한국 현장 점검 / 발주처 검토 웹앱이 GPS 좌표 기반 즉시 계산 (시설물 거리, 작업 구역, 영역 교차) 을 클라이언트에서 처리하고 싶을 때 사실상 표준.
