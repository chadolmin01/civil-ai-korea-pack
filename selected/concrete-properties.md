---
name: "concrete-properties"
slug: "concrete-properties"
category: "STRUCTURE_SIM"
summary: "RC 단면 특성 자동 계산"
github: "https://github.com/robbievanleeuwen/concrete-properties"
license: "MIT"
language: "Python"
korean_applications:
  - "한국 KDS 14 20 50 (콘크리트 철근상세) 의 *RC 단면* 휨 / 축력 / 모멘트-곡률 자동 계산"
  - "section-properties (일반 단면) 와 짝지어 한국 RC 설계 자동화 라이브러리 구축"
added: 2026-05-25
---

호주 Robbie van Leeuwen 의 *철근콘크리트 (RC) 단면 전용* Python 라이브러리. ★229. section-properties 의 자매.

핵심: RC 단면의 *철근 + 콘크리트* 결합 거동 계산. 모멘트-축력 (M-N) 상관도, 모멘트-곡률 (M-φ), 응력 / 변형률 분포, 균열 / 단면 분석.

section-properties 가 *일반 단면* (강재 H, 박스, 트러스) 이라면 concrete-properties 는 *RC 단면 전용*.

Eurocode 2 기반 — 한국 KDS 14 20 50 으로 포팅 자연스러움. 사내 RC 설계 자동화의 핵심 컴포넌트.

학습 자료 풍부 (Jupyter 노트북 예제) — 학생 / 입문자도 접근 가능.

한국 콘크리트 설계 (교량 PSC 거더, 옹벽, 박스 컬버트 등) 자동화 도구의 표준 단면 계산기.
