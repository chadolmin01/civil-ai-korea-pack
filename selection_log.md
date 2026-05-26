# 선별 과정 로그

원본 후보 **2059** 개 → 최종 큐레이션 **83** 장.
(후보 중 ko/ 에 promotion 된 카드: 34 · 일부 카드는 후보 발굴 전 수동 추가)

## 발굴 파이프라인

### 1차 — 자동 발굴 (`scripts/discover.ts`)

소스:
- awesome list 5개 (`mitevpi/awesome-bim`, `osama-ata/Awesome-AECO`, `QuantumNovice/awesome-civil-engineering`, etc.)
- GitHub topic 검색 32개 (`topic:bim`, `topic:ifc`, `topic:cad`, `topic:point-cloud`, `topic:structural-analysis` 등)
- GitHub 풀텍스트 검색 9개 (`civil+engineering+language:python+stars:>50` 등)

결과: **2059** 개 후보 (이미 ko/ + `_drafts/` 에 있는 것은 자동 제외)

### 2차 — 자동 카테고리 추정 (`scripts/score-and-draft.ts`)

키워드 매칭으로 8 카테고리 enum 중 1개 매핑. 매칭 실패 → 자동 폐기.

### 3차 — 자동 ★ 등급

휴리스틱 점수 (별 + 활동 + 설명 길이 + corroboration + archived 감점 + fork 감점):
- ≥ 6 → ★★★
- ≥ 4 → ★★
- 그 외 → ★

### 4차 — Lee 의 수동 promotion

자동 등급 ★★★ 부터 *수동 검수* 후 `_drafts/auto/` → `src/content/library/ko/` 이동.
각 카드의 한국 적용 시나리오 (KDS / KCS / BF / KOSHA 매핑) 는 자동이 아닌 *Lee 의 도메인 판단*.

최종 큐레이션 83 카드.

## 최근 promotion 이력 (git log 추출)

- `abee9b4 [야간#67] 워크플로우 갱신 — speckle-multidiscipline 통합 도구 보강`
- `f0be4f0 [야간#66] 워크플로우 갱신 — drawing-pdf-indexing DWG 처리 옵션 확장`
- `c6c9100 [야간#65] 워크플로우 갱신 — bim-delivery-validation 좌표/Revit 보강`
- `9a3ff39 [야간#64] 워크플로우 갱신 — spec-llm-analysis OCR/LLM 도구 추가`
- `7b7d424 [야간#63] 워크플로우 갱신 — bcf-issue-cycle 경량 BIM + 클릭 가속`
- `8c74e1f [야간#62] 워크플로우 갱신 — 4d-bim-schedule-simulation Revit 추출 도구 추가`
- `54275ca [야간#61] 워크플로우 갱신 — bim-cost-estimation Revit/시각화 도구 추가`
- `4fb643d [야간#60] 워크플로우 갱신 — standard-precast-parametric 도구 옵션 확장`
- `ba1a4a7 [야간#59] 워크플로우 갱신 — agent-bim-design-assistant 도구 옵션 확장`
- `5f8e254 [야간#58] 워크플로우 갱신 — facility-iot-monitoring ML/시각화 보강`
- `caa9825 [야간#57] 워크플로우 갱신 — cad-to-bim-migration 신규 CAD/BIM 카드 통합`
- `0974bd3 [야간#56] /notes/[slug] 라우트 추가 — 노트 첫 등록 대비`
- `10d44c6 [야간#55] 워크플로우 갱신 — facility-digital-twin-inspection ML/구조 카드 통합`
- `4b90707 [야간#54] 워크플로우 갱신 — urban-digital-twin 신규 GIS/VIZ 카드 통합`
- `2cff077 [야간#53] 워크플로우 갱신 — seismic-evaluation 단면/해석 도구 보강`
- `6fb489a [야간#52] 워크플로우 갱신 — structural-code-verification 신규 카드 통합`
- `936e665 [야간#51] 워크플로우 갱신 — revit-automation 에 pyRevit/RevitLookup/RevitMCPBridge 통합`
- `25e3d44 [야간#50] ★★ promotion — COMPAS FAB (건설 로봇)`
- `4bc02d7 [야간#49] ★★ promotion — COMPAS XR (AR/VR)`
- `e0993aa [야간#48] /about 통계 섹션 — 라이브러리/워크플로우/노트 카운트 + 카테고리 분포`
- `d1591b5 [야간#47] ★★ promotion — RevitMCPBridge (Revit + LLM)`
- `04119a7 [야간#46] 워크플로우 #19 — 지반 BIM 통합 (시추 + LiDAR + IFC)`
- `1daa00d [야간#45] ★★ promotion 2 — bedrock-ge, FreeCAD-Reinforcement`
- `be0660f [야간#44] ★★ promotion 2 — concrete-properties, FreeCAD Road`
- `246c5fa [야간#43] ★★ promotion 2 — TorchGeo, Open3D-ML (AI 학습 도구)`
- `0a73f58 [야간#42] 워크플로우 #18 — pyRevit 사내 도구 배포 사이클`
- `fdd9927 [야간#41] ★★ promotion — Easy3D (학술 친화 3D)`
- `1add849 [야간#40] ★★ promotion — maptalks.js (2D/3D 통합 지도)`
- `10165fe [야간#39] ★★ promotion 2 — RevitLookup, Hypar Elements`
- `089ae6f [야간#38] ★★ promotion 2 — pyRevit, pythonocc-core (BIM/CAD 강력 도구)`

## 카테고리 분포 (큐레이션 83 장)

- **SURVEY_GIS**: 22
- **VIZ_TWIN**: 15
- **CAD_DWG**: 13
- **BIM_IFC**: 12
- **STRUCTURE_SIM**: 10
- **AGENT_WORKFLOW**: 7
- **SPEC_REVIEW**: 2
- **DRAWING_OCR**: 2

## 등급별 분포 (자동 큐 `_drafts/_QUEUE.md` 기준)

- ★★★: 약 76
- ★★: 약 487
- ★: 약 908
- 자동 폐기 (no category / fetch fail): 약 588

(2059 후보 중 588 ≈ 0 = 모든 후보가 등급 받음)
