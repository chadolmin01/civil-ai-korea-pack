---
name: "pythonocc-core"
slug: "pythonocc-core"
category: "CAD_DWG"
summary: "OpenCASCADE Python 바인딩"
github: "https://github.com/tpaviot/pythonocc-core"
license: "LGPL-3.0"
language: "C++ / SWIG"
korean_applications:
  - "FreeCAD / CadQuery 가 부족할 때 *OpenCASCADE 직접 호출* 사내 CAD 도구 작성"
  - "한국 토목 정밀 기하 계산 (Boolean / 절단 / 변환) 의 Python 자동화"
added: 2026-05-25
---

OpenCASCADE (OCCT) 의 Python 바인딩 (SWIG 자동 생성). ★1.9k.

FreeCAD / CadQuery / Mayo 모두 OCCT 위에서 동작. pythonocc-core 는 *그 OCCT 자체를* 직접 호출.

CadQuery 가 *상위 API* (간결, 파라메트릭) 라면, pythonocc-core 는 *하위 API* (모든 OCCT 함수 노출).

학습 곡선 큼 (OCCT 자체 학습 필요), 대신 *모든 CAD 기능* 가능. CadQuery 로 부족한 정밀 기하 작업 (특정 곡선 / 표면 / Boolean 옵션) 에 적합.

STEP / IGES / BREP / STL / IFC import / export. CadQuery / FreeCAD 의 기반.

한국 사내 정밀 CAD 도구 (특수 부재 / 비표준 형상 / 정밀 절단 시뮬레이션) 에 필요.
