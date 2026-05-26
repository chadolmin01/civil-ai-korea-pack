---
name: "3D Tiles 표준"
slug: "3d-tiles-spec"
category: "VIZ_TWIN"
summary: "대용량 3D 도시 데이터 스트리밍 표준"
github: "https://github.com/CesiumGS/3d-tiles"
license: "Apache-2.0"
language: "Specification"
korean_applications:
  - "서울 / 부산 단위 도시 디지털 트윈의 대용량 메시 / 점군 / 모델 효율 전송"
  - "공공 데이터 (NGII) 의 3D 데이터를 표준 형식으로 발주 → 다양한 뷰어 호환"
added: 2026-05-25
---

OGC 가 정식 표준화한 *대용량 heterogeneous 3D 지오스페이셜 데이터 스트리밍* 사양. ★2.5k.

원래 Cesium 이 만들어 OGC 에 기증. 도시 단위의 수십 GB 모델 / 포토그라메트리 메시 / 점군을 *공간 인덱싱 + LOD 분할* 로 클라이언트가 보이는 영역만 다운로드.

3D 모델은 glTF 기반, 메타데이터는 JSON, 좌표는 ECEF (지구 중심) — 어떤 클라이언트도 같은 데이터 사용 가능.

CesiumJS / xeokit / Three.js (3DTilesRendererJS) / Unreal / Unity 모두 지원.

한국 디지털 트윈 발주 시 *표준 데이터 형식* 으로 지정하면 발주처 / 운영자 / 다양한 뷰어 호환성 확보. NGII / 국토정보플랫폼의 3D 데이터 표준화에 적합.
