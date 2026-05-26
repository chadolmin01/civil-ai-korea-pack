---
name: "RevitMCPBridge"
slug: "revit-mcp-bridge"
category: "AGENT_WORKFLOW"
summary: "Revit 에 LLM 읽기/쓰기 권한 노출"
github: "https://github.com/weberg619/RevitMCPBridge2026"
license: "MIT"
language: "C#"
korean_applications:
  - "Claude / GPT 등 LLM 에 *Revit 모델 직접 편집* 권한 부여 (700+ MCP endpoint)"
  - "한국 BIM 매니저의 *대화형 사내 도구* — \"이 모델의 3층 슬래브 모두 두께 230mm 로 바꿔\""
added: 2026-05-25
---

Autodesk Revit 의 Read + Write 능력을 Model Context Protocol (MCP) 로 LLM 에 직접 노출하는 다리. ★18 (신생).

MCP4IFC 가 *IFC 헤드리스* 영역이라면 RevitMCPBridge 는 *Revit 라이브 환경* 영역. Rhino.Inside / Bonsai_mcp 의 Revit 버전.

700+ MCP endpoint — Revit API 의 거의 모든 기능 (객체 생성 / 편집 / 속성 / 패밀리 / 시트 / 보기 / 뷰포트) 을 LLM 도구로 노출.

신생 (★18) — 안정성 / 보안 검증 단계. 사내 적용 전 Read-only 모드 시작 권장.

한국 BIM 매니저의 *Claude / GPT 와 Revit 대화형 결합* — pyRevit / Dynamo 위의 LLM 레이어. Revit 중심 (조달청 / LH) 한국 환경에 직접 가치.
