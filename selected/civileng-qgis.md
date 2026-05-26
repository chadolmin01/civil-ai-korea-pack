---
name: "CivilEng (QGIS Provider)"
slug: "civileng-qgis"
category: "SURVEY_GIS"
summary: "QGIS 에서 저수지·토공·LRS 자동 설계"
github: "https://github.com/MBR111/CivilEng"
license: "GPL-3.0"
language: "Python"
korean_applications:
  - "초기 단계 저수지 / 도로 평면 설계를 GIS 데이터 위에서 바로 수행"
  - "LRS (Linear Referencing System) 로 도로·관로의 누가거리 표시 자동 생성"
added: 2026-05-25
---

QGIS 의 처리 프로바이더 (provider) 로 등록되는 초기 단계 토목 설계 도구.

세 가지 핵심 기능:
- Reservoir : 댐 초안 설계 + 침수 면적 계산
- Earthworks : 평탄지 절·성토 계산
- LRS : 폴리라인에 거리 마크 / 텍스트 자동 부착

QGIS 처리 프레임워크에 통합되므로 다른 GIS 데이터 (DEM, 지적, 토양도) 와 한 흐름에서 다룬다.

초기 타당성 / 개념 설계 단계에서 Civil 3D 없이 진행하고 싶은 한국 설계사 / 지자체 토목과 의 출발점.
