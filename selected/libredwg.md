---
name: "LibreDWG"
slug: "libredwg"
category: "CAD_DWG"
summary: "DWG 직접 읽기·쓰기 라이브러리"
github: "https://github.com/LibreDWG/libredwg"
license: "GPL-3.0"
language: "C"
korean_applications:
  - "AutoCAD / ODA File Converter 없이 DWG 파일 직접 처리 (사내 도구 의존성 축소)"
  - "FreeCAD / LibreCAD 의 DWG 지원 백엔드 — 직접 사용 또는 사내 도구의 라이브러리"
added: 2026-05-25
---

GNU 프로젝트가 유지하는 DWG 파일 직접 처리 C 라이브러리. ★1.4k.

DWG 는 AutoDesk 소유 폐쇄 포맷이지만 LibreDWG 가 리버스 엔지니어링으로 *읽기 + 쓰기* 모두 구현. ODA File Converter 같은 외부 변환기 의존성 회피.

C 코어 + Python / Perl / Ruby / Java 바인딩. FreeCAD / LibreCAD 의 DWG 지원 백엔드.

활성 개발 중이지만 *DWG 의 모든 버전 / 모든 엔티티 완벽 지원* 은 진행 중 — 단순 도면은 OK, 복잡한 동적 블록 / Civil 3D 객체는 한계 있을 수 있음.

한국 사내 도구가 DWG 직접 처리 (변환기 의존 없이) + 오픈소스 라이센스 (GPL-3.0 의무 검토) 가 가능할 때 적합.
