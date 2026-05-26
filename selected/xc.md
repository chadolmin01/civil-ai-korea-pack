---
name: "XC (xcfem)"
slug: "xc"
category: "STRUCTURE_SIM"
summary: "토목 구조물 전용 C++/Python FEM"
github: "https://github.com/xcfem/xc"
license: "GPL-3.0"
language: "C++ / Python"
korean_applications:
  - "교량 / 옹벽 / 토류벽 등 토목 구조물의 비선형 해석 (Pynite 의 일반 골조 한계 초과)"
  - "내진 / 토압 / 수압 등 복합 하중의 다중 시나리오 일괄 해석"
added: 2026-05-25
---

스페인 Luis C. Pérez Tato 가 시작한 *토목 구조 전용* C++ + Python FEM 패키지. ★352.

OpenSees 가 지진공학 연구 / 학계 강점이라면, XC 는 *토목 실무* (교량, 옹벽, 토류벽, 펌프 스테이션 등) 의 일상 해석 자동화에 더 초점.

C++ 코어 + Python 인터페이스. 비선형 부재 / 콘크리트 / 강재 / 토류 / 액체 압력 등 토목 특화 모델.

Eurocode 식 자동 검토 모듈 내장 — structuralcodes 와 조합하면 한국 KDS 식으로 포팅 가능.

학습 곡선 큰 편 (OpenSees 와 유사) — 사내 1명 전담 후 사내 표준 템플릿화 흐름이 적합.

한국 토목 구조 (교량, 옹벽, 사면) 전용 정밀 해석 + 자동화에 적합. Pynite (일반) / OpenSees (지진) 와 보완 관계.
