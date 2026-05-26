---
name: "iTowns"
slug: "itowns"
category: "VIZ_TWIN"
summary: "Three.js 위 3D 지오스페이셜 프레임"
github: "https://github.com/iTowns/itowns"
license: "MIT / CeCILL-B"
language: "JavaScript"
korean_applications:
  - "Cesium 의 글로브가 필요 없는 *도시 단위* 디지털 트윈 (Three.js 친화 사내 도구)"
  - "프랑스 IGN 활용 사례 참조 — 한국 NGII 데이터로 *국가 단위 지리정보 플랫폼* 구축"
added: 2026-05-25
---

프랑스 IGN (국토지리정보원) + CNES (우주청) 가 주도하는 Three.js 위 *3D 지오스페이셜 시각화* 프레임. ★1.2k.

Cesium 의 *글로브 중심* vs iTowns 의 *Three.js 자유*. 도시 / 광역 (글로브 필요 없는 영역) 에서 Three.js 자유도 가지고 위경도 좌표 다룬다.

3D Tiles 표준 import + 정사영상 + DEM + 벡터 데이터. 좌표계 변환은 proj4js 내장.

3DTilesRendererJS 보다 더 무거운 풀 프레임. Three.js + r3f 사내 코드와 통합 쉬움.

한국 NGII / 지자체의 *국가 단위 지리 시스템* 구축 시 IGN 사례 참조 가치 큼. Cesium 대비 Three.js 친화.
