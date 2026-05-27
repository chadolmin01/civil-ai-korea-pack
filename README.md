# CIVIL AI Korea Pack

> 글로벌 토목·건설 AI 오픈소스를 **한국 표준** (KDS / KCS / BF / KOSHA) 에 1:1 매핑한 *첫 한국어* 데이터 자산.

![mappings](https://img.shields.io/badge/매핑-83-0f766e?style=flat-square)
![standards](https://img.shields.io/badge/KDS%20%2F%20BF%20%2F%20KOSHA-mapped-0f766e?style=flat-square)
![categories](https://img.shields.io/badge/categories-8-737373?style=flat-square)
![license](https://img.shields.io/badge/content-CC%20BY--SA%204.0-0f766e?style=flat-square)
![pack](https://img.shields.io/badge/format-OpenCrab%20friendly-737373?style=flat-square)

원본 사이트 → [civilai.kr](https://civilai.kr) · 만든 사람 → [Lee (Seongmin)](https://tryseongmin.com) · [@trySeongmin](https://www.threads.com/@tryseongmin)

---

## 영문 awesome list 가 절대 만들 수 없는 것

KDS · KCS · BF · KOSHA 는 한국어 PDF 다. 글로벌 큐레이터는 *어느 한국 조항* 을 *어느 오픈소스* 로 푸는지 매핑할 수 없다. 이 팩이 그 매핑을 한다.

| 한국 표준 / 실무 시나리오 | 오픈소스 도구 | 매핑 방식 |
|---|---|---|
| **KDS 14 20 50** 콘크리트 철근상세 자동 검증 | [MCP4IFC](./selected/mcp4ifc.md) + [IfcOpenShell](./selected/ifcopenshell.md) | LLM 이 IFC 속성을 자연어로 점검 |
| **KDS 41 17 00** 내진설계 비선형 시간이력 | [OpenSees](./selected/opensees.md) | OpenSeesPy 자동화 파이프라인 |
| **조달청 BIM 납품** IFC 일괄 검수 | [IfcOpenShell](./selected/ifcopenshell.md) | C++ 코어 + Python 바인딩 사내 도구 |
| **BF (장애물 없는 생활환경)** 인증 자동 점검 | [MCP4IFC](./selected/mcp4ifc.md) | 출입구 / 경사로 IFC 속성 추출 |
| 드론 LiDAR → **토공 물량 산정** | [CSFTools](./selected/csftools.md) | Cloth Simulation 지표면 추출 + DEM |
| 교각 / 박스 거더 **중공 RC 단면 검토** | [HollowRC](./selected/hollowrc.md) | Eurocode 2 → KDS 14 20 50 포팅 |

→ `selected/` 의 83 카드 *모두* 가 같은 방식으로 한국 표준에 1:1 매핑되어 있다. 이건 *번역* 이 아니라 *Lee 의 도메인 판단* — 어느 조항·어느 시나리오에 어떻게 쓸지가 frontmatter `korean_applications` 에 명시되어 있다.

---

## 카드 한 장의 모양

```yaml
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

(본문: 영문 README 직역이 아닌 한국어 *재구성* — 핵심 기능, 의존성,
한국 토목 실무자가 시작할 지점, 라이센스 주의사항)
```

`korean_applications` 가 핵심. 영문 README 에 *절대* 없는 한국 도메인 매핑.

---

## 자연어 질의 (보너스)

매핑이 frontmatter 에 있으니 자연어로 *조합* 을 뽑을 수 있다.

```bash
git clone https://github.com/AlexAI-MCP/OpenCrab && cd OpenCrab
pip install -e ".[dev]"
opencrab ingest -r -e .md,.jsonl /path/to/civil-ai-korea-pack
```

> "한국 KDS 검증 워크플로우에 묶을 수 있는 도구 조합?"

```
mcp4ifc          0.907  자연어 IFC 모델 검증
text-to-cad      0.853  자연어 CAD 명령 에이전트
hollowrc         0.790  중공 RC 단면 설계
structuralcodes  0.774  Eurocode 식 (KDS 포팅 템플릿)
blueprints       0.719  토목 / 구조 규준 계산식
```

사람이 awesome list 를 손으로 묶어야 알았을 *4 도구 조합* 을 hybrid retrieval (vector + BM25 + graph) 이 한 줄 질의로 점수와 함께 반환. `queries/RESULTS.md` 에 5 질의 전체 결과.

---

## 큐레이션 과정 (왜 이 83 장인가)

총 **2108** 후보를 4 단계 필터로 83 장으로 좁힘.

![선별 펀넬](./charts/funnel.png)

| 단계 | 통과 | 비고 |
|---|---:|---|
| 자동 발굴 (`scripts/discover.ts`) | **2059** | awesome list 5 + GitHub topic 32 + 풀텍스트 search 9 |
| + 수동 시드 (Lee 가 사이트 빌드 중 직접 추가) | **2108** | discover 전 시점 |
| 자동 카테고리 매칭 (8 enum) | 1,471 | 키워드 1차 필터 |
| 자동 ★ 등급 ★★★ | 76 | 별 + 활동 + corroboration 휴리스틱 |
| 수동 promotion + 한국 매핑 | **83** | KDS / BF / KOSHA 매핑은 Lee 의 도메인 판단 |

핵심은 *마지막 단계* — 76 후보를 ★★★ 만 본 게 아니라, **각 카드의 `korean_applications` 를 Lee 가 한 줄씩 작성**. 이게 다른 awesome list 와의 차이.

`selection_log.md` 4 단계 필터 전 과정 / `rejected_patterns.md` 7 탈락 사유 패턴.

### 카테고리 분포

![카테고리](./charts/category.png)

SURVEY_GIS **22** ↔ SPEC_REVIEW **2** — 자동 발굴 풀의 GIS 편향 + 시방 검증 오픈소스 자체가 적은 현실이 그대로. 인위적 균등 분배 안 함.

### 발굴 출처

![출처](./charts/sources.png)

한 후보가 여러 출처에 동시에 잡힐 수 있다 (corroboration = 신호 강도).

---

## 무엇이 이 안에

```
civil-ai-korea-pack/
├── selected/             # 83 카드 (.md) — 한국 표준 매핑 + frontmatter
├── candidates.jsonl      # 2108 후보 전체 (selected/rejected 상태)
├── selection_log.md      # 4 단계 필터 + Lee promotion 이력
├── rejected_patterns.md  # 7 가지 탈락 사유 패턴
├── charts/               # matplotlib 시각화 PNG 3장 + generate.py
├── queries/              # OpenCrab 5 질의 결과 (q1-q5.json + RESULTS.md)
└── posts/                # Threads 글 1/3-3/3 초안
```

---

## 본인 큐레이션도 같은 방식으로

내 자산은 토목·건설 오픈소스지만, 같은 패턴이 다른 도메인에도 적용된다.

```
당신의 자산 ─→ candidates.jsonl + selected/*.md + selection_log.md ─→ OpenCrab ─→ 자연어 질의
```

이 repo 를 **template 으로 fork** 하면 본인 도메인 (전기 / 기계 / 화공 / 의료 / 디자인) 에 바로 맞출 수 있다.

조정할 것:
1. `candidates.jsonl` 의 schema 는 그대로 (`repo / sources / stars / status` 등)
2. `selected/*.md` frontmatter 의 `category` enum 을 본인 도메인 분류로 (8 개 enum 고정 권장)
3. `selection_log.md` 에 본인 필터 기준 단계별 기록 (자동 발굴 / 키워드 매칭 / 등급 / 수동 promotion)
4. `rejected_patterns.md` 에 본인 도메인의 탈락 사유 (라이센스 / 환경 종속 / 도메인 비매칭 등)
5. `charts/generate.py` 의 카테고리 라벨만 본인 enum 에 맞춰 교체

오픈소스 큐레이션을 *자산화* 하는 게 목적이지, 토목·건설만이 정답이 아니다.

---

## 갱신 흐름

원본 사이트 ([civilai.kr](https://civilai.kr)) 의 `src/content/library/ko/` 가 single source of truth.
이 팩은 사이트 repo 의 [`scripts/build-pack.ts`](https://github.com/chadolmin01/civil-ai-korea/blob/main/scripts/build-pack.ts) 로 자동 생성.

```
사이트 컨텐츠 변경 ─→ npm run build:pack ─→ 이 repo 자동 갱신 ─→ OpenCrab 재인제스트
```

차트는 별도 흐름: `cd charts && python generate.py` (matplotlib + 한글 폰트 필요).

---

## 만든 사람

- [Lee (Seongmin)](https://tryseongmin.com) · [@trySeongmin](https://www.threads.com/@tryseongmin) (Threads)
- 원본 사이트: [civilai.kr](https://civilai.kr)
- 이슈 / 제안: [GitHub Issues](https://github.com/chadolmin01/civil-ai-korea-pack/issues)

## 영감

- [@alex_ai_mcp](https://github.com/AlexAI-MCP) 의 **OpenCrab** — 자연어 질의 데이터 팩 인프라
- [@logotekton](https://www.threads.com/@logotekton) — *큐레이션 자체가 데이터 자산* 관점

## 라이센스

- 콘텐츠 (`selected/`, `selection_log.md`, `rejected_patterns.md`, `posts/`) — **CC BY-SA 4.0**
- 스크립트 (`charts/generate.py`, `queries/summarize.py`) — **MIT**
- `candidates.jsonl` 의 메타데이터 (별 / 라이센스 / 활동 등) — GitHub 공개 API 원천, fair use
