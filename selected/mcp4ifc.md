---
name: "MCP4IFC"
slug: "mcp4ifc"
category: "BIM_IFC"
summary: "자연어로 IFC 모델 검증 및 편집"
github: "https://github.com/show2instruct/mcp4ifc"
paper: "https://arxiv.org/abs/2511.05533"
license: "MIT"
language: "Python"
korean_applications:
  - "KDS 14 20 50 (콘크리트 철근상세) 조항을 IFC 모델에서 자동 검증"
  - "BF (장애물 없는 생활환경) 인증 항목을 IFC 속성 기반으로 자동 점검"
added: 2026-05-25
---

독일 University of Rostock 과 TU Clausthal 공동 연구팀이 만든 IFC 전용 MCP 서버.

Python 으로 작성됐고, LLM (Claude / GPT 등) 이 자연어로 IFC 모델을 질의·편집하도록 도구를 노출한다.

핵심은 IFC 스키마를 MCP tool 로 매핑하여, "3층 슬래브 두께를 조회해줘" 같은 요청을 IfcOpenShell 호출로 변환하는 것.

학술 논문 (arXiv 2511.05533) 으로도 발표됐다.

한국 BIM 실무자가 KDS / BF 같은 한국 표준 검증 워크플로우를 LLM 으로 자동화하려 할 때 시작점.
