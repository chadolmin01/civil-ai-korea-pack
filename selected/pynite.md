---
name: "Pynite"
slug: "pynite"
category: "STRUCTURE_SIM"
summary: "Python 3D 구조 유한요소 해석"
github: "https://github.com/JWock82/PyNite"
license: "MIT"
language: "Python"
korean_applications:
  - "사내 표준 거더교 / 트러스 구조의 자동 해석 스크립트 작성"
  - "내진 검토를 위한 다중 시나리오 (지진 가속도 변화) 일괄 비교"
added: 2026-05-25
---

J. Wock 이 개인 프로젝트로 시작해 약 700 ⭐ 까지 성장한 3D 구조 FEM 라이브러리.

순수 Python (NumPy / SciPy / matplotlib) 으로 작성되어 의존성이 가볍고, ETABS / SAP2000 의 미니 버전이 필요한 자동화 작업에 적합.

`pip install PyNiteFEA[all]`. 부재 (member), 판 (plate), 절점 (node), 하중 조합, 비선형 옵션 (P-Δ) 지원.

OpenSees 가 지진공학 연구용이라면 Pynite 는 일반 구조 자동화용 — 학습 곡선이 훨씬 완만.

SectionProperties 와 짝지어 단면 특성을 계산하면 흐름이 자연스럽다.

한국 중소 설계사가 표준 검토 스크립트를 사내 자산으로 쌓아가려 할 때 첫 후보.
