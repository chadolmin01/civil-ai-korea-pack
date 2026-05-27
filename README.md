# CIVIL AI Korea Pack

> 글로벌 토목·건설 AI 오픈소스 **2108** 후보를 **83** 장으로 큐레이션. 그 *과정 전체* 를 자연어로 질의할 수 있는 데이터 자산.

원본 사이트 → [civilai.kr](https://civilai.kr)
라이센스 → CC BY-SA 4.0 (콘텐츠 자유 사용, fork 환영)

---

## 선별 펀넬

![선별 펀넬](./charts/funnel.png)

| 단계 | 통과 | 비고 |
|---|---:|---|
| 자동 발굴 (`scripts/discover.ts`) | **2059** | awesome list 5 + GitHub topic 32 + 풀텍스트 search 9 |
| + 수동 시드 (Lee 가 사이트 빌드 중 직접 추가) | **2108** | discover 전 시점 |
| 자동 카테고리 매칭 (8 enum) | 1,471 | 키워드 1차 필터 — 자율주행 LiDAR / 회로 CAD 등 도메인 비매칭 제거 |
| 자동 ★ 등급 ★★★ | 76 | 별 + 활동 + corroboration 휴리스틱 |
| 수동 promotion + 시드 합산 | **83** | KDS / BF / KOSHA 매핑은 Lee 의 도메인 판단 |

`selection_log.md` 에 4 단계 필터 전 과정. `rejected_patterns.md` 에 7 가지 탈락 사유 패턴.

---

## 카테고리 분포 (선별 83 장)

![카테고리](./charts/category.png)

측량/GIS 22 ↔ 시방 검증 2 — 자동 발굴 풀이 GIS 편향이고, 시방 검증은 오픈소스 자체가 적어 큐레이션도 적음.

---

## 무엇이 이 안에

```
civil-ai-korea-pack/
├── selected/          # 83 카드 (.md) — 한국 적용 시나리오 + 메타
├── candidates.jsonl   # 2108 후보 전체 (selected/rejected 상태)
├── selection_log.md   # 4 단계 필터 + Lee promotion 이력
├── rejected_patterns.md   # 7 가지 탈락 사유 패턴
├── charts/            # matplotlib 시각화 PNG 3장 + generate.py
├── queries/           # OpenCrab 5 질의 결과 + RESULTS.md
└── posts/             # Threads 글 1/3-3/3 초안
```

---

## OpenCrab 인제스트 (검증됨)

```bash
# LocalCrab (local-first, SQLite + ChromaDB)
git clone https://github.com/AlexAI-MCP/OpenCrab && cd OpenCrab
pip install -e ".[dev]"
opencrab ingest -r -e .md,.jsonl /path/to/civil-ai-korea-pack
```

또는 [opencrab.sh](https://opencrab.sh) 호스팅 SaaS 의 "ingest from GitHub URL".

### 자연어 질의 5종 검증 결과

`queries/RESULTS.md` 전체. 대표 질의 한 건:

> "한국 KDS 검증 워크플로우에 묶을 수 있는 도구 조합?"

```
mcp4ifc        0.907  자연어 IFC 모델 검증
text-to-cad    0.853  자연어 CAD 명령 에이전트
hollowrc       0.790  중공 RC 단면 설계
structuralcodes 0.774 Eurocode 식 (KDS 포팅 템플릿)
blueprints     0.719  토목 / 구조 규준 계산식
```

→ 사람이 손으로 묶어야 알았을 4 도구 조합을 hybrid retrieval (vector + BM25 + graph) 이 한 줄 질의로 점수와 함께 반환.

---

## 본인 큐레이션도 같은 방식으로

내 자산은 토목·건설 오픈소스지만, 같은 패턴이 다른 도메인에도 적용됨.

```
당신의 자산 ─→ candidates.jsonl + selected/*.md + selection_log.md ─→ OpenCrab ─→ 자연어 질의
```

이 repo 를 **template 으로 fork** 하면 본인 도메인 (전기 / 기계 / 화공 / 의료 / 디자인) 에 바로 맞출 수 있음.
조정할 것:
1. `candidates.jsonl` 의 schema 는 그대로 (`repo / sources / stars / status` 등)
2. `selected/*.md` 카드 frontmatter 의 `category` enum 을 본인 도메인 분류로
3. `selection_log.md` 에 본인 필터 기준 단계별 기록

---

## 갱신 흐름

원본 사이트 ([civilai.kr](https://civilai.kr)) 의 `src/content/library/ko/` 가 source of truth.
이 팩은 사이트 repo 의 [`scripts/build-pack.ts`](https://github.com/chadolmin01/civil-ai-korea/blob/main/scripts/build-pack.ts) 로 자동 생성.

```
사이트 컨텐츠 변경 ─→ npm run build:pack ─→ 이 repo 자동 갱신 ─→ OpenCrab 재인제스트
```

---

## 만든 사람

- [Lee (Seongmin)](https://tryseongmin.com) · [@trySeongmin](https://www.threads.com/@tryseongmin) (Threads)
- 원본 사이트: [civilai.kr](https://civilai.kr)
- 이슈 / 제안: [GitHub Issues](https://github.com/chadolmin01/civil-ai-korea-pack/issues)

## 영감

- [@alex_ai_mcp](https://github.com/AlexAI-MCP) 의 **OpenCrab** — 자연어 질의 데이터 팩 인프라
- [@logotekton](https://www.threads.com/@logotekton) — *큐레이션 자체가 데이터 자산* 관점

## 라이센스

콘텐츠 (`selected/`, `selection_log.md`, `rejected_patterns.md`) — **CC BY-SA 4.0**
스크립트 (`charts/generate.py`, `queries/summarize.py`) — MIT
`candidates.jsonl` 의 메타데이터 (별 / 라이센스 / 활동 등) — GitHub 공개 API 원천, fair use
