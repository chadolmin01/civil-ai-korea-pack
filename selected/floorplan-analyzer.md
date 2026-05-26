---
name: "FloorPlanAnalyzer"
slug: "floorplan-analyzer"
category: "DRAWING_OCR"
summary: "YOLO 와 OCR 로 평면도 요소 자동 인식"
github: "https://github.com/mageaustralia/FloorPlanAnalyzer"
license: "라이센스 명시 없음"
language: "Python"
korean_applications:
  - "구축 도서 PDF 평면도에서 실명·치수·문 위치를 추출해 IFC 골조 자동 생성"
  - "BF 인증 검토용 통로 폭 / 출입구 너비 자동 측정"
added: 2026-05-25
---

호주 mageaustralia 가 공개한 실험용 평면도 분석 도구.

YOLO 기반 객체 탐지 + OCR 텍스트 인식을 조합해 벽 / 문 / 창 / 실명 등 평면도 요소를 자동 추출한다.

도면 텍스트는 일반 OCR 엔진 (Tesseract, Google Vision) 이 잘 처리하지 못하는 영역 (작은 크기, 회전, 겹침) 이라 딥러닝 기반 접근이 필요하다.

> 라이센스 명시 없음 — 코드 학습용 또는 실험 용도로만 사용하고, 사내 / 상용 활용 전 저자에게 확인 필요.

한국 시공사가 구축 (旣築) 건물의 평면 PDF 를 IFC / Revit 으로 옮기는 파이프라인의 출발점.
