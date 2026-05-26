---
name: "Mayo"
slug: "mayo"
category: "CAD_DWG"
summary: "다양한 3D CAD 포맷 뷰어·변환"
github: "https://github.com/fougue/mayo"
license: "BSD-2-Clause"
language: "C++"
korean_applications:
  - "현장 PC 표준 3D CAD 뷰어 (STEP / IGES / BREP / OBJ / STL 등 모든 주요 포맷)"
  - "사내 자동화 파이프라인의 *변환 단계* (CAD 모델 일괄 포맷 변환 + 측정 정보 추출)"
added: 2026-05-25
---

프랑스 fougue 가 만든 3D CAD 뷰어 + 변환기. ★2k.

OpenCASCADE (OCCT) + Qt 기반. CAD 표준 포맷 (STEP / IGES / BREP / OBJ / STL / glTF / DXF) 의 *뷰어 표준* 자리를 노린다.

핵심 기능: 다중 모델 동시 뷰, 객체 트리 / 속성, 측정 (거리·각도·표면), 단면 (clipping plane), 모델 합치기 / 분리, 모든 지원 포맷 → 다른 포맷 변환.

CAD 모델링 도구가 아니라 *뷰어 + 변환기* — FreeCAD 가 모델링 + 뷰어 통합이라면, Mayo 는 뷰어 + 변환 특화.

한국 시공사 / 발주처의 현장 PC 표준 뷰어, 사내 자동화 파이프라인의 *포맷 변환 단계* 에 적합.
