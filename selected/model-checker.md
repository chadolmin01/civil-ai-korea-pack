---
name: "Model Checker"
slug: "model-checker"
category: "SPEC_REVIEW"
summary: "브라우저에서 IDS 기반 IFC 검수"
github: "https://github.com/opensource-construction/model-checker"
license: "Apache-2.0"
language: "TypeScript"
korean_applications:
  - "감리법인이 발주처 출장 없이 현장에서 IFC 즉시 검수"
  - "한국형 IDS 템플릿을 사내 위키에 배포해 발주-설계-시공 공통 규약화"
added: 2026-05-25
---

opensource-construction 커뮤니티가 만든 브라우저 기반 IFC + IDS 검증 웹앱.

WASM 으로 처리하기 때문에 파일이 서버로 전송되지 않는다. 발주처 / 감리가 보안 부담 없이 현장에서 모델을 검토할 수 있다.

IDS (Information Delivery Specification) 표준에 따라 "어떤 객체에 어떤 속성이 어떤 값으로 있어야 하는지" 를 선언적으로 작성하고, 위반 항목을 시각화한다.

buildingSMART validate 와 같은 IDS 표준을 따르므로 규칙 자산을 공유할 수 있다.

발주처 / 감리법인이 현장에서 즉시 검수 도구가 필요할 때.
