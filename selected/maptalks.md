---
name: "maptalks.js"
slug: "maptalks"
category: "SURVEY_GIS"
summary: "2D/3D 통합 지도 JavaScript 라이브러리"
github: "https://github.com/maptalks/maptalks.js"
license: "BSD-3-Clause"
language: "JavaScript / TypeScript"
korean_applications:
  - "지자체 / 발주처 GIS 웹앱에서 *2D 평면도 + 3D 모델* 동시 표현 (kepler.gl 의 3D 대안)"
  - "가벼움 + 플러그인 구조 — 사내 도구 통합 시 부담 작음 (Cesium 보다 가벼움)"
added: 2026-05-25
---

maptalks 팀이 만든 *2D + 3D 통합* 지도 JavaScript 라이브러리. ★4.5k.

OpenLayers / Leaflet 가 2D 전용, Cesium 이 3D 글로브 특화라면, maptalks 는 *2D 와 3D 한 캔버스* — 평면도와 3D 건물 / 지형 동시 표현.

플러그인 구조: 코어는 가볍고 (~수십 KB), 필요한 기능 (3D / 클러스터 / 히트맵 / VT) 만 추가.

Three.js 통합 플러그인 (`maptalks.three`) 으로 Three.js BIM 객체를 지도 위에 직접 렌더링.

한국 지자체 GIS 웹앱이 *평면도 + 3D 건물* 모두 표현해야 할 때, Cesium 의 글로브 부담 없이 사용. 플러그인 구조라 사내 도구 통합 부담 작음.
