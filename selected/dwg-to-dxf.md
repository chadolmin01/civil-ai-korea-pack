---
name: "dwg_to_dxf"
slug: "dwg-to-dxf"
category: "CAD_DWG"
summary: "ODA 변환기로 DWG 일괄 변환"
github: "https://github.com/oddworldng/dwg_to_dxf"
license: "GPL-3.0"
language: "Python"
korean_applications:
  - "AutoCAD 라이센스 없이 발주 DWG 도서 수천 장을 DXF 로 일괄 변환 후 ezdxf 처리"
  - "사내 도서 아카이브에서 구버전 DWG 를 신규 표준 DXF 로 자동 마이그레이션"
added: 2026-05-25
---

ODA File Converter (구 Teigha) 를 subprocess 로 감싼 얇은 Python 래퍼.

ezdxf 는 DXF 만 직접 다루므로 DWG 작업의 첫 단계로 dwg_to_dxf → ezdxf → 결과 워크플로우가 자연스럽다.

ODA File Converter 는 별도 무료 설치 (https://www.opendesign.com).

GPL-3.0 — 내부 도구로 자유롭게 쓰되, 변형해 외부 배포 시 라이센스 의무 확인 필요.

DWG 파일이 산처럼 쌓여있는데 AutoCAD 라이센스가 부족한 한국 설계사 / 시공사의 가장 빠른 우회로.
