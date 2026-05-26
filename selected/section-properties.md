---
name: "section-properties"
slug: "section-properties"
category: "STRUCTURE_SIM"
summary: "임의 단면의 FEM 단면 특성 계산"
github: "https://github.com/robbievanleeuwen/section-properties"
license: "MIT"
language: "Python"
korean_applications:
  - "H-beam / 박스단면 / 복합단면 등 한국 표준 부재의 단면 특성 자동 산정 (Ix, Iy, Sx, J)"
  - "Pynite 와 짝지어 *단면 → 골조 해석 → 결과* 흐름을 한 Python 파이프라인으로"
added: 2026-05-25
---

호주 Robbie van Leeuwen 이 만든 *임의 단면* 의 단면 특성 + 응력 / 변형률 계산 Python 라이브러리. ★530.

FEM 기반으로 단면 형상이 어떤 비대칭 / 곡선 / 복합단면이라도 정확한 단면 특성 계산. 일반 표준 단면 (I, H, 박스, 원형) 은 헬퍼 함수 한 줄.

Pynite (3D FEM 골조) + section-properties (단면) 조합이 *Python 으로 끝나는 구조 해석* 의 한국 적용 표준 쌍.

학술 / 사내 사용 모두 인용 / 추적성 강함.

한국 구조 설계사 / 컨설팅 / 학술 연구가 복잡한 단면 (특히 RC + 강재 복합) 의 정확한 단면 특성을 코드로 자동 산정할 때 필수.
