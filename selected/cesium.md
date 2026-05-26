---
name: "CesiumJS"
slug: "cesium"
category: "VIZ_TWIN"
summary: "지구 규모 3D 디지털 트윈 렌더링"
github: "https://github.com/CesiumGS/cesium"
license: "Apache-2.0"
language: "JavaScript / TypeScript"
korean_applications:
  - "지자체 도시 디지털 트윈 (지형 + BIM + 도로 시설물) 광역 시각화 플랫폼"
  - "도로공사 / 한전 / K-water 의 광역 인프라 (노선 수십 km) 검토 + 발주처 보고"
added: 2026-05-25
---

미국 AGI (Analytical Graphics Inc.) 가 만든 지구 규모 3D 시각화 JavaScript 라이브러리.

Three.js 가 일반 3D 라면, Cesium 은 실측 좌표 (WGS84 위경도 + 고도) 기반의 *지구 규모* 3D 처리에 특화. double precision 으로 cm 단위 정밀도 유지.

지형 / 위성 영상 스트리밍, 3D Tiles (대용량 도시 모델), 시간축 시뮬레이션 (위성 궤도, 교통량 변화), CZML 데이터 형식 지원.

상업 클라우드 (Cesium ion) 와 분리되어 코어 라이브러리 자체는 Apache-2.0 무료. 자체 호스팅 가능.

한국 지자체 디지털 트윈 사업 (서울 S-Map 등), 광역 도로·교량 노선 검토, 발주처 보고용 광역 가시화의 사실상 표준.
