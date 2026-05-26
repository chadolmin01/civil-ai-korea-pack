---
name: "web-ifc"
slug: "web-ifc"
category: "VIZ_TWIN"
summary: "브라우저에서 IFC 직접 파싱"
github: "https://github.com/ThatOpen/engine_web-ifc"
license: "MPL-2.0"
language: "TypeScript / C++ (WASM)"
korean_applications:
  - "발주처 검토용 IFC 뷰어를 별도 설치 없이 웹에서 제공"
  - "감리 보고서에 IFC 단면 / 속성 캡처를 자동 첨부하는 사내 도구"
added: 2026-05-25
---

That Open Company 가 만든 브라우저 네이티브 IFC 파서.

C++ 로 작성된 핵심 로직을 WebAssembly 로 컴파일하여 JavaScript / TypeScript 에서 호출한다.

기존에 IFC 처리는 서버 (IfcOpenShell) 또는 데스크탑 (Revit, BlenderBIM) 에서만 가능했지만, web-ifc 는 클라이언트 한 곳에서 완결한다.

That Open Engine, openBIM 시스템의 기반.

브라우저 BIM 뷰어 / 검토 도구를 만드는 한국 PropTech 팀의 출발점.
