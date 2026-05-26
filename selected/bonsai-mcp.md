---
name: "Bonsai_mcp"
slug: "bonsai-mcp"
category: "AGENT_WORKFLOW"
summary: "Blender Bonsai 를 MCP 로 노출"
github: "https://github.com/JotaDeRodriguez/Bonsai_mcp"
license: "MIT"
language: "Python"
korean_applications:
  - "발주 IFC 모델을 Blender 에 띄우고 자연어 명령으로 단면 / 속성 검토"
  - "Bonsai 의 IFC 편집 기능을 한국어 명령 (예: \"3층 슬래브 두께 200mm\") 으로 호출"
added: 2026-05-25
---

Juan Rodriguez 가 BlenderMCP 를 포크해 IFC 처리에 특화한 MCP 서버.

Blender 4.0+ / Python 3.12+ / Bonsai BIM 애드온 위에서 동작. 11 개 IFC tool (프로젝트 정보, 엔티티 목록, 속성 조회, 공간 구조 탐색, 관계 분석 등) 을 LLM 에 노출한다.

modelcontextprotocol/servers 의 sequential-thinking tool 도 함께 묶어, 다단계 BIM 검토에 적합.

MCP4IFC (서버 / 헤드리스) 와 달리 Blender GUI 에서 결과를 시각화하면서 LLM 과 대화할 수 있다는 게 차이.

한국 BIM R&D 팀이 시각적 피드백을 받으며 LLM 으로 IFC 편집을 실험할 때 첫 선택지.
