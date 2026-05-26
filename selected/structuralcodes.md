---
name: "structuralcodes"
slug: "structuralcodes"
category: "STRUCTURE_SIM"
summary: "Eurocode 구조 계산을 Python 으로"
github: "https://github.com/fib-international/structuralcodes"
license: "Apache-2.0"
language: "Python"
korean_applications:
  - "Eurocode 식을 *템플릿* 으로 한국 KDS / KCS 식 사내 라이브러리 작성 (Blueprints 와 조합)"
  - "콘크리트 / 강재 부재 검토를 코드 단위로 자동화 (LaTeX / Markdown 검토서 자동 출력)"
added: 2026-05-25
---

fib (International Federation for Structural Concrete) 가 공식 유지하는 Eurocode 구조 계산 Python 라이브러리. ★273.

Blueprints 가 일반 토목 계산식 모음이라면, structuralcodes 는 *fib 공식* 표준 식 (Eurocode 2 / Model Code 2010 / FRP 보강 등) 구현체.

각 식이 단일 함수 + 입력 단위 (Pint) + 출처 인용 (fib bulletin 번호) 까지 박혀있어 검토 추적성 최상급.

한국 KDS (구조설계기준) 가 Eurocode 를 많이 따랐기 때문에 한국 식 사내 라이브러리 작성 시 *최고의 템플릿*.

구조 컨설팅 / 설계사 / 학술 연구의 사내 검토 코드 자산화 시 출발점.
