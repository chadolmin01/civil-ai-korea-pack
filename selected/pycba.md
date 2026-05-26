---
name: "PyCBA"
slug: "pycba"
category: "STRUCTURE_SIM"
summary: "연속보 영향선 / 모멘트 해석"
github: "https://github.com/ccaprani/pycba"
license: "Apache-2.0"
language: "Python"
korean_applications:
  - "교량 거더 (PSC / 강합성) 의 활하중 영향선 + 최대 / 최소 모멘트 / 전단력 자동 해석"
  - "단순한 연속보 검토에서 Pynite 의 일반 골조 해석보다 빠르고 정확"
added: 2026-05-25
---

Colin Caprani (모나쉬 대학교 교수) 가 만든 연속보 (Continuous Beam Analysis) 전용 Python 라이브러리. ★80.

핵심: 영향선 (Influence Line) 분석 — 교량 / 연속보의 활하중 (이동하중) 효과를 한 줄로 계산. KDS 도로교 설계기준에서 *활하중 위치별 최대 응력* 평가에 핵심.

Pynite 의 일반 골조 해석으로도 가능하지만, 연속보 한 부재의 *영향선* 만 빠르게 보고 싶을 때 PyCBA 가 가벼움.

교과서적 문제와 한국 도로교 활하중 검토에 적합.

한국 교량 설계사 / 학술 연구의 *영향선 기반 검토* 자동화에 최적.
