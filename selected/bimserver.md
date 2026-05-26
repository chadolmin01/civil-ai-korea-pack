---
name: "BIMserver"
slug: "bimserver"
category: "BIM_IFC"
summary: "IFC 모델을 객체 단위로 서버 관리"
github: "https://github.com/opensourceBIM/BIMserver"
license: "AGPL-3.0"
language: "Java"
korean_applications:
  - "발주처가 IFC 파일을 *파일이 아닌 객체 단위* 로 관리 (변경 이력, 권한, 부분 추출)"
  - "사내 BIM 협업 서버 (Speckle 대신 더 IFC 중심으로 가고 싶을 때)"
added: 2026-05-25
---

네덜란드 BIM Collective 가 만든 Java 기반 IFC 객체 데이터베이스 서버.

핵심 아이디어: IFC 를 *파일* 이 아니라 *객체 단위로* 데이터베이스에 저장. 다중 사용자 접근, 권한 분리, 변경 이력 추적, 부분 추출 (특정 층 / 부재만), 다른 IFC 버전 변환을 서버 차원에서 처리.

Speckle 이 Git-style 다중 CAD 협업이라면, BIMserver 는 *IFC 표준 중심* + Java 백엔드. AEC 표준 준수에 더 엄격하다.

Web 콘솔 + JSON API + Java SDK. 자체 호스팅. AGPL-3.0 라이센스 (외부 서비스화 시 의무 검토 필요).

한국 발주처 / 대형 시공사의 사내 BIM 서버 구축 — 특히 IFC 표준 엄격 준수 + Java 환경 친화 (조달청 등 공공 IT 환경) 가 필요할 때 가장 적합.
