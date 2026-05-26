---
name: "buildingSMART Validate"
slug: "bsmart-validate"
category: "SPEC_REVIEW"
summary: "IFC 표준 준수를 공식 규칙으로 검증"
github: "https://github.com/buildingSMART/validate"
license: "MIT"
language: "Python"
korean_applications:
  - "조달청 BIM 납품 IFC 파일을 공식 buildingSMART 규칙으로 자동 사전 검수"
  - "사내 IDS (Information Delivery Specification) 를 한국형 요구사항으로 작성해 CI 에 통합"
added: 2026-05-25
---

buildingSMART International 이 직접 운영하는 IFC 검증 서비스의 오픈소스 버전.

Gherkin 형식 (BDD) 으로 규칙을 정의하고, IDS 1.0 표준에 따라 IFC 모델의 형식·구조·속성을 검사한다.

웹 서비스 (validate.buildingsmart.org) 와 동일한 엔진을 로컬에서 돌릴 수 있어, 사내 환경에 대용량 파일 (250MB+) 검증 파이프라인을 자체 구축 가능.

IFC2x3 / IFC4 / IFC4.3 모두 지원.

한국 발주처가 BIM 납품 검수 자동화 도구를 만들 때 가장 신뢰할 수 있는 출발점.
