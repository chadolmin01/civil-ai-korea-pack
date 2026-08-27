---
type: project_index
project_id: civil_ai_korea_pack
name: "CIVIL AI Korea Pack — 큐레이션 데이터 파이프라인"
identity: "@trySeongmin"
related: "../../CIVILkorea (웹사이트)"
status: active_nightly_automation
tags: [project, domain/civil-ai-curation, identity/trySeongmin, pipeline]
---

# CIVIL AI Korea Pack

`CIVILkorea`(civilai.kr 웹사이트)에 실리는 83개 라이브러리 카드의 **실제 큐레이션
파이프라인 저장소.** `selection_log.md`/`rejected_patterns.md`가 이미 방법론을
완결적으로 문서화하고 있어 재구성 불필요 — 이 노트는 교차 연결만 추가.

## 파이프라인 요약 (원문은 `../selection_log.md` 참조)
2,108개 후보(자동발굴 2,059 + 수동시드 49) → **83장 선별** (자동풀 promotion 34 +
수동시드 49) → 2,025개 탈락. 탈락 사유 7패턴이 `../rejected_patterns.md`에 문서화됨
(라이센스 불명, 도메인 비매칭, 활동정체, 미완성, 중복/파생, 환경종속 과다, 일반
LLM도구 — AEC 무관).

## ⚠️ CIVILkorea와의 수치 연결 확인
`CIVILkorea/ontology/index.md`에서 발견한 `_drafts/auto/`의 1,433개 초안은 바로 이
저장소의 자동발굴 풀(2,059개 중 미승격분, 여기선 2,025로 집계)과 같은 파이프라인의
결과물 — 두 저장소가 실제로 연동되어 있음을 수치로 확인.

## 특이 패턴 — "야간#N" 커밋
`selection_log.md`의 최근 promotion 이력이 전부 `[야간#61]`, `[야간#62]`... 형식 —
**야간에 자동/반자동으로 도는 정기 워크플로우**로 보임(스케줄러 존재 가능성, 교차확인
필요). 카테고리 분포: SURVEY_GIS 22 > VIZ_TWIN 15 > CAD_DWG 13 > BIM_IFC 12 >
STRUCTURE_SIM 10 > AGENT_WORKFLOW 7 > SPEC_REVIEW 2 = DRAWING_OCR 2.

---
*소스: `../selection_log.md`, `../rejected_patterns.md`, `../README.md` 직접 확인, 2026-07-04*
