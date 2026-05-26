---
name: "3DTilesRendererJS"
slug: "three-tiles-renderer"
category: "VIZ_TWIN"
summary: "Three.js 에서 3D Tiles 스트리밍"
github: "https://github.com/NASA-AMMOS/3DTilesRendererJS"
license: "Apache-2.0"
language: "JavaScript"
korean_applications:
  - "Cesium 의 글로브 컨텍스트 없이도 Three.js 기반 BIM 뷰어에 도시 3D 데이터 스트리밍"
  - "디지털 트윈 사내 도구를 Three.js 로 자체 개발할 때 OGC 3D Tiles 표준 데이터 직접 활용"
added: 2026-05-25
---

NASA AMMOS 가 유지하는 OGC 3D Tiles 표준 Three.js 렌더러. ★2.3k.

3D Tiles 는 대용량 도시 모델 (포토그라메트리 / 메시 / 점군) 의 스트리밍 표준. 보통 Cesium 의 globe 렌더링과 함께 쓰이지만, 이 라이브러리는 *순수 Three.js 위에서* 동일 데이터를 렌더링한다.

용도: 글로브 (지구 구) 가 필요 없는 디지털 트윈 도구. xeokit 의 IFC 강점 + 3D Tiles 의 도시 메시 강점을 같이 쓰고 싶을 때 어댑터.

Three.js / Babylon.js / r3f (React Three Fiber) 모두 지원.

한국 디지털 트윈 사업의 Three.js 기반 사내 뷰어 (Cesium 종속 회피) 가 OGC 3D Tiles 데이터를 받아야 할 때 가장 적합.
