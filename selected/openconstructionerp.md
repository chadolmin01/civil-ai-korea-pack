---
name: "OpenConstructionERP"
slug: "openconstructionerp"
category: "BIM_IFC"
summary: "로컬 호스팅 건설 ERP + BIM 물량 산출"
github: "https://github.com/datadrivenconstruction/OpenConstructionERP"
license: "AGPL-3.0"
language: "TypeScript / Python"
korean_applications:
  - "발주 BIM (RVT / IFC / DWG) 의 물량을 사내 표준품셈 코드로 자동 매핑"
  - "다국어 cost catalogue 에 한국 자재 단가 카탈로그 추가"
added: 2026-05-25
---

DataDrivenConstruction (DDC) 가 만든 로컬 우선 (local-first) 건설 ERP.

BOQ, PDF / CAD / BIM takeoff, AI 기반 단가 매칭을 한 자리에서 처리한다. 42 개 지역 카탈로그 + 21 개 언어 + 71 개 모듈.

핵심 차이: 폐쇄 CAD/BIM 파일 (RVT, IFC, DWG, DGN, PLN, TSK) 을 사내 서버에서 직접 ERP 데이터로 변환. 클라우드 / 종속 라이센스 없음.

`pip install openconstructionerp` 로 설치. AGPL-3.0 이라 사내 도구로는 자유롭게 쓰되, 변형해서 외부 판매하려면 라이센스 의무 확인 필요.

같은 단체의 DDC Skills 와 함께 쓰는 것이 설계 의도.

한국 중소 시공사가 BIM 도입을 ERP 통합까지 한 번에 끌어올리고 싶을 때 첫 후보.
