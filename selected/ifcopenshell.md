---
name: "IfcOpenShell"
slug: "ifcopenshell"
category: "BIM_IFC"
summary: "IFC 파일 파싱·편집·포맷 변환"
github: "https://github.com/IfcOpenShell/IfcOpenShell"
license: "LGPL-3.0"
language: "Python / C++"
korean_applications:
  - "조달청 BIM 납품 IFC 파일을 일괄 검수하는 사내 도구 개발"
  - "한국형 BIM 라이브러리 (보, 기둥, 슬래브 표준) IFC 자동 생성 파이프라인"
added: 2026-05-25
---

토마스 크리잘리 (Thomas Krijnen) 가 시작해 현재 커뮤니티가 유지하는 IFC 처리 인프라.

C++ 코어 + Python 바인딩 구조. 대부분의 오픈소스 IFC 도구가 내부적으로 이 라이브러리를 부른다.

IFC2x3 ~ IFC4.3 스키마 파싱, geometry 추출 (OpenCASCADE 기반), 속성 편집, 다른 포맷 (glTF, OBJ, COLLADA) 변환을 한 자리에서 처리한다.

Bonsai (구 BlenderBIM), MCP4IFC, web-ifc 등의 의존 라이브러리.

한국에서 자체 BIM 도구를 만드는 팀의 첫 의존성.
