---
name: "OpenSCAD"
slug: "openscad"
category: "CAD_DWG"
summary: "프로그래머의 3D 솔리드 모델링"
github: "https://github.com/openscad/openscad"
license: "GPL-2.0"
language: "C++"
korean_applications:
  - "프리캐스트 / 거푸집 / 표지판 등 *단순 기하* 부재의 코드 기반 모델링 + DXF / STL / STEP 출력"
  - "사내 교육 / 학술 연구의 파라메트릭 모델링 입문 (FreeCAD / CadQuery 보다 진입 장벽 낮음)"
added: 2026-05-25
---

프로그래머 친화의 함수형 3D CAD 모델러. ★9.4k.

CSG (Constructive Solid Geometry) 기반 — 차집합 / 합집합 / 교집합 만으로 형상 정의. 코드가 곧 모델, 변수가 곧 파라미터.

FreeCAD 가 GUI + Sketcher 강점이면, OpenSCAD 는 *코드 100% + 명령행 빌드*. CI 파이프라인에 통합 가능.

CadQuery 가 OCCT 기반 정밀 CAD 라면, OpenSCAD 는 더 단순 / 빠름 — 학습 곡선이 짧아 사내 입문에 적합.

DXF / STL / STEP / OFF 출력. 명령행 (`openscad -o output.stl model.scad`) 으로 일괄 처리.

한국 토목의 단순 기하 부재 (거푸집, 측구, 표지판) 자동화 + 사내 파라메트릭 입문 교육에 적합.
