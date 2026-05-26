---
name: "HollowRC"
slug: "hollowrc"
category: "STRUCTURE_SIM"
summary: "중공 철근콘크리트 단면 설계 / 검토"
github: "https://github.com/kleissl/HollowRC"
license: "GPL-3.0"
language: "Python"
korean_applications:
  - "교각 / 콘크리트 박스 거더 등 *중공 RC* 단면의 결합 하중 (축력 + 휨 + 비틂 + 전단) 검토"
  - "Eurocode 2 기반이라 KDS 14 20 50 와 매핑하여 한국 식 사내 도구로 포팅"
added: 2026-05-25
---

코펜하겐 공대 Niels Kleissl 이 만든 *중공 RC 단면* 전용 설계 / 검토 Python 도구. ★32.

핵심 가치: 일반 RC 가 아닌 *중공 단면* (Box / Hollow) — 교각, 박스 거더, 옹벽 헤드 등의 결합 하중 (N + M + V + T) 검토.

Eurocode 2 기반. 일반 FEM 도구 (Pynite, OpenSees) 가 *해석* 이라면 HollowRC 는 *단면 검토* 전문.

GUI 도 있어 학습 곡선 작음. Python API 로 자동화도 가능.

한국 토목 (도로공사, 한국철도) 의 교각 / 박스 거더 검토 자동화에 적합. 한국 KDS 식 포팅 후 사내 도구화.
