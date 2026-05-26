---
name: "three-mesh-bvh"
slug: "three-mesh-bvh"
category: "VIZ_TWIN"
summary: "Three.js 메시 BVH (raycast 가속)"
github: "https://github.com/gkjohnson/three-mesh-bvh"
license: "MIT"
language: "JavaScript"
korean_applications:
  - "대용량 BIM 모델 (수만 부재) 의 객체 클릭 / 호버 / 단면 응답 속도 개선"
  - "사내 Three.js 기반 BIM 뷰어의 *공간 질의* (충돌 검출 / 가시성 / 영역 선택) 가속"
added: 2026-05-25
---

Garrett Johnson 이 만든 Three.js 메시의 *BVH (Bounding Volume Hierarchy)* 구축 + 활용 라이브러리. ★3.4k.

Three.js 의 기본 raycast 는 모든 삼각형 순회로 *O(n)* — 100만 폴리곤 메시에서 클릭 한 번이 수백 ms 걸림. BVH 로 *O(log n)* 까지 단축.

활용: 모델 클릭 응답, 호버 하이라이트, 단면 (clipping), 부재 거리 측정, 충돌 검출, 영역 선택 등 *공간 질의* 전반.

xeokit / web-ifc / iTowns / 사내 Three.js 뷰어 모두 이 라이브러리를 백엔드로 도입할 수 있음.

한국 대형 BIM (공항 / 발전소 / 광역 인프라) 사내 뷰어의 *반응성 병목* 해결책.
