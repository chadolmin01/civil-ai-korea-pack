---
name: "xeokit BIM Viewer"
slug: "xeokit-bim-viewer"
category: "VIZ_TWIN"
summary: "바로 쓰는 IFC·BIM·점군 웹 뷰어"
github: "https://github.com/xeokit/xeokit-bim-viewer"
license: "AGPL-3.0"
language: "JavaScript"
korean_applications:
  - "감리 / 발주처 사내 BIM 검토 포털 (별도 개발 없이 IFC 모델 드롭 → 즉시 검토)"
  - "현장 검측팀이 BCF 형식으로 issue 를 모델 위에 핀하고 사내 공유"
added: 2026-05-25
---

xeolabs 가 xeokit SDK 위에 만든 *바로 쓸 수 있는* BIM 뷰어 애플리케이션.

xeokit-sdk 가 라이브러리 (개발자가 통합) 라면, BIM Viewer 는 패키지된 완성품 (사내 호스팅 → 사용자가 모델 업로드 → 즉시 뷰).

기능: IFC 2x3 / IFC 4 + 점군 (LAS / LAZ) 동시 뷰, 객체 격리 / 단면 / 측정, BCF (BIM Collaboration Format) 이슈 핀 + 저장 / 불러오기, 다중 모델 로딩, 모바일 대응.

AGPL-3.0 — 자체 호스팅 무료, 변형해서 외부 SaaS 로 제공할 경우 라이센스 의무 검토 필요.

한국 감리법인 / 발주처 BIM 검토팀이 *개발 비용 없이* 사내 BIM 검토 포털을 구축하려 할 때 가장 빠른 선택지.
